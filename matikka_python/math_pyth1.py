import numpy as np
a = 2.493
b = 0.911
c = 137.7
d = 62.3
print("Tehtävä 1")
print(f"Vastaus 1 : {np.degrees(a)}")
print(f"Vastaus 2 : {np.degrees(b)}")
print("Tehtävä 2")
print(f"Vastaus 1 : {np.radians(c)}")
print(f"Vastaus 2 : {np.radians(d)}")
print("\nTehtävä 3 " )
angles = [30,45,60,90,120, 135, 150, 180 ,270, 360]
for angle in angles:
    radians= np.radians(angle)
    print(f"{angle} : {radians:.4f} ")

print("\nTehtävä 2.2.1 \nTehtävä 1")

x = 1.6
y = 2.3
hypotenus = np.hypot(x,y)
print(f"hypotenuusa pituus kun kateetit on 1.6 ja 2.3 :{hypotenus}")



