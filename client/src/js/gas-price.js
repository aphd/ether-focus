
module.exports.createGasPriceChart = (data) => {
    console.log(`data.length: ${data.length}`);
    // @ts-ignore
    const ctx = document.getElementById('gas-price').getContext('2d');
    const chartData = {
        labels: data.map((row) => row.time),
        datasets: [
            {
                label: 'High Gas Price',
                borderColor: 'rgb(75, 0, 192)',
                data: data.map((row) => row.high_gas_price),
                fill: false,
            },
            {
                label: 'Low Gas Price',
                borderColor: 'rgb(192, 192, 0)',
                data: data.map((row) => row.low_gas_price),
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


