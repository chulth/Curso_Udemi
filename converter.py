



if __name__ == "__main__":
    print('how many kilometers you run today')
    kms = input()
    #print(type(kms)) un input siempre devuelve un str
    miles = float(kms)/1.609 # hay que oconvertir el dato a float para poderlo utilizar
    miles = round(miles,2)
    print('you run {} milles to day'.format(miles))
    
    