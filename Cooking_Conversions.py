__author__ = "Paul Grochocinski"
__copyright__ = "Copyright (C) 2013 Paul Grochocinski"
__licence__ = "Public Domain"
__version__ = "1.0"

# After calculation functions add user input control with exceptions
#     Check whether value is given (default is 1)
#     Check whether units are given (default is oz, g, imperial)

def main_screen():
    """ The main screen for choosing which conversion category to choose
    and getting the user's input so that redirection can take place.
    """
    
    return input("Please choose the category in which conversion" +
                 " is needed.\nType 'help' if you need assistance: ")


# __________________________________________________    
# ================ MASS FUNCTIONS ==================
# __________________________________________________
def mass():
    """ Conversions between different units of Mass.
    """
    
    print("1) Metric to U.S Units \n2) U.S Units to Metric")
    
    return input("Please choose the corresponding number" +
                       " for the intended category: ")
    

def mass_metric_us():
    """ Conversion from Metric to U.S Units.
    """
    
    user_input = input("Please enter amount and unit (ex. 1 g): ")
    user_input = user_input.split()
    
    if user_input[-1] == "g":
        conv_1 = round((int(user_input[0]) * (1/28)), 2)
        conv_2 = round((int(user_input[0]) * (1/454)), 2)
        return (user_input[0] + " " + user_input[-1] + " is " + 
                str(conv_1) + " ounces, or " + str(conv_2) + " pounds.")
    if user_input[-1] == "kg":
        conv_1 = round((int(user_input[0]) * (1/907)), 2)
        conv_2 = round((int(user_input[0]) * (1/0.45)), 2)
        return (user_input[0] + " " + user_input[-1] + " is " +
                str(conv_2) + " pounds, or " + str(conv_1) + " tons.")


def mass_us_metric():
    """ Conversion from U.S Units to Metric.
    """
    
    user_input = input("Please enter amount and unit (ex. 1 oz): ")
    user_input = user_input.split()
    
    if user_input[-1] == "oz":
        conv =  round((int(user_input[0]) * 28), 2)
        return (user_input[0] + " " + user_input[-1] + " is " + str(conv)
                + " grams.")
    if user_input[-1] == "lb":
        conv_1 = round((int(user_input[0]) * 454), 2)
        conv_2 = round((int(user_input[0]) * 0.45), 2)
        return (user_input[0] + " " + user_input[-1] + " is " + 
                str(conv_1) + " grams, or " + str(conv_2) + 
                " kilograms.")
    if user_input[-1] == "t":
        conv =  round((int(user_input[0]) * 907), 2)
        return (user_input[0] + " " + user_input[-1] + " is " + str(conv)
                + " kilograms.")
   
    
# __________________________________________________
# ================ VOLUME FUNCTIONS ================
# __________________________________________________
def volume():
    """ Conversions between different units of Volume.
    """
    
    print("1) Metric to U.S Units \n2) U.S Units to Metric \n3)" +
          " Metric to Imperial \n4) Imperial to Metric \n5)" +
          " U.S Units to Imperial \n6) Imperial to U.S Units")
    
    return input("Please choose the corresponding number" +
                       " for the intended category: ")

def volume_metric_us():
    """ Conversion from Metric to U.S Units.
    """
    pass


def volume_us_metric():
    """ Conversion from U.S Units to Metric.
    """
    pass


# __________________________________________________
# ================ TEMPERATURE FUNCTIONS ===========
# __________________________________________________
def temperature():
    """ Converstions between different units of Temperature.
    """
    
    print("1) Celsius \n2) Fahrenheit \n3) Imperial")
    
    return input("Please choose the corresponding number" +
                       " for the intended category: ")


def cel():
    """ Conversion from Celsius.
    """
    
    user_input = input("Please enter temperature: ")
    
    conv_fah = int(round((((int(user_input) * 9) / 5) + 32) / 5) * 5)
    
    if int(user_input) == 105:
        conv_imp = "1/3"
    elif int(user_input) == 120:
        conv_imp = "1/2"
    elif int(user_input) < 105:
        conv_imp = "not possible in"
    else:
        conv_imp = int((conv_fah / 25) % 10)
        
    return (user_input + " Celsius is " + str(conv_fah) + 
            " Fahrenheit, or " + str(conv_imp) + " Gas Mark(Imperial).")


