class LinearRegression:
  def __init__(self):
    self.b1 = 0
    self.b0 = 0
    
  def fit(self, data_X, data_y):
    x_mean = np.mean(data_X)
    y_mean = np.mean(data_y)
    numerator = 0
    denominator = 0
    for i in range(len(data_y)):
      numerator = numerator + (data_X[i] - x_mean)*(data_y[i] - y_mean)
      denominator = denominator + (data_X[i] - x_mean)**2
    self.b1 = numerator/denominator
    self.b0 = y_mean - (self.b1 * x_mean)

  def predict(self, data_x):
    y_predicted = []
    for x in data_x:
      y_predicted.append((x * self.b1) + self.b0)
    y_predicted = np.asarray(y_predicted)
    y_predicted = y_predicted.reshape(1, len(y_predicted))
    y_predicted = y_predicted.flatten()
    return y_predicted

  def getCoeff():
    return b1
  
  def getConst():
    return b0
