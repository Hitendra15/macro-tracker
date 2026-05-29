from django.shortcuts import render
from .models import Food,Consume
from django.utils.timezone import now
from django.db.models import Sum
from django.http import JsonResponse
from datetime import timedelta
# Create your views here.
def index(request):
    if request.method == "POST":
        food_id = request.POST['food']
        food_consumed = Food.objects.get(pk=food_id)
        Consume.objects.create(
            user=request.user,
            food_consumed=food_consumed
        )
    foods = Food.objects.all()
    today = now().date()
    daily_goal = 2500
    protein_goal = 150
    carbs_goal = 300
    fats_goal = 70
    fiber_goal = 30
    sugar_goal = 50
    consumes = Consume.objects.filter(
        user=request.user,
        consumed_at__date=today
    )
    totals = consumes.aggregate(
        total_calories=Sum('food_consumed__calories'),
        total_protein=Sum('food_consumed__protein'),
        total_carbs=Sum('food_consumed__carbs'),
        total_fats=Sum('food_consumed__fats'),
        total_fiber=Sum('food_consumed__fiber'),
        total_sugar=Sum('food_consumed__sugar'),
    )
    total_calories = totals['total_calories'] or 0
    total_protein = totals['total_protein'] or 0
    total_carbs = totals['total_carbs'] or 0
    total_fats = totals['total_fats'] or 0
    total_fiber = totals['total_fiber'] or 0
    total_sugar = totals['total_sugar'] or 0
    goal_percentage = round((total_calories / daily_goal) * 100)
    if goal_percentage > 100:
        goal_percentage = 100
    calories_percent = round((total_calories / daily_goal) * 100)
    protein_percent = round((total_protein / protein_goal) * 100)
    carbs_percent = round((total_carbs / carbs_goal) * 100)
    fats_percent = round((total_fats / fats_goal) * 100)
    fiber_percent = round((total_fiber / fiber_goal) * 100)
    sugar_percent = round((total_sugar / sugar_goal) * 100)
    calories_percent = min(calories_percent, 100)
    protein_percent = min(protein_percent, 100)
    carbs_percent = min(carbs_percent, 100)
    fats_percent = min(fats_percent, 100)
    fiber_percent = min(fiber_percent, 100)
    sugar_percent = min(sugar_percent, 100)
    labels = []
    calories_data = []
    protein_data = []
    carbs_data = []
    fats_data = []
    fiber_data = []
    sugar_data = []
    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        weekly_totals = Consume.objects.filter(
            user=request.user,
            consumed_at__date=day
        ).aggregate(
            calories=Sum('food_consumed__calories'),
            protein=Sum('food_consumed__protein'),
            carbs=Sum('food_consumed__carbs'),
            fats=Sum('food_consumed__fats'),
            fiber=Sum('food_consumed__fiber'),
            sugar=Sum('food_consumed__sugar')
        )
        labels.append(day.strftime('%a'))
        calories_data.append(float(weekly_totals['calories'] or 0))
        protein_data.append(float(weekly_totals['protein'] or 0))
        carbs_data.append(float(weekly_totals['carbs'] or 0))
        fats_data.append(float(weekly_totals['fats'] or 0))
        fiber_data.append(float(weekly_totals['fiber'] or 0))
        sugar_data.append(float(weekly_totals['sugar'] or 0))
    user_food_consumes = Consume.objects.filter(user=request.user)
    return render(
        request,
        'food/index.html',
        {
            'foods': foods,
            'user_food_consumes': user_food_consumes,
            'todays_calories': total_calories,
            'todays_proteins': total_protein,
            'todays_carbs': total_carbs,
            'goal_percentage': goal_percentage,
            'labels': labels,
            'calories_data': calories_data,
            'protein_data': protein_data,
            'carbs_data': carbs_data,
            'fats_data': fats_data,
            'fiber_data': fiber_data,
            'sugar_data': sugar_data,
            'calories_percent': calories_percent,
            'protein_percent': protein_percent,
            'carbs_percent': carbs_percent,
            'fats_percent': fats_percent,
            'fiber_percent': fiber_percent,
            'sugar_percent': sugar_percent,
            'daily_goal': daily_goal,
            'protein_goal': protein_goal,
            'carbs_goal': carbs_goal,
            'fats_goal': fats_goal,
            'fiber_goal': fiber_goal,
            'sugar_goal': sugar_goal,
        }
    )