def fah():
    """ Conversion from Fahrenheit.
    """
    
    user_input = input("Please enter temperature: ")
    
    if int(user_input) == 225:
        conv_imp = "1/3"
    elif int(user_input) == 250:
        conv_imp = "1/2"
    elif int(user_input) < 225:
        conv_imp = "not possible in"
    else:
        conv_imp = int((int(user_input) / 25) % 10)
    conv_cel = int(round((((int(user_input) - 32) * 5) / 9) / 5) * 5)
    
    return (user_input + " Fahrenheit is " + str(conv_cel) + 
            " Celsius, or " + str(conv_imp) + " Gas Mark(Imperial).")
    

def imp():
    """ Conversion from Imperial.
    """
    
    user_input = input("Please enter temperature: ")
    
    if user_input == "1/3":
        conv_cel = 105
        conv_fah = 225
    elif user_input == "1/2":
        conv_cel = 120
        conv_fah = 250
    else:
        conv_fah = (10 + int(user_input)) * 25
        conv_cel = int(round((((conv_fah - 32) * 5) / 9) / 5) * 5)
    
    return (user_input + " Gas Mark(Imperial) is " + str(conv_cel) + 
            " Celsius, or " + str(conv_fah) + " Fahrenheit.")


# __________________________________________________
# ================ LENGTH FUNCTIONS ================
# __________________________________________________
def length():
    """ Converstions between different units of Length.
    """
    
    print("1) Centimeters \n2) Inches")
    
    return input("Please choose the corresponding number" +
                       " for the intended category: ")


def cm_in():
    """ Conversion from centimeters or inches.
    """
    
    user_input = input("Please enter length: ")
    conv_in = round(int(user_input) * 0.39)
    
    return (user_input + " Centimeters is " + str(conv_in) + " Inches.")


def in_cm():
    """ Conversion from inches to centimeters.
    """
    
    user_input = input("Please enter length: ")
    conv_cm = round(int(user_input) * 2.54)
    
    return (user_input + " Inches is " + str(conv_cm) + " Centimeters.")


# __________________________________________________
# ================ CUP/SPOONS FUNCTIONS ============
# __________________________________________________
def cups_and_spoons():
    """ Conversions between Volume and Cups and/or Spoons.
    """
    pass


# __________________________________________________
# ================ EGG FUNCTIONS ===================
# __________________________________________________
def eggs():
    """ Conversions for Egg Whites and Egg Yolks between Mass.
    """
    pass


# __________________________________________________
# ================ GARLIC FUNCTIONS ================
# __________________________________________________
def garlic():
    """ Conversions for fresh Garlic between Units, Mass and Cups
    and/or Spoons, and powdered.
    """
    pass


# __________________________________________________
# ================ ONION FUNCTIONS =================
# __________________________________________________
def onion():
    """ Conversions for fresh Onion between Units, Mass and Cups
    and/or Spoons, and powdered.
    """
    pass


# __________________________________________________
# ================ BASIL FUNCTIONS =================
# __________________________________________________
def basil():
    """ Conversions for fresh Basil between Units, Mass, and Cups
    and/or Spoons, and dried.
    """
    pass


# __________________________________________________
# ================ OREGANO FUNCTIONS ===============
# __________________________________________________
def oregano():
    """ Conversions for fresh Oregano between Units, Mass, and Cups
    and/or Spoons, and dried.
    """
    pass


# __________________________________________________
# ================ BUTTER FUNCTIONS ================
# __________________________________________________
def butter():
    """ Conversions for butter between sticks, Cups, and Mass.
    """
    pass



if __name__ == "__main__":
    forever = True
    while forever:
        user_input = main_screen()
        
        if user_input.upper() == "HELP":
            print("1) Mass \n2) Volume \n3) Temperature \n4)" +
                  " Length \n5) Cups and Spoons \n6) Eggs \n7)" +
                  " Garlic \n8) Onions \n9) Basil \n10) Oregano" +
                  "\n11) Butter")
            
        if user_input.upper() == "MASS":
            conv_type = mass()
            if conv_type == "1":
                print(mass_metric_us())
            if conv_type == "2":
                print(mass_us_metric())
        
        if user_input.upper() == "VOLUME":
            conv_type = volume()
            if conv_type == "1":
                print(volume_metric_us())
        
        if user_input.upper() == "TEMPERATURE":
            conv_type = temperature()
            if conv_type == "1":
                print(cel())
            if conv_type == "2":
                print(fah())
            if conv_type == "3":
                print(imp())
        
        if user_input.upper() == "LENGTH":
            conv_type = length()
            if conv_type == "1":
                print(cm_in())
            if conv_type == "2":
                print(in_cm())
                