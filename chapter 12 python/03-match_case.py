def http_stuts(stuts):
    match stuts:
        case 200:
            return "Ok"
        case 404:
            return "Not found"
        case 500:
            return "Internet Erro"
        case _:
            return "Unkhown Stuts"
        

print(http_stuts(404))
    