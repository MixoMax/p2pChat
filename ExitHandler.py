def Exit_Code(code):
    match code:
        case 2: return "Could not connect to server"
        case 3: return "Could not connect to server"

def help(code):
    match code:
        case 2: return "Check your internet connection and try again\nThe Problem may be on our end, please try again later"
        case 3: return "The IP Handler is currently down, please try again later"