    const labels = JSON.parse(document.getElementById('labels-data').textContent);
    const caloriesData = JSON.parse(document.getElementById('calories-data').textContent);
    const proteinData = JSON.parse(document.getElementById('protein-data').textContent);
    const carbsData = JSON.parse(document.getElementById('carbs-data').textContent);
    const fatsData = JSON.parse(document.getElementById('fats-data').textContent);
    const fiberData = JSON.parse(document.getElementById('fiber-data').textContent);
    const sugarData = JSON.parse(document.getElementById('sugar-data').textContent);
    const ctx = document.getElementById('macroChart');
    const macroChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Calories',
                    data: caloriesData,
                    borderColor: '#8b5cf6',
                    backgroundColor: 'rgba(139,92,246,0.08)',
                    fill: false,
                    tension: 0.4,
                    borderWidth: 3
                },
                {
                    label: 'Protein',
                    data: proteinData,
                    borderColor: '#22c55e',
                    fill: false,
                    tension: 0.4,
                    borderWidth: 2
                },
                {
                    label: 'Carbs',
                    data: carbsData,
                    borderColor: '#f59e0b',
                    fill: false,
                    tension: 0.4,
                    borderWidth: 2
                },
                {
                    label: 'Fats',
                    data: fatsData,
                    borderColor: '#ef4444',
                    fill: false,
                    tension: 0.4,
                    borderWidth: 2
                },
                {
                    label: 'Fiber',
                    data: fiberData,
                    borderColor: '#06b6d4',
                    fill: false,
                    tension: 0.4,
                    borderWidth: 2
                },
                {
                    label: 'Sugar',
                    data: sugarData,
                    borderColor: '#ec4899',
                    fill: false,
                    tension: 0.4,
                    borderWidth: 2
                }
            ]
        },
            options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: 'index',
                intersect: false
            },
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        color: '#1e293b',
                        boxWidth: 20,
                        padding: 20
                    }
                },
                tooltip: {
                    enabled: true,
                    mode: 'index',
                    intersect: false,
                    backgroundColor: '#1e293b',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    borderColor: '#8b5cf6',
                    borderWidth: 1,
                    padding: 12
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: '#64748b'
                    },
                    grid: {
                        display: false
                    }
                },
                y: {
                    beginAtZero: true,
                    ticks: {
                        color: '#64748b'
                    },
                    grid: {
                        color: 'rgba(0,0,0,0.05)'
                    }
                }
            }
        }
    });

    $(document).ready(function(){
        calculateTotals();
    });

    function calculateTotals(){
        let totalCalories = 0;
        let totalProtein = 0;
        let totalCarbs = 0;
        let totalFats = 0;
        let totalFiber = 0;
        let totalSugar = 0;
        $('#foodTableBody tr:not(#totalRow)').each(function(){
            totalCalories += parseFloat($(this).find('.kcal').text()) || 0;
            totalProtein += parseFloat($(this).find('.protein').text()) || 0;
            totalCarbs += parseFloat($(this).find('.carbs').text()) || 0;
            totalFats += parseFloat($(this).find('.fats').text()) || 0;
            totalFiber += parseFloat($(this).find('.fiber').text()) || 0;
            totalSugar += parseFloat($(this).find('.sugar').text()) || 0;
        });
        $('#totalCalories').text(totalCalories.toFixed(2));
        $('#totalProtein').text(totalProtein.toFixed(2));
        $('#totalCarbs').text(totalCarbs.toFixed(2));
        $('#totalFats').text(totalFats.toFixed(2));
        $('#totalFiber').text(totalFiber.toFixed(2));
        $('#totalSugar').text(totalSugar.toFixed(2));
    }
    
    function showToast(message, type = 'success') {
        let toast = $('#toast');
        if (!toast.length) {
            $('body').append(`
                <div id="toast" class="toast-success" style="display:none;">
                    <span id="toast-message"></span>
                    <span class="toast-close">&times;</span>
                </div>
            `);
            toast = $('#toast');
        }
        toast.removeClass('toast-success toast-error')
            .addClass(type === 'error' ? 'toast-error' : 'toast-success');
        $('#toast-message').text(message);
        toast.show();
        setTimeout(function () {
            toast.hide();
        }, 5000);
        $('#timelineDrawer').removeClass('open');
        $('body').removeClass('drawer-open');
    }


