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
    
    print("1) Metric to Imperial \n2) Imperial to Metric")
    
    return input("Please choose the corresponding number" +
                       " for the intended category: ")


def temp_metric_us():
    """ Conversion from Metric to U.S Units.
    """
    pass


def temp_us_metric():
    """ Conversion from U.S Units to Metric.
    """
    pass


# __________________________________________________
# ================ LENGTH FUNCTIONS ================
# __________________________________________________
def length():
    """ Converstions between different units of Length.
    """
    pass


def cups_and_spoons():
    """ Conversions between Volume and Cups and/or Spoons.
    """
    pass

    
def eggs():
    """ Conversions for Egg Whites and Egg Yolks between Mass.
    """
    pass


def garlic():
    """ Conversions for fresh Garlic between Units, Mass and Cups
    and/or Spoons, and powdered.
    """
    pass


def onion():
    """ Conversions for fresh Onion between Units, Mass and Cups
    and/or Spoons, and powdered.
    """
    pass


def basil():
    """ Conversions for fresh Basil between Units, Mass, and Cups
    and/or Spoons, and dried.
    """
    pass


def oregano():
    """ Conversions for fresh Oregano between Units, Mass, and Cups
    and/or Spoons, and dried.
    """
    pass



if __name__ == "__main__":
    forever = True
    while forever:
        user_input = main_screen()
        
        if user_input.upper() == "HELP":
            print("1) Mass \n2) Volume \n3) Temperature \n4)" +
                  " Length \n5) Cups and Spoons \n6) Eggs \n7)" +
                  " Garlic \n8) Onions \n9) Basil \n10) Oregano")
            
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
                print(temp_metric_us())