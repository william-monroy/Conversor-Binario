class Solution:
    '''String -> ASCII -> binary'''
    def transform(self, stringToTransform):
        resultado_final = ''
        for letra in stringToTransform:
          numero = ord(letra)
          resultado = format(numero,'08b')
          resultado_final = resultado_final + resultado + ' '
        return resultado_final

print('Codificador Binario 8bits\n')
stringToTransform = input('Introduce el texto a codificar: ')
print('Resultado:',Solution().transform(stringToTransform))