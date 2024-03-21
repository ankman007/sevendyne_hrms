// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Access the candidates data// Access the skill counts data
var skillCountsElement = document.getElementById("candidateSkills");
var skillCountsData = JSON.parse(skillCountsElement.getAttribute("data-skills"));

// Prepare data for the pie chart
var skillLabels = Object.keys(skillCountsData);
var skillData = Object.values(skillCountsData);

// Pie Chart Example
var ctx = document.getElementById("myPieChart").getContext('2d');
var myPieChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: skillLabels,
        datasets: [{
            data: skillData,
            backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#ff0000', '#00ff00', '#0000ff'], // Add more colors as needed
            hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf', '#ff6666', '#66ff66', '#6666ff'], // Hover colors
            hoverBorderColor: "rgba(234, 236, 244, 1)",
        }],
    },
    options: {
        maintainAspectRatio: false,
        tooltips: {
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: false,
            caretPadding: 10,
        },
        legend: {
            display: false
        },
        cutoutPercentage: 80,
    },
});
