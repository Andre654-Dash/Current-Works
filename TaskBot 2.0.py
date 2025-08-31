print("Press Enter to Continue")
wake = input()

while True:

    # What they can do
    print("\nMain Menu")
    print("1. Temperature Advisor")
    print("2. Unit Converter")
    print("3. Calculator | not coded yet")
    print("4. Exit | not coded yet")

    # The choice they pick determines how the program will proceed
    choice = (input("\nSelect one to continue... "))

    if "4" in choice.lower() or "exit" in choice.lower():
        print("Session End")
        break

    if "1" in choice.lower() or "temperature advisor" in choice.lower():
        while True:

            print("Choose a Unit")
            print("a. Fahrenheit")
            print("b. Celsius")
            print("- Type Back to return to main menu <--")

            temperature = (input("Enter a Choice: "))

            if "back" in temperature.lower():
                break

            elif "fahrenheit" in temperature.lower():
                # if user chooses fahrenheit its gives info based on fahrenheit
                temperature_fahrenheit = int(
                    input("Enter the temperature in Fahrenheit: "))

                if temperature_fahrenheit <= 50:
                    print(
                        # below 50 is cold
                        f" since its {temperature_fahrenheit} its chilly outside")

                    response_fahrenheit_cold = input(
                        # asks is the user still wants to go outside
                        "Do you want to go outside still? ")

                    if response_fahrenheit_cold.lower() == "yes" and temperature_fahrenheit <= 50:
                        # yes if cold : take a jacket
                        print("Take a jacket with you!")
                    elif response_fahrenheit_cold.lower() == "no" and temperature_fahrenheit <= 50:
                        # no if cold : turn on heater
                        print("Make sure the heater is on then!")
                        break

                elif temperature_fahrenheit >= 85:
                    print(
                        # above 85 is hot
                        f"since its {temperature_fahrenheit} its hot outsiude")

                    response_fahrenheit_hot = input(
                        # asks is the user still wants to go outside
                        "Do you want to go outside still? ")

                    if response_fahrenheit_hot.lower() == "yes" and temperature_fahrenheit >= 85:
                        # yes if hot : be hydrated
                        print("Besure to be Hydrated then!")
                    elif response_fahrenheit_hot.lower() == "no" and temperature_fahrenheit >= 85:
                        # no if hot : try tommorow
                        print("Thats fine, Maybe tommorow then!")
                        break

                else:
                    # if above 50 and below 85 it's a good day for an outing
                    print("Its nice outside you should go out")

                    response_fahrenheit_warm = input("Do you want to? ")

                    if response_fahrenheit_warm.lower() == "yes" and temperature_fahrenheit > 50 and temperature_fahrenheit < 85:
                        # agrees user should go out
                        print(" Well then do it! It's a nice day for an outing!")
                    elif response_fahrenheit_warm.lower() == "no" and temperature_fahrenheit > 50 and temperature_fahrenheit < 85:
                        # User should rethink going out
                        print("Maybe you should reconsider that")
                break

            # if user choose celcius it give info based on celcius
            elif "celcius" in temperature.lower():
                temperature_celsius = int(
                    input("Enter the temperature in Celsius: "))
                if temperature_celsius <= 15:
                    print(
                        # below 15 is cold
                        f" since its {temperature_celsius} its chilly outside")
                    response_celcius_cold = input(
                        "Do you want to go outside still? ")

                    if response_celcius_cold.lower() == "yes" and temperature_celsius <= 15:
                        print("Take a jacket with you!")
                    # no if cold : turn on heater
                    elif response_celcius_cold.lower() == "no" and temperature_celsius <= 15:
                        print("Make sure the heater is on then!")
                        break

                elif temperature_celsius >= 30:
                    print(
                        # above 30 is hot
                        f"since its {temperature_celsius} its hot outsiude")

                    # asks is the user still wants to go outside
                    response_celsius_hot = input(
                        "Do you want to go outside still? ")

                    if response_celsius_hot.lower() == "yes" and temperature_celsius >= 30:
                        # yes if hot : be hydrated
                        print("Besure to be Hydrated then!")
                    elif response_celsius_hot.lower() == "no" and temperature_celsius >= 30:
                        # no if hot : try tommorow
                        print("Thats fine, Maybe tommorow then!")
                        break
                    # yes if cold : take a jacket

                else:
                    # if above 15 and below 30 its a nice day
                    print("Its nice outside you should go out")

                    response_celsius_warm = input("Do you want to? ")

                    if response_celsius_warm.lower() == "yes" and temperature_celsius > 15 and temperature_celsius < 30:
                        # agrees user should go out
                        print(" Well then do it! It's a nice day for an outing!")
                    elif response_celsius_warm.lower() == "no" and temperature_celsius > 15 and temperature_celsius < 30:
                        # User should rethink going out
                        print("Maybe you should reconsider that")

                break
            else:
                print("Invalid! Please type Fahrenheit or Celsius?: ")

        # if user doesnt type fahrenheit or celcius correctly, it asks them to do it again

    elif "2" in choice.lower() or "unit converter" in choice.lower():
        while True:
            print("Choose a Unit")
            print("a. Temperature")  # 1
            print("b. Length")  # 2
            print("c.  Weight/Mass")  # 3
            print("d.  Volume")  # 4
            print("e. Time")  # 5
            print("f.  Digital Storage")  # 6
            print("g.  Energy")  # 7
            print("- Type Back to return to main menu <--")

            choice_2 = str(input("Enter a choice: "))

            if "back" in choice_2.lower():
                break

            elif choice_2.lower() == "temperature" or choice_2.lower() == "a":
                print("Choose one from down below: ")
                print("a. Celcius --> Fahrenheit")
                print("b. Fahrenheit --> Celcius")
                print("c. Celcius --> Kelvin")

                while True:
                    choice_temperature = str(input("Choose a Conversion: "))
                    if choice_temperature.lower() == "a":  # if user choose a, it solves for fahrenheit
                        degree_in_celcius = int(
                            input("Input degree in Celcius: "))
                        # solves for fahrenheit
                        solve_fahrenheit = (degree_in_celcius * 9/5) + 32
                        print(f"{solve_fahrenheit}°F")  # prints fahrenheit
                        break

                    elif choice_temperature.lower() == "b":
                        degree_in_fahrenheit = int(
                            input("Input degree in Fahrenheit: "))
                        # solves for celcius
                        solve_celcius = (degree_in_fahrenheit - 32) * 5/9
                        print(f"{solve_celcius}°C")        # prints celcius
                        break

                    elif choice_temperature.lower() == "c":
                        degree_in_celcius = int(
                            input("Input degree in Celcius: "))
                        # Solves for kelvin
                        solve_kelvin = (degree_in_celcius + 273.15)
                        print(f"{solve_kelvin}°K")
                        break

                    else:
                        print("Invalid input! Try again..")
                break

            elif choice_2.lower() == "length" or choice_2.lower() == "b":          # if user chooses length
                print("Choose one from down below: ")  # options to choose from
                print("a. Meters --> Kilometers")
                print("b. Kilometers --> Miles")
                print("c. Inches --> Centimeters")

                while True:
                    choice_length = str(input("Choose a Conversion: "))
                    if choice_length.lower() == "a":               # chooses choice a
                        length_in_meters = int(
                            input("Input length in Meters: "))
                        solve_Kilometers = length_in_meters / 1000
                        print(f"{solve_Kilometers}km")
                        break

                    elif choice_length.lower() == "b":               # chose choice b
                        length_in_kilometers = int(
                            input("Input length in Kilometers: "))
                        solve_meters = length_in_kilometers * 0.621371
                        print(f"{solve_meters}m")
                        break

                    elif choice_length.lower() == "c":  # choose choice c
                        length_in_inches = int(
                            input("Input length in Inches: "))
                        solve_centimeters = length_in_inches * 2.54
                        print(f"{solve_centimeters}cm")
                        break

                    else:
                        print("Invalid input! Try again..")
                break

            elif choice_2.lower() == "weight" or choice_2.lower() == "mass" or choice_2.lower() == "c":     # user chooses weight or mass
                print("Choose one from down below: ")
                print("a. Kilograms --> Pounds")
                print("b. Pounds --> Kilograms")
                print("c. Grams --> Kilograms")

                while True:
                    choice_weight = str(input("Choose a Conversion: "))
                    if choice_weight.lower() == "a":                                   # chose choice a
                        weight_in_kilograms = float(
                            input("Input weight in Kilograms: "))
                        solve_pounds = weight_in_kilograms * 2.20462
                        print(f"{solve_pounds}lb")
                        break

                    elif choice_weight.lower() == "b":                       # chose choice b
                        weight_in_pounds = float(
                            input("Input weight in Pounds: "))
                        solve_kilograms = weight_in_pounds / 2.20462
                        print(f"{solve_kilograms}kg")
                        break

                    elif choice_weight.lower() == "c":                   # chose choice c
                        weight_in_grams = float(
                            input("Input weight in grams: "))
                        solve_kilograms = weight_in_grams / 1000
                        print(f"{solve_kilograms}kg")
                        break

                    else:
                        print("Invalid input! Try again..")
                break

            elif choice_2.lower() == "volume" or choice_2.lower() == "d":                          # User chose volume
                print("Choose one from down below: ")
                print("a. Liters --> Mililiters")
                print("b. Liters --> Galons")
                print("c. Cups --> Militers")

                while True:
                    choice_volume = str(input("Choose a Conversion: "))
                    if choice_volume.lower() == "a":                      # chose choice a
                        volume_in_liters = float(
                            input("Input Volume in Liters: "))
                        solve_mililiters = volume_in_liters * 1000
                        print(f"{solve_mililiters}ml")
                        break

                    elif choice_volume.lower() == "b":                         # chose choice b
                        volume_in_liters = float(
                            input("Input Volume in Liters: "))
                        solve_galons = volume_in_liters * 0.264172
                        print(f"{solve_galons}gal")
                        break

                    elif choice_volume.lower() == "c":                            # chose choice c
                        volume_in_cups = float(input("Input Volume in Cups: "))
                        solve_mililiters = volume_in_cups * 236.588
                        print(f"{solve_mililiters}ml")
                        break

                    else:
                        print("Invalid input! Try again..")
                break

            elif choice_2.lower() == "time" or choice_2.lower() == "e":                                  # user chose Time
                print("Choose one from down below: ")
                print("a. Second --> Minutes")
                print("b. Minutes --> Hours")
                print("c. Hours --> Days")

                while True:
                    choice_time = str(input("Choose a Conversion: "))
                    if choice_time.lower() == "a":                                  # chose choice a
                        time_in_seconds = int(input("Input Time in Seconds: "))
                        solve_minutes = time_in_seconds / 60
                        print(f"{time_in_seconds}s = {solve_minutes}min")
                        break

                    elif choice_time.lower() == "b":                                  # chose choice b
                        time_in_minutes = int(input("Input Time in Minutes: "))
                        solve_hours = time_in_minutes / 60
                        print(f"{time_in_minutes}min = {solve_hours}hr")
                        break

                    elif choice_time.lower() == "c":                                   # chose choice c
                        time_in_hours = int(input("Input Time in Hours: "))
                        solve_days = time_in_hours / 24
                        print(f"{time_in_hours}hr = {solve_hours}d")
                        break

                    else:
                        print("Invalid input! Try again..")
                break

            # user chose digital storage
            elif choice_2.lower() == "digital storage" or choice_2.lower() == "f":
                print("Choose one from down below: ")
                print("a. Bytes --> Kilobytes")
                print("b. Kilobytes --> Megabytes")
                print("c. Megabytes --> Gigabytes")

                while True:
                    choice_digital_storage = str(
                        input("Choose a Conversion: "))
                    if choice_digital_storage.lower() == "a":  # chose choice a
                        unit_in_bytes = int(input("Input Unit in Bytes: "))
                        solve_kilobytes = unit_in_bytes / 1024
                        print(f"{unit_in_bytes}B = {solve_kilobytes}kb ")
                        break

                    elif choice_digital_storage.lower() == "b":                           # chose choice b
                        unit_in_kilobyes = int(
                            input("Input Unit in Kilobytes: "))
                        solve_megabytes = unit_in_bytes / 1024
                        print(f"{unit_in_kilobyes}kb = {solve_megabytes}mb")
                        break

                    elif choice_digital_storage.lower() == "c":                            # chose choice c
                        unit_in_megabytes = int(
                            input("Input Unit in Megabytes: "))
                        solve_gigabyte = unit_in_megabytes / 1024
                        print(f"{unit_in_megabytes}mb = {solve_gigabyte}gb")
                        break

                    else:
                        print("Invalid input! Try again..")
                break

            elif choice_2.lower() == "energy" or choice_2.lower() == "g":                            # user chose
                print("Choose one from down below: ")
                print("a. Joules --> Calories")
                print("b. Calories --> Joules")
                print("c. Watt-hours --> Joules")

                while True:
                    choice_energy = str(input("Choose a Conversion: "))
                    if choice_energy.lower() == "a":                                 # chose choice a
                        energy_in_joules = float(
                            input("Input Energy in Joules: "))
                        solve_calories = energy_in_joules / 4.184
                        print(f"{energy_in_joules}J = {solve_calories}cal")
                        break

                    elif choice_energy.lower() == "b":                             # chose choice b
                        energy_in_calories = float(
                            input("Input Energy in Calories: "))
                        solve_joules = energy_in_joules * 4.184
                        print(F"{energy_in_calories}cal = {solve_joules}J")
                        break

                    elif choice_energy.lower() == "c":                           # chose choice c
                        energy_in_watthours = float(
                            input("Input Energy in Watt-Hours: "))
                        solve_joules = energy_in_watthours * 3600
                        print(f"{energy_in_watthours}Wh = {solve_joules}J")
                        break
                    else:
                        print("Invalid input! Try again..")

                break
            else:
                print("Invalid input! Try again..")

    elif "3" in choice.lower() or "calculator" in choice.lower():              # User chose choice 3
        while True:
            print("Choose what you would like to solve for: ")
            print("a. Solve Numbers")
            print("b. Solve Shapes")
            print("- Type Back to return to main menu <--")

            choice_3 = str(input("Enter a choice: "))

            if "back" in choice_3.lower():
                break

            elif choice_3.lower() == "a":
                print("Enter an Equation: ")
                equation = input()
                solve = eval(equation)
                print(f"Total = {solve}")
                break

            elif choice_3.lower() == "b":
                while True:
                    print("Choose a shape")
                    print("a. Square")
                    print("b. Rectangle")
                    print("c. Cicrle")
                    print("d. Triangle")
                    print("e. Cube")
                    print("f. Cylinder")
                    print("g. Cone")
                    print("h. Pyramid")
                    print("i. Triangular Prism")
                    print("- Type Back to return to main menu <--")

                    problem_choice = str(input("Choose an Option: "))

                    if "back" in problem_choice.lower():
                        break

                    elif "a" in problem_choice.lower() or "square" in problem_choice.lower():
                        while True:
                            print("Pick a Problem")
                            print("1. Area")
                            print("2. Perimeter")

                            choice_square = str(input("Choose an Option: "))
                            if "1" == choice_square:
                                print("Area of a Squar: Side * Side.")
                                while True:
                                    side1 = int(input("Input a Side: "))
                                    side2 = int(input("Input another Side: "))
                                    if side1 == side2:
                                        solve_square = side1 * side2
                                        print(f"Area: {solve_square}")
                                        break
                                    else:
                                        print("Error")
                                break
                            elif "2" == choice_square:
                                print("Perimeter of a Square: 4 * Side.")
                                side1 = int(input("Input a Side: "))
                                solve_square = 4 * side1
                                print(f"Perimeter: {solve_square}")
                                break

                            else:
                                print("Invalid Input! Try again...")

                        break

                    elif "b" in problem_choice.lower() or "rectangle" in problem_choice.lower():
                        while True:
                            print("Pick a Problem")
                            print("1. Area")
                            print("2. Perimeter")

                            choice_rectangle = str(input("Choose an Option: "))
                            if "1" == choice_rectangle:
                                print("Area of a Rectangle: Width * Length")
                                width = int(input("Input Width: "))
                                length = int(input("Input Length : "))
                                solve_rectangle = width * length
                                print(f"Area: {solve_rectangle}")
                                break
                            elif "2" == choice_rectangle:
                                print("Perimeter of Rectangle: 2(Length + Width).")
                                width = int(input("Input Width: "))
                                length = int(input("Input Length: "))
                                solve_rectangle = 2 * length + width
                                print(f"Perimeter: {solve_rectangle}")
                                break
                            else:
                                print("Invalid Input! Try again...")
                        break
                    elif "c" in problem_choice.lower() or "cicrcle" in problem_choice.lower():
                        while True:
                            print("Pick a Problem")
                            print("1. Area")
                            print("2. Circumeference")

                            choice_circle = str(input("Choose an Option: "))
                            if "1" == choice_circle:
                                print("Area of a Cricle:  πr2")
                                input_radius = int(input("Input Radius: "))
                                solve_circle = 3.14159265359 * input_radius ** 2
                                print("solve_circle")

                            elif "2" == choice_circle:
                                while True:
                                    print("Enter Diameter or Radius:")
                                    Diameter_or_Radius = str(input())
                                    if "diameter" in Diameter_or_Radius.lower():
                                        print("Circumference of Circle: πd")
                                        diameter = float(
                                            input("Input Diameter: "))
                                        solve_circle_diameter = 3.14159265359 * diameter
                                        print(solve_circle_diameter)
                                    elif "radius" in Diameter_or_Radius.lower():
                                        print("Circumference of Circle: 2πr ")
                                        radius = float(input("Input Radius: "))
                                        solve_circle_radius = 3.14159265359 * radius
                                        print(solve_circle_radius)
                                        break
                                    else:
                                        print("Invalid Input! Try again...")
                                break

                    elif "d" in problem_choice.lower() or "triangle" in problem_choice.lower():
                        while True:
                            print("Pick a Problem")
                            print("1. Area")
                            print("2. Height")

                            choice_triangle = str(input("Choose an Option: "))
                            if "1" == choice_triangle:
                                print("Area of Triangle:  ½ (b × h)")
                                base = float(input("Input Base: "))
                                height = float(input("Input Height"))
                                solve_triangle = 0.5 * base * height
                                print(solve_triangle)
                            elif "2" == choice_triangle:
                                print("Height of Triangle: 2A/b)")
                                Area = float(input("Input Area"))
                                base = float(input("Input Base: "))
                                solve_Triangle = 2 * Area/base
                                print(solve_triangle)
                                break
                            else:
                                print("Invalid Input! Try again...")
                        break

                    elif "e" in problem_choice.lower() or "cube" in problem_choice.lower():
                        while True:
                            print("Pick a Problem")
                            print("1. Volume")
                            print("2. Surface Area")
                            choice_cube = str(input("Choose an Option: "))
                            if "1" == choice_cube:
                                print("Volume: a3")
                                edge = float(input("Input Edge: "))
                                solve_cube = edge ** 3
                                print(solve_cube)
                            elif "2" == choice_cube:
                                print("Surface Area of Cube: 6a2")
                                edge = float(input("Input Edge: "))
                                solve_cube = 6 * edge ** 2
                                print(solve_cube)
                                break
                            else:
                                print("Invalid Input! Try again...")
                        break

                    elif "f" in problem_choice.lower() or "cylinder" in problem_choice.lower():
                        while True:
                            print("Pick a Problem")
                            print("1. Volume")
                            print("2. Height")
                            choice_cylinder = str(input("Choose an Option: "))
                            if "1" == choice_cylinder:
                                print("Volume of Cylinder: πr² h")
                                radius_cylinder = int(input("Input Radius: "))
                                height_cylinder = int(input("Input Height: "))
                                solve_cylinder = 3.14159265359 * radius_cylinder ** 2 * height_cylinder
                                print(solve_cylinder)
                            elif "2" == choice_cylinder:
                                print("Height of Cylinder: V / (πr²)")
                                volume = float(input("Input Volume: "))
                                radius_cylinder = float(
                                    input("Input Radius: "))
                                solve_cylinder = volume / \
                                    (3.14159265359 * radius_cylinder ** 2)
                                print(solve_cylinder)
                                break
                            else:
                                print("Invalid Input! Try again...")
                        break

                    elif "g" in problem_choice.lower() or "cone" in problem_choice.lower():
                        while True:
                            print("Pick a Problem")
                            print("1. Volume")
                            print("2. Height")
                            choice_cone = str(input("Choose an Option: "))
                            if "1" == choice_cone:
                                print("Volume of Cone: πr²h/3 ")
                                radius_cone = float(input("Input Radius: "))
                                height_cone = float(input("Input Height: "))
                                solve_cone = 3.14159265359 * \
                                    radius_cone ** 2 * (height_cone / 3)
                                print(solve_cone)
                            elif "2" == choice_cone:
                                print("Height of Cone: (3V) / (πr²)")
                                volume_cone = float(input("Input Volume: "))
                                radius_cone = float(input("Input Radius: "))
                                solve_cone = (3 * volume_cone) / \
                                    (3.14159265359 * radius_cone ** 2)
                                print(solve_cone)
                                break
                            else:
                                print("Invalid Input! Try again...")
                        break
                    elif "h" in problem_choice.lower() or "pyramid" in problem_choice.lower():
                        while True:
                            print("Triangular or Rectangular?")
                            ans_triangular_or_rectangular = str(input())
                            while True:
                                if ans_triangular_or_rectangular.lower() == "rectangular":
                                    print("Pick a Problem")
                                    print("1. Volume")
                                    print("2. Height")
                                    choice_rectangular_pyramid = str(
                                        input("Choose an Option: "))
                                    if choice_rectangular_pyramid == "1":
                                        print(
                                            "Volume of Rectangular Pyramid: lwh / 3")
                                        width_pyramid = float(
                                            input("Input Width: "))
                                        height_pyramid = float(
                                            input("Input Height: "))
                                        length_pyramid = float(
                                            input("Input Length: "))
                                        solve_rectangular_pyramid = (
                                            width_pyramid * height_pyramid * length_pyramid) / 3
                                        print(solve_rectangular_pyramid)
                                    elif choice_rectangular_pyramid == "2":
                                        print(
                                            "Height of Rectangular Pyramid: 3 * V / LW")
                                        volume_pyramid = float(
                                            input("Input Volume: "))
                                        width_pyramid = float(
                                            input("Input Width: "))
                                        length_pyramid = float(
                                            input("Input Length: "))
                                        solve_rectangular_pyramid = 3 * volume_pyramid / \
                                            (length_pyramid * width_pyramid)
                                        print(solve_rectangular_pyramid)
                                        break
                                    else:
                                        print("Invalid Input! Try again...")

                                elif ans_triangular_or_rectangular.lower() == "triangular":
                                    print("Pick a Problem")
                                    print("1. Volume")
                                    print("2. Height")
                                    choice_triangular_pyramid = str(
                                        input("Choose an Option: "))
                                    if choice_triangular_pyramid == "1":
                                        print(
                                            "Volume of Triangular Pyramid: 1/3 * Base Area *H")
                                        base_area = float(
                                            input("Input Base Area: "))
                                        height_triangular_pyramid = float(
                                            input("Input Height: "))
                                        solve_triangular_pyramid = 1/3 * base_area * height
                                        print(solve_triangular_pyramid)
                                    elif choice_triangular_pyramid == "2":
                                        print(
                                            "Height of Triangular Pyramid: 3 * Volume / Base Area")
                                        volume_triangular_pyramid = float(
                                            input("Input Volume: "))
                                        base_area = float(
                                            input("Input Base Area: "))
                                        solve_triangular_pyramid = 3 * volume_triangular_pyramid * base_area
                                        print(solve_triangular_pyramid)
                                        break
                                    else:
                                        print("Invalid Input! Try again...")
                                break
                            break
                    else:
                        print("Invalid Input! Try again...")
                break

            else:
                print("Invalid Input! Try again...")

    elif "4" in choice.lower() or "exit" in choice.lower():
        print("session end")
        break

    else:
        print("Option does not exist. Please try again...")
