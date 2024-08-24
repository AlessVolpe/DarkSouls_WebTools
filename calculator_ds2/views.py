from functools import lru_cache

from django.http import JsonResponse
from django.shortcuts import render


# The following functions are not precise, the coefficients aren't right
def cost_1_to_200(level):
    return 0.01 * level**3 - 1.5 * level**2 + 100 * level + 5000

def cost_201_to_400(level):
    return 0.02 * level**3 - 3.0 * level**2 + 200 * level + 10000

def cost_401_to_600(level):
    return 0.03 * level**3 - 4.5 * level**2 + 300 * level + 15000

def cost_601_to_800(level):
    return 0.04 * level**3 - 6.0 * level**2 + 400 * level + 20000

def cost_801_to_838(level):
    return 0.05 * level**3 - 7.5 * level**2 + 500 * level + 25000

level_functions = [
    (200, cost_1_to_200),
    (400, cost_201_to_400),
    (600, cost_401_to_600),
    (800, cost_601_to_800),
    (838, cost_801_to_838),
]

@lru_cache(maxsize=None)
def min_cost(level):
    for upper_bound, func in level_functions:
        if level <= upper_bound:
            return func(level)

def souls_needed(current, desired):
    if desired <= current or desired < 2:
        return 0

    return round(sum(min_cost(level) for level in range(current, desired + 1)))

# View to render the form page
def calculator_form2(request):
    return render(request, 'calculator_ds/calculator_ds2.html')

def calculate_souls2(request):
    calculator_form2(request)
    current_level = request.GET.get('current_level')
    desired_level = request.GET.get('desired_level')

    if current_level is None or desired_level is None:
        return JsonResponse({'error': 'Invalid input'}, status=400)

    current_level = int(current_level)
    desired_level = int(desired_level)

    souls = souls_needed(current_level, desired_level)
    return JsonResponse({'souls_needed': souls})