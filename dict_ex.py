dict={'Yes':["Oui","wee"],"No":["Non","nong"],"That's fine":["C'est bien","say byang "],"I like it":["Ça me plaît","sahm play"],"How?":["Comment?","kommahng"],"I want..":["Je veux...","zher ver"],"How many?":["Combien?","kong-byang"],"Which?":["Laquelle?","ler-kell"],"Where?":["Où?","oo"],"Sorry":["Désolé(e)","day-zo-lay"],"When?":["Quand?","kahng"],"Goodbye":["Au revoir","oh rer-vwahr"],"Good night":["Bonne nuit","bonn nwee"],"Excuse me":["Excusez-moi","ex-kewzay mwah"],"Do you speak English?":["Est-ce que vous parlez anglais?","essker voo pahrlay ahng-glay"],"Leave me alone!":["Laissez-moi tranquille","lay-say mwah trahng-keel"]}


sen=input("enter your sentence:").split(" ")
a=""
a1=""
for i in range(len(sen)):
    if(sen[i] in dict.keys()):
         list=dict[sen[i]]
         
         a=a+" "+list[0]
         
         a1=a1+" "+list[1]
    
    elif(sen[i] not in dict.keys()):
         a=a+" "+sen[i]
         a1=a1+"  "+sen[i]      
        # print(sen[i],end=' ')

print(a,end="  ")
print(a1,end="   ")
     
