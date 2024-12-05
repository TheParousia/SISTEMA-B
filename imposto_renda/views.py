from django.shortcuts import render

# Create your views here.


def irpf(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        renda_bruta = request.POST.get('salario')
        dependentes = request.POST.get('dependentes')
        cpf = request.POST.get('cpf')

        

        renda_bruta = float(renda_bruta)
        dependentes = int(dependentes)
        
        # Base de Cálculos
        valor_dependente = dependentes * 189.59
        base_calculo = renda_bruta - valor_dependente
        aliquota = {0, 0.075, 0.15, 0.225, 0.275}

        # Cáculo do IRRF
        if base_calculo <= 2259.20:
            aliquota = 0
        elif base_calculo <= 2826.65:
            aliquota = 0.075
        elif base_calculo <= 3751.05:
            aliquota = 0.15
        elif base_calculo <= 4664.68:
            aliquota = 0.225
        else:
            aliquota = 0.275

        imposto = base_calculo * aliquota
        salario_liquido = renda_bruta - imposto

        aliquota = aliquota * 100
        
        contexto = {
            'imposto': imposto,
            'renda_bruta': renda_bruta,
            'dependentes': dependentes,
            'salario_liquido': salario_liquido,
            'valor_dependente': valor_dependente,
            'nome': nome,
            'valor_aliquota': aliquota,
            'cpf': cpf
        }

        return render(request, 'irpf.html', contexto)

    return render(request, 'irpf.html')
