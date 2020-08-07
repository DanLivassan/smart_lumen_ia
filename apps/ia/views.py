from django.shortcuts import render
from django.views.generic import View


class HomeView(View):

    def get(self, request, *args, **kwargs):
        data = [
            {
                'disponibilidade': 0.9898725268988021*100,
                'mttr': 2.334685485663481,
                'mtbf': 228.1952267969295,
                'anos_func': 1095 / 365,
                'qtd': 29545,
                'qtd_possivel_falha': 0,
                'color': 'spring'
            },
            {
                'disponibilidade': 0.9878322192591767*100,
                'mttr': 2.2899118511263468,
                'mtbf': 185.90478855497298,
                'anos_func': 1460 / 365,
                'qtd': 23329,
                'qtd_possivel_falha': 0,
                'color': 'amethyst'
            },
            {
                'disponibilidade': 0.9775506815050335*100,
                'mttr': 2.080341059204996,
                'mtbf': 90.58799805636542,
                'anos_func': 1825/365,
                'qtd': 10484,
                'qtd_possivel_falha': 0,
                'color': 'autumn'
            },
            {
                'disponibilidade': 0.9399332599713632*100,
                'mttr': 1.9626820388349515,
                'mtbf': 30.712339743589745,
                'anos_func': 2050/365,
                'qtd': 3650,
                'qtd_possivel_falha': 0,
                'color': 'fire'
            },
        ]
        for i, param in enumerate(data):
            data[i]['qtd_possivel_falha'] = param['qtd']*(100-param['disponibilidade'])/100


        return render(request, 'home.html', {'data': data})
