print('seja bem vindo a calculadora de media do aluno - 2025') 

nm = input("digite o nome do aluno: ")
idd = input("turma do aluno:")
ec = input('digite o turno do aluno:')
print("**agora passaremos as notas do aluno**")
nt1 =float (input ("digite a nota 1° bim: "))
nt2=float (input ("digite a nota 2° bim: "))
nt3=float (input ("digite a nota 3° bim: "))
nt4=float (input("digite a nota 4° bim: "))
ng = nt1+nt2+nt3+nt4 
r1= ng /4
print("aqui esta os dados do aluno:\n nome:{}}\n idade: {}\n escola: {}\n\n a nota final do aluno foi igual a:{}".format (nm, idd, ec, ng))

if ng >=20:
    print ('aprovado, parabéns sua media foi igual: {}'.format(r1))
else: 
    print ('reprovado, sua média ficou a baixo dos 20 pontos, nota: {} estude mais.'.format(r1))