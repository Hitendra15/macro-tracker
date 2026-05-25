    const ctx = document.getElementById('macroChart');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
            datasets: [{
                label:'Calories',
                data:[1800,2200,2100,2400,2300,2600,2340],
                borderColor:'#8b5cf6',
                backgroundColor:'rgba(139,92,246,0.15)',
                fill:true,
                tension:0.4,
                borderWidth:4,
                pointRadius:0
            }]
        },
        options:{
            responsive:true,
            plugins:{
                legend:{
                    display:false
                }
            },
            scales:{
                x:{
                    ticks:{
                        color:'#94a3b8'
                    },
                    grid:{
                        color:'rgba(255,255,255,0.05)'
                    }
                },
                y:{
                    ticks:{
                        color:'#94a3b8'
                    },
                    grid:{
                        color:'rgba(255,255,255,0.05)'
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
        $('#foodTableBody tr').each(function(){
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


