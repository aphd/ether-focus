
module.exports.createLineChart = (data) => {
    console.log(`data.length: ${data.length}`);
    // @ts-ignore
    const ctx = document.getElementById('myLineChart').getContext('2d');
    const chartData = {
        labels: data.map((row) => row.time),
        datasets: [
            {
                label: 'Unconfrirmed traunsaction',
                borderColor: 'rgb(75, 192, 192)',
                data: data.map((row) => row.count),
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
                beginAtZero: false,
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


