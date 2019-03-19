from gpiozero import Button

button = Button(4, pull_up=False)

while True:
    if button.is_pressed:
        print("The button was pressed!!")