# Problem 3: Widgets and Gizmos

# An online retailer sells two products: widgets and gizmos. Each widget weighs 75 grams.
# Each gizmo weighs 112 grams.
# Write a program that reads the number of widgets and the number of gizmos from the
# user. Then your program should compute and display the total weight of the parts.

# Define weights of widgets and gizmos
widget_weight = 75  # Each widget weighs 75 grams
gizmo_weight = 112  # Each gizmo weighs 112 grams

# Input the number of widgets and gizmos
num_widgets = int(input("Enter the number of widgets: "))
num_gizmos = int(input("Enter the number of gizmos: "))

# Calculate the total weight
total_weight = (num_widgets * widget_weight) + (num_gizmos * gizmo_weight)

# Display the result
print(f"The total weight of the parts is: {total_weight} grams")
