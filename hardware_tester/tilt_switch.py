from gpiozero import Button

button = Button(22, pull_up=False)

while True:
    if button.is_pressed:
        print("The button was pressed!!")
    else:
        print("Not pressed")