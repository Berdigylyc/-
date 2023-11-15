import numpy as np
import matplotlib.pyplot as plt

#Our data
data0 = np.loadtxt('data_0.txt')
data1 = np.loadtxt('data_1.txt')
data3 = np.loadtxt('data_3.txt')
data4 = np.loadtxt('data_4.txt')


# Function to calculate speed of sound based on temperature and humidity
def speed_of_sound(data_0, data_1):
    maxValueData0 = np.max(data_0)
    maxValueData1 = np.max(data_1)
    print("max value 0: ", maxValueData0, "max value 1: ", maxValueData1)
    position0 = np.argmax(data_0)
    position1 = np.argmax(data_1)
    print("pos 0: ", position0, "pos 1: ", position1)

    time = 0.01018
    timeDiv =time/5000

    time0 = position0 * timeDiv
    print("time0: ", time0)
    time1 = position1 * timeDiv
    print("time1: ", time1)

    differenceTime = time1 - time0
    print("time: : ", differenceTime)

    length = 1.158
    # Your analytical function for speed of sound calculation
    # Replace this with the actual formula you have
    # e.g., speed = some_function(temperature, humidity
    speed = length/differenceTime
    return speed
print("speed: ", speed_of_sound(data0, data1))

print("speed: ", speed_of_sound(data3, data4))

def speedOfSound(temperature, humidity):

    R = 8.31446  # Universal gas constant

    # Constants for air (mixture of nitrogen, oxygen, and argon)
    m_noa = 0.02897
    c_p_noa = 1.0036
    c_v_noa = 0.7166

    # Constants for carbon dioxide
    m_y = 0.04401
    c_p_y = 0.838
    c_v_y = 0.649

    # Constants for water vapor
    m_h = 0.01801
    c_p_h = 1.863
    c_v_h = 1.403

    x = 0.03/100
    y = ((22.4*20.5*(humidity/100))/(1000*0.018))/1000
    print("y: ", y)

    M = m_noa*(1 - y - x) + m_y*y + m_h*x

    gama = (m_noa*c_p_noa*(1-y-x)+m_y*c_p_y*y+m_h*c_p_h*x)/(m_noa*c_v_noa*(1-y-x)+m_y*c_v_y*y+m_h*c_v_h*x)

    soundSpeed = ((gama*R*temperature)/M)**0.5

    print("Result: ", soundSpeed)
    return soundSpeed


T = 296.45 #23.3
H = 37.4 # 0.374 otnositelnoe


speedOfSound(T, H)

def speedOfSoundCO2(co2, humidity=37.4, temperature=296.45):
    R = 8.31446  # Universal gas constant

    # Constants for air (mixture of nitrogen, oxygen, and argon)
    m_noa = 0.02897
    c_p_noa = 1.0036
    c_v_noa = 0.7166

    # Constants for carbon dioxide
    m_y = 0.04401
    c_p_y = 0.838
    c_v_y = 0.649

    # Constants for water vapor
    m_h = 0.01801
    c_p_h = 1.863
    c_v_h = 1.403

    x = co2
    y = ((22.4 * 20.5 * (humidity / 100)) / (1000 * 0.018)) / 1000

    M = m_noa * (1 - y - x) + m_y * y + m_h * x

    gama = (m_noa * c_p_noa * (1 - y - x) + m_y * c_p_y * y + m_h * c_p_h * x) / (
            m_noa * c_v_noa * (1 - y - x) + m_y * c_v_y * y + m_h * c_v_h * x)

    soundSpeed = ((gama * R * temperature) / M) ** 0.5

    return soundSpeed

# Generate data points
co2_values = np.arange(0.0003, 0.0501, 0.0001)
sound_speed_values = np.array([speedOfSoundCO2(co2) for co2 in co2_values])

# Reverse the order of sound speed values

# Perform linear regression
slope, intercept = np.polyfit(co2_values, sound_speed_values[::-1], 1)

# Plotting
plt.plot(co2_values, sound_speed_values[::-1], label='Speed of Sound')
plt.xlabel('CO2 Concentration')
plt.ylabel('Speed of Sound')
plt.title('Speed of Sound vs CO2 Concentration')
plt.legend()

# Print the slope
print("Slope of the linear regression line:", slope)

plt.show()
