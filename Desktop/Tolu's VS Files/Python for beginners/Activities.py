def superpower(name, power):
    print(f"Hi I'm super {name} and my superpower is  {power}!")
superpower("Tolu", "coding")    

def funny_greeting(color, dessert):
    print(f"My favorite dessert is {color} because it tastes so good and my favorite color is {dessert} because it is very pretty!")
funny_greeting("black", "ice cream")   

from datetime import datetime
from datetime import timedelta
def world_times():
    my_city = datetime.now()
    berlin = my_city +timedelta(hours=1)
    baguio = my_city +timedelta(hours=7)
    tokyo = my_city +timedelta(hours=8) 
    all_times = f"""It is {my_city:%I:%M} in my city.
    That means it's {berlin:%I:%M} in Berlin, {baguio:%I:%M} in Baguio city and {tokyo:%I:%M} in Tokyo."""
    print(all_times)
world_times()    