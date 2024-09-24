## #############################################################################
## DRIVER:
## NAVIGATOR:
## #############################################################################

#  This line lets use use the "datetime" functions below, which otherwise wouldn't be available.
import datetime

# The comet speed will not change, so we can define it as a constant
COMET_SPEED = 3860000  # km/day

# We will store the comet's distance from Earth in a variable, because it will change each day.
distance = 100000000  # km

# Gets the current date. We will increment this by one day each time through the loop.
current_date = datetime.datetime.now()

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Do not edit above this line
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Loop through the days until the comet reaches Earth.
# 1. Replace the "???" with the correct condition to enter the loop. We want to keep printing days as long as...?
# while ???:

    # BEGIN LOOP - make sure everything between the beginning and end of the loop is indented by one level

    # 2. Calculate days remaining as the distance divided by the comet's speed.
    # Store it in the "days_remaining" variable.

    # 3. Uncomment the following line to print the current date, distance, and days remaining.
    # print(f'Date: {current_date:%Y-%m-%d}\tComet Distance: {distance:10} km\tJoyous Arrival: {days_remaining:10.1f} days')

    # 4. Update the distance by subtracting the comet's speed from it.

    # 5. Uncomment the following line to increment the current date by one day.
    # current_date = current_date + datetime.timedelta(days=1)

    # END LOOP

# Print the final message to your fellow cult members letting them know that they may rejoice.
print( 'Rejoice! Day of Joyous Arrival is upon us!' )
