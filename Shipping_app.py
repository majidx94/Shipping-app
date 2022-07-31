print("""

                                        Welcome to XXXXXX Shipping Company

Ground Shipping

Weight of Package	                            Price per Pound	                Flat Charge
----------------------------------------------------------------------------------------------------
2 lb or less                                           $1.50	                    $20.00
Over 2 lb but less than or equal to 6 lb	       $3.00	                    $20.00
Over 6 lb but less than or equal to 10 lb	       $4.00                        $20.00
Over 10 lb	                                       $4.75	                    $20.00
----------------------------------------------------------------------------------------------------

Ground Shipping Premium Flat charge: $125.00

----------------------------------------------------------------------------------------------------
Drone Shipping

Weight of Package	                           Price per Pound	               Flat Charge
----------------------------------------------------------------------------------------------------
2 lb or less                                           $4.50	                    $0.00
Over 2 lb but less than or equal to 6 lb	       $9.00	                    $0.00
Over 6 lb but less than or equal to 10 lb	       $12.00	                    $0.00
Over 10 lb	                                       $14.25	                    $0.00

""")


weight = float(input("Please Enter your weight: "))

cost_premium = 125.00


#“Ground Shipping”
if weight <= 2:
  cost_ground = (1.5 * weight) + 20

elif weight > 2 and weight <= 6:
  cost_ground = (3.00 * weight) + 20

elif weight > 6 and weight == 10:
  cost_ground = (4.00 * weight) + 20

elif weight > 10:
  cost_ground = (4.75 * weight) +20

print("ground shipping cost is ", cost_ground)

#Premium Shipping
print("ground shipping premium cost is ", cost_premium)

#“Drone Shipping”
if weight <= 2:
  drone_cost = (4.50 * weight)

elif weight > 2 and  weight <= 6:
  drone_cost = (9.00 * weight)

elif weight > 6 and  weight <= 10:
  drone_cost = (12.00 * weight)

elif weight > 10:
  drone_cost = (14.25 * weight)

print("Drone Shipping cost is ", drone_cost)

