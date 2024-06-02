from matplotlib import pyplot as plt
from matplotlib import dates
from matplotlib.animation import FuncAnimation
import pandas as pd
plt.style.use('ggplot')

# Reading btc price from csv file
def animate(i):
    df = pd.read_csv('dataset/btc price.csv')
    plt.cla()  # Removes the old plot lines
    plt.xticks(rotation=45)  # Rotate labels by 45 degrees
    plt.xlabel('Time')
    plt.ylabel('Price (USD)')
    plt.title('Real-Time BTC Price Plot')
    plt.plot(df['time'], df['price'])

print('Script Running')

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()