def validar(entrada:dict):
    
    sql=[
        "UPDATE",
        "INSERT",
        "DELETE",
        "WHERE",
        "SELECT",
        "FROM"
    ]
    sqlSize= len(sql)
    
    atts = list(entrada.keys())
    ret = True
    n = len(atts)
    i=0
    while(ret and i<n):
        entry = entrada[atts[i]]
        if type(entry)==str:
            j=0
            while(ret and j<sqlSize):
                if sql[j] in entry:
                    ret=False
                j+=1
        i+=1
    return ret
