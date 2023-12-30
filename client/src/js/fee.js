
module.exports.createFeePriceChart = (data) => {
    console.log(`data.length: ${data.length}`);
    // @ts-ignore
    const ctx = document.getElementById('fee').getContext('2d');
    const chartData = {
        labels: data.map((row) => row.time),
        datasets: [
            {
                label: 'High Priority Fee',
                borderColor: 'rgb(255, 102, 102)',
                data: data.map((row) => row.high_priority_fee),
                fill: false,
            },
            {
                label: 'Low Priority Fee',
                borderColor: 'rgb(153, 255, 153)',
                data: data.map((row) => row.low_priority_fee),
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