def delete_consume(request):
    if request.method == "POST":
        consume_id = request.POST.get('id')
        try:
            consume = Consume.objects.get(pk=consume_id)
            consume.delete()
            today = now().date()
            daily_goal = 2500
            protein_goal = 150
            carbs_goal = 300
            fats_goal = 70
            fiber_goal = 30
            sugar_goal = 50
            consumes = Consume.objects.filter(
                user=request.user,
                consumed_at__date=today
            )
            totals = consumes.aggregate(
                total_calories=Sum('food_consumed__calories'),
                total_protein=Sum('food_consumed__protein'),
                total_carbs=Sum('food_consumed__carbs'),
                total_fats=Sum('food_consumed__fats'),
                total_fiber=Sum('food_consumed__fiber'),
                total_sugar=Sum('food_consumed__sugar'),
            )
            total_calories = totals['total_calories'] or 0
            total_protein = totals['total_protein'] or 0
            total_carbs = totals['total_carbs'] or 0
            total_fats = totals['total_fats'] or 0
            total_fiber = totals['total_fiber'] or 0
            total_sugar = totals['total_sugar'] or 0
            goal_percentage = round((total_calories / daily_goal) * 100)
            calories_percent = round((total_calories / daily_goal) * 100)
            protein_percent = round((total_protein / protein_goal) * 100)
            carbs_percent = round((total_carbs / carbs_goal) * 100)
            fats_percent = round((total_fats / fats_goal) * 100)
            fiber_percent = round((total_fiber / fiber_goal) * 100)
            sugar_percent = round((total_sugar / sugar_goal) * 100)
            goal_percentage = min(goal_percentage, 100)
            calories_percent = min(calories_percent, 100)
            protein_percent = min(protein_percent, 100)
            carbs_percent = min(carbs_percent, 100)
            fats_percent = min(fats_percent, 100)
            fiber_percent = min(fiber_percent, 100)
            sugar_percent = min(sugar_percent, 100)
            labels = []
            calories_data = []
            protein_data = []
            carbs_data = []
            fats_data = []
            fiber_data = []
            sugar_data = []
            for i in range(6, -1, -1):
                day = today - timedelta(days=i)
                weekly_totals = Consume.objects.filter(
                    user=request.user,
                    consumed_at__date=day
                ).aggregate(
                    calories=Sum('food_consumed__calories'),
                    protein=Sum('food_consumed__protein'),
                    carbs=Sum('food_consumed__carbs'),
                    fats=Sum('food_consumed__fats'),
                    fiber=Sum('food_consumed__fiber'),
                    sugar=Sum('food_consumed__sugar')
                )
                labels.append(day.strftime('%a'))
                calories_data.append(float(weekly_totals['calories'] or 0))
                protein_data.append(float(weekly_totals['protein'] or 0))
                carbs_data.append(float(weekly_totals['carbs'] or 0))
                fats_data.append(float(weekly_totals['fats'] or 0))
                fiber_data.append(float(weekly_totals['fiber'] or 0))
                sugar_data.append(float(weekly_totals['sugar'] or 0))
            return JsonResponse({
                'success': True,
                'message': 'Consumed food deleted successfully',
                'id': consume_id,
                'todays_calories': total_calories,
                'todays_proteins': total_protein,
                'todays_carbs': total_carbs,
                'goal_percentage': goal_percentage,
                'labels': labels,
                'calories_data': calories_data,
                'protein_data': protein_data,
                'carbs_data': carbs_data,
                'fats_data': fats_data,
                'fiber_data': fiber_data,
                'sugar_data': sugar_data,
                'calories_percent': calories_percent,
                'protein_percent': protein_percent,
                'carbs_percent': carbs_percent,
                'fats_percent': fats_percent,
                'fiber_percent': fiber_percent,
                'sugar_percent': sugar_percent,
            })
        except Consume.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Record not found'
            })
    return JsonResponse({
        'success': False,
        'message': 'Invalid request'
    })