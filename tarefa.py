print("aula do git")
while True:
 nota1 = int(input("digite sua primeira nota:\n"))
 nota2= int (input("digite sua segunda nota:\n"))
 nota3= int(input("digite sua segunda nota:\n"))
 media=(nota1+nota2+nota3)/3

 if nota1 <0 or nota2<0 or nota3<0:
    print("erro")
    continue
 else:
    print(media)
 if media >0 and media<10:
    break