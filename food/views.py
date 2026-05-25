from django.shortcuts import render
from .models import Food,Consume
from django.utils.timezone import now
from django.db.models import Sum
from django.http import JsonResponse
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
    todays_calories = Consume.objects.filter(user=request.user,consumed_at__date=today).aggregate(total_calories=Sum('food_consumed__calories'))
    todays_proteins = Consume.objects.filter(user=request.user,consumed_at__date=today).aggregate(todays_proteins=Sum('food_consumed__protein'))
    todays_carbs = Consume.objects.filter(user=request.user,consumed_at__date=today).aggregate(todays_carbs=Sum('food_consumed__carbs'))
    user_food_consumes = Consume.objects.filter(user=request.user)
    total_calories = todays_calories['total_calories'] or 0
    goal_percentage = round((total_calories / daily_goal) * 100)
    if goal_percentage > 100:
        goal_percentage = 100
    return render(
        request,
        'food/index.html',
        {
            'foods': foods,
            'user_food_consumes': user_food_consumes,
            'todays_calories': todays_calories['total_calories'] or 0,
            'todays_proteins': todays_proteins['todays_proteins'] or 0,
            'todays_carbs': todays_carbs['todays_carbs'] or 0,
            'goal_percentage': goal_percentage
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
            todays_calories = Consume.objects.filter(user=request.user,consumed_at__date=today).aggregate(total_calories=Sum('food_consumed__calories'))
            todays_proteins = Consume.objects.filter(user=request.user,consumed_at__date=today).aggregate(todays_proteins=Sum('food_consumed__protein'))
            todays_carbs = Consume.objects.filter(user=request.user,consumed_at__date=today).aggregate(todays_carbs=Sum('food_consumed__carbs'))
            total_calories = todays_calories['total_calories'] or 0
            goal_percentage = round((total_calories / daily_goal) * 100)
            if goal_percentage > 100:
                goal_percentage = 100
            return JsonResponse({
                'success': True,
                'message': 'Consumed food deleted successfully',
                'id': consume_id,
                'todays_calories': todays_calories['total_calories'] or 0,
                'todays_proteins': todays_proteins['todays_proteins'] or 0,
                'todays_carbs': todays_carbs['todays_carbs'] or 0,
                'goal_percentage': goal_percentage
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