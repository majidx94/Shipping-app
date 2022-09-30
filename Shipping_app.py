

def welcome_page():
    print("""

                                            Welcome to XXXXXX Shipping Company

    Ground Shipping

    Weight of Package	                            Price per Pound	                Flat Charge
    ----------------------------------------------------------------------------------------------------
    2 lb or less                                       $1.50	                    $20.00
    Over 2 lb but less than or equal to 6 lb	       $3.00	                    $20.00
    Over 6 lb but less than or equal to 10 lb	       $4.00                        $20.00
    Over 10 lb	                                       $4.75	                    $20.00
    ----------------------------------------------------------------------------------------------------

    Ground Shipping Premium Flat charge: $125.00

    ----------------------------------------------------------------------------------------------------
    Drone Shipping

    Weight of Package	                           Price per Pound	               Flat Charge
    ----------------------------------------------------------------------------------------------------
    2 lb or less                                       $4.50	                    $0.00
    Over 2 lb but less than or equal to 6 lb	       $9.00	                    $0.00
    Over 6 lb but less than or equal to 10 lb	       $12.00	                    $0.00
    Over 10 lb	                                       $14.25	                    $0.00

    """)


while True:

    class variable:
        sentence1 = "Please Enter your weight: "
        sentence2 = "ground shipping cost is "
        sentence3 = "Premium Shipping cost is "
        sentence4 = "Drone Shipping cost is "
        sentence5 = '\nDo you want to repeat(y/n)'
        cost_premium = 125.00

    
    
    
    welcome_page()                                  #this function to call the welcome page 
    inputs = variable()                             #Assign class to a variable
    
    weight = float(input(inputs.sentence1))         #Ask user to enter the weight inputs is to call the class and sentence1 in the class



    #“Ground Shipping”
    if weight <= 2:
      cost_ground = (1.5 * weight) + 20

    elif weight > 2 and weight <= 6:
      cost_ground = (3.00 * weight) + 20

    elif weight > 6 and weight == 10:
      cost_ground = (4.00 * weight) + 20

    elif weight > 10:
      cost_ground = (4.75 * weight) +20


    print(inputs.sentence2, cost_ground)            #Print out the sentence2 and show the result for the ground cost

    #Premium Shipping
    print(inputs.sentence3, inputs.cost_premium)    #Print out the sentence3 and show the result for the Premium Shipping

    #“Drone Shipping”
    if weight <= 2:
      drone_cost = (4.50 * weight)

    elif weight > 2 and  weight <= 6:
      drone_cost = (9.00 * weight)

    elif weight > 6 and  weight <= 10:
      drone_cost = (12.00 * weight)

    elif weight > 10:
      drone_cost = (14.25 * weight)
   

    print(inputs.sentence4, drone_cost)             #Print out the sentence4 and show the result for the Drone Shipping

    if input(inputs.sentence5) == 'n':              #To repeat the request if the user ask to repeat
        break

    