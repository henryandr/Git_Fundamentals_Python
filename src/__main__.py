from functions import calculate_payment, compare_numbers, factorial, menu

def main():
    option = 0
    while option != 4:
        option = menu()
        if option == 1
            hours = float(input("Please, enter the..**//**/.: "))
            value_per_hour = float(input("Enter the value ***----* USD$: "))
            total_to_pay = calculate_payment(hours,value_per_hour)
            print(f"{hours} hours worked. USD${value_per_hour} per hour")
            print(f"Total to pay = USD${total_to_pay}")
        
        elif option == 2:
            print("You are going to compare two numbers")
            number1 = int(input("Please, *******//////: "))
            number2 = int(input("Please, /*/*/*/*/*/*/: "))
            print(f"first number greater: {compare_numbers(number1,number2)}")
            
        elif option == 3:
            print("Calculating the Factorial")
            number = int(input("Please, ////******/:"))
            fact_result = factorial(number)
            print(f"{number}! = {fact_result}")
        
        elif option == 4:
            print("¡Thanks for using our app!"
        
        else:
            print("¡You must choose from the defined options!")


if __name__ == '__main__':
    main()