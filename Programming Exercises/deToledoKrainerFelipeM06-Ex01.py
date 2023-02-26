import tkinter as tk

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    # Get the temperature in Celsius from the user
    temp = float(celsius_entry.get())
    
    
    # Convert the temperature to Fahrenheit
    fahrenheit = (9/5) * temp + 32
    
    # Display the result in the label
    result_label.config(text=str(fahrenheit) + "°F")


def fahrenheit_to_celsius():

    temp = float(celsius_entry.get())
    
    # Convert the temperature to celsius
    celsius =  (temp - 32) /1.8
    
    # Display the result in the label
    result_label.config(text=str(celsius) + "°F")

# Create the main window
root = tk.Tk()
root.title("Celsius to Fahrenheit Converter")
root.geometry("500x400")

# Create a label to display instructions
instructions_label = tk.Label(root, text="Enter a temperature to convert it to Celsius or Fahrenheit: ")
instructions_label.pack()

# Create an entry widget for the user to enter the temperature in Celsius
celsius_entry = tk.Entry(root)
celsius_entry.pack()

# Create button to trigger the conversion to Fahrenheit
fahrenheit_button = tk.Button(root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
fahrenheit_button.pack()
# Create button to trigger the conversion to Celsius
celsius_button = tk.Button(root, text="Convert to Celsius", command=fahrenheit_to_celsius)
celsius_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()