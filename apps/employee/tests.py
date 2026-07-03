from datetime import date
from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse

from apps.employee.models import AttendanceRegister, Department, Designation, Employee
from apps.main.models import Company, CompanyAccess, Country, State


class AttendanceExportCSVTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name="hrms_clients")

        self.user = User.objects.create_user(
            username="client",
            password="password123",
        )
        self.user.groups.add(self.group)

        self.country = Country.objects.create(
            name="Nepal",
            iso3="NPL",
            iso2="NP",
            numeric_code="524",
            phone_code="977",
            capital="Kathmandu",
            currency="NPR",
            currency_symbol="Rs",
            tld=".np",
            native="Nepali",
            region="Asia",
            subregion="South Asia",
            latitude="28",
            longitude="84",
        )

        self.state = State.objects.create(
            country=self.country,
            name="Bagmati",
            country_code="NP",
            state_code="BA",
            latitude="27",
            longitude="85",
        )

        self.company = Company.objects.create(
            auto_id=1,
            creator=self.user,
            updator=self.user,
            name="Demo Company",
            contact_person="Admin",
            address="Kathmandu",
            country=self.country,
            state=self.state,
            city="Kathmandu",
            postal_code="44600",
            email="demo@test.com",
            phone="9800000000",
        )

        CompanyAccess.objects.create(
            user=self.user,
            company=self.company,
            group=self.group,
            is_accepted=True,
            is_default=True,
        )

        self.department = Department.objects.create(
            auto_id=1,
            a_id=1,
            creator=self.user,
            updator=self.user,
            company=self.company,
            name="Engineering",
        )

        self.designation = Designation.objects.create(
            auto_id=1,
            a_id=1,
            creator=self.user,
            updator=self.user,
            company=self.company,
            department=self.department,
            name="Developer",
        )

        self.employee = Employee.objects.create(
            auto_id=1,
            a_id=1,
            creator=self.user,
            updator=self.user,
            company=self.company,
            user=self.user,
            firstname="Danger",
            lastname="Doe",
            username="client",
            password="password123",
            email="demo@test.com",
            phone="9800000000",
            department=self.department,
            designation=self.designation,
            employeeid="EMP001",
            joindate=date.today(),
        )

        AttendanceRegister.objects.create(
            auto_id=1,
            a_id=1,
            creator=self.user,
            updator=self.user,
            company=self.company,
            employee=self.employee,
            date=date.today(),
            status="present",
        )

    def test_export_attendance_csv(self):
        self.client.login(
            username="client",
            password="password123",
        )

        session = self.client.session
        session["current_company"] = str(self.company.pk)
        session.save()

        response = self.client.get(
            reverse("employee:export_attendance_register_csv")
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/csv")

        content = response.content.decode()

        self.assertIn("Employee,Date,Status", content)
        self.assertIn("Danger Doe", content)
        self.assertIn("Present", content)