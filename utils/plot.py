import matplotlib.pyplot as plt

class Plot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        
    def add(self, x_values, y_values):
        self.ax.plot(x_values, y_values)
    
    def plot(self):
        plt.show()