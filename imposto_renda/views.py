from django.shortcuts import render

# Create your views here.


def irpf(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        renda_bruta = request.POST.get('salario')
        dependentes = request.POST.get('dependentes')

        renda_bruta = float(renda_bruta == '0' >=0)
        dependentes = int(dependentes == '0'>=0)

        base_calculo = renda_bruta - (dependentes * 2240)
        aliquota = 0.275

        if base_calculo <= 2259.20:
            aliquota = 0
        elif base_calculo <= 2826.65:
            aliquota = 0.075
        elif base_calculo <= 3751.05:
            aliquota = 0.15
        elif base_calculo <= 4664.68:
            aliquota = 0.225
        elif base_calculo > 4664.68:
            aliquota = 0.275

        imposto = base_calculo * aliquota
        salario_liquido = renda_bruta - imposto

        contexto = {
            'imposto': imposto,
            'renda_bruta': renda_bruta,
            'dependentes': dependentes,
            'salario_liquido': salario_liquido,
            'nome': nome
        }

        return render(request, 'irpf.html', contexto)

    return render(request, 'irpf.html')

