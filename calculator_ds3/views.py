from django.http import JsonResponse
from math import floor

from django.shortcuts import render


def levels_2_12(level):
    times = level - 2
    return floor(673 * (pow((1 + 2.5 / 100), times)))

def levels_13_onwards(level):
    return floor(0.02 * pow(level, 3) + 3.06 * pow(level, 2) + 105.6 * level + 895)

def min_souls_needed(level):
    souls_2_12 = sum(levels_2_12(lvl) for lvl in range(2, min(level + 1, 13)))
    souls_13_onwards = sum(levels_13_onwards(lvl) for lvl in range(13, level + 1))
    return souls_2_12 + souls_13_onwards

def souls_needed(current, desired):
    if desired <= current or desired < 2:
        return 0

    min_current = min_souls_needed(current)
    min_desired = min_souls_needed(desired)
    return min_desired - min_current

# View to render the form page
def calculator_form(request):
    return render(request, 'calculator_ds3/calculator_ds3.html')

def calculate_souls(request):
    calculator_form(request)
    current_level = request.GET.get('current_level')
    desired_level = request.GET.get('desired_level')

    if current_level is None or desired_level is None:
        return JsonResponse({'error': 'Invalid input'}, status=400)

    current_level = int(current_level)
    desired_level = int(desired_level)

    souls = souls_needed(current_level, desired_level)
    return JsonResponse({'souls_needed': souls})
