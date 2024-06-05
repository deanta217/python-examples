import requests, json, rich, os, sys, yagmail, keyring
from rich import print as rprint
email = input("Enter Email. \n")
receiver = input("Receiving Email \n")
password = keyring.get_password("yagmail", email)
yag = yagmail.SMTP(email, password)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def get_alerts(abbreviation):
    global alerts
    url = "https://api.weather.gov/alerts/active?area=" + abbreviation
    alerts = requests.get(url)
def setup_table():
    global states
    states = " 1. Alabama \n 2. Alaska \n 3. Arizona \n 4. Arkansas \n 5. California \n 6. Colorado \n 7. Connecticut \n 8. Delaware \n 9. Florida \n 10. Georgia \n 11. Hawaii \n 12. Idaho \n 13. Illinois \n 14. Indiana \n 15. Iowa \n 16. Kansas \n 17. Kentucky \n 18. Louisiana \n 19. Maine \n 20. Maryland \n 21. Massachusetts \n 22. Michigan \n 23. Minnesota \n 24. Mississippi \n 25. Missouri \n 26. Montana \n 27. Nebraska \n 28. Nevada \n 29. New Hampshire \n 30. New Jersey \n 31. New Mexico \n 32. New York \n 33. North Carolina \n 34. North Dakota \n 35. Ohio \n 36. Oklahoma \n 37. Oregon \n 38. Pennsylvania \n 39. Rhode Island \n 40. South Carolina \n 41. South Dakota \n 42. Tennessee \n 43. Texas \n 44. Utah \n 45. Vermont \n 46. Virginia \n 47. Washington \n 48. West Virginia \n 49. Wisconsin \n 50. Wyoming"
def abbreviationConvert():
    global symbol
    if state == 1:
        symbol = "AL"
    elif state == 2:
        symbol = "AK"
    elif state == 3:
        symbol = "AZ"
    elif state == 4:
        symbol = "AR"
    elif state == 5:
        symbol = "CA"
    elif state == 6:
        symbol = "CO"
    elif state == 7:
        symbol = "CT"
    elif state == 8:
        symbol = "DE"
    elif state == 9:
        symbol = "FL"
    elif state == 10:
        symbol = "GA"
    elif state == 11:
        symbol = "HI"
    elif state == 12:
        symbol = "ID"
    elif state == 13:
        symbol = "IL"
    elif state == 14:
        symbol = "IN"
    elif state == 15:
        symbol = "IA"
    elif state == 16:
        symbol = "KS"
    elif state == 17:
        symbol = "KY"
    elif state == 18:
        symbol = "LA"
    elif state == 19:
        symbol = "ME"
    elif state == 20:
        symbol = "MD"
    elif state == 21:
        symbol = "MA"
    elif state == 22:
        symbol = "MI"
    elif state == 23:
        symbol = "MN"
    elif state == 24:
        symbol = "MS"
    elif state == 25:
        symbol = "MO"
    elif state == 26:
        symbol = "MT"
    elif state == 27:
        symbol = "NE"
    elif state == 28:
        symbol = "NV"
    elif state == 29:
        symbol = "NH"
    elif state == 30:
        symbol = "NJ"
    elif state == 31:
        symbol = "NM"
    elif state == 32:
        symbol = "NY"
    elif state == 33:
        symbol = "NC"
    elif state == 34:
        symbol = "ND"
    elif state == 35:
        symbol = "OH"
    elif state == 36:
        symbol = "OK"
    elif state == 37:
        symbol = "OR"
    elif state == 38:
        symbol = "PA"
    elif state == 39:
        symbol = "RI"
    elif state == 40:
        symbol = "SC"
    elif state == 41:
        symbol = "SD"
    elif state == 42:
        symbol = "TN"
    elif state == 43:
        symbol = "TX"
    elif state == 44:
        symbol = "UT"
    elif state == 45:
        symbol = "VT"
    elif state == 46:
        symbol = "VA"
    elif state == 47:
        symbol = "WA"
    elif state == 48:
        symbol = "WV"
    elif state == 49:
        symbol = "WI"
    elif state == 50:
        symbol = "WY"
while True:
    clear_screen()
    setup_table()
    rprint("[blue]Welcome to NWS alert searcher!")
    print(states)
    while True:
        state = int(input("Enter the state number you would like. \n"))
        if state > 0 and state < 51:
            break
        else:
            rprint("[yellow]Please enter a number between 1 and 50!")
            
    abbreviationConvert()
    #print(symbol) not used
    get_alerts(symbol)
    clear_screen()
    title = alerts.json()['title']
    total = str(len(alerts.json()['features'])) + " total statements."
    print(title)
    print(total)
    yag.send(to=receiver, contents=title + "\n\n" + total, subject="Important Weather Update")
    while True:
        keep = input("Would you like to check alerts for other states? (y/n)\n")
        if keep.upper() == "Y":
            break
        elif keep.upper() == "N":
            rprint("[blue]Thanks for using!")
            exit()
        else:
            rprint("[red]Please enter Y or N.")