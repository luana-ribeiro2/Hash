class Hash:
    def _init_(self, string):
        self.string = string.lower()
        self.tab = [0]*26
        for x in self.string:
           self.tab[self.numero(x)] += 1
           
    def contem(self, letra):
        return self.tab[self.numero(letra)] > 0
        
    def numero(self,letra):
        return ord(letra) - ord('a')
        
t = int(input())
for x in range(t):
    string1 = input()
    string2 = input()
    aux = False
    for j in string1:
        for i in string2:
            if (j == i):
                aux = True
    if (aux == False):
        print ('Nao Compartilham Substring')

    else:
        print('Compartilham Substring')
