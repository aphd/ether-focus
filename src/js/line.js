
module.exports.createLineChart = (data) => {
    // @ts-ignore
    const ctx = document.getElementById('myLineChart').getContext('2d');
    const chartData = {
        labels: data.map((row) => row.Month),
        datasets: [
            {
                label: 'Unconfrirmed traunsaction',
                borderColor: 'rgb(75, 192, 192)',
                data: data.map((row) => row.Sales),
                fill: false,
            },
        ],
    };

    const chartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: {
                type: 'category',
                position: 'bottom',
            },
            y: {
                beginAtZero: true,
            },
        },
    };

    // @ts-ignore
    new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: chartOptions,
    });
};


