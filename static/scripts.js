document.addEventListener('DOMContentLoaded', () => {
    let index = 1;
    for (const tenant in tenants) {
        const ctx = document.getElementById(`chart${index}`).getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
                datasets: [{
                    label: 'Active Users',
                    data: tenants[tenant].chart,
                    borderColor: '#ffd700',
                    backgroundColor: 'rgba(255,215,0,0.2)',
                    tension: 0.4
                }]
            },
            options: { responsive: true, plugins: { legend: { display: false } }, scales: { y: { beginAtZero: true } } }
        });
        index++;
    }
});
