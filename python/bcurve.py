#!/usr/bin/env python

# This script renders Bezier curvse. todo

import numpy as np

def quat_inter(p1, p2, p3, p4, t):
  h = square_inter(p1, p2, p3, t)
  i = square_inter(p2, p3, p4, t)
  return h + t * (i - h)

def quat_bezier_curve(p1, p2, p3, p4, samples=None):
  if samples is None:
    samples = 100
  t = np.linspace(0, 1, samples)
  p1 = np.asarray(p1).flatten()
  p2 = np.asarray(p2).flatten()
  p3 = np.asarray(p3).flatten()
  p4 = np.asarray(p4).flatten()
  ret = np.zeros((samples, p1.size))

  for idx, _t in enumerate(t):
    ret[idx] = quat_inter(p1, p2, p3, p4, _t)
  return ret

def square_inter(p1, p2, p3, t):
  p4 = p1 + t * (p2 - p1)
  e = p2 + t * (p3 - p2)
  return p4 + t * (e - p4)

def square_bezier_curve(p1, p2, p3, samples=None):
  if samples is None:
    samples = 100
  t = np.linspace(0, 1, samples)
  p1 = np.asarray(p1).flatten()
  p2 = np.asarray(p2).flatten()
  p3 = np.asarray(p3).flatten()
  ret = np.zeros((samples, p1.size))

  for idx, _t in enumerate(t):
    ret[idx] = square_inter(p1, p2, p3, _t)

  return ret

def demo_square_inter():
  import matplotlib.pyplot as plt
  p1 = np.array([10,10])
  p2 = np.array([120,50])
  p3 = np.array([100,20])

  line = square_bezier_curve(p1,p2,p3,50)
  x, y = line[:,0], line[:,1]
  plt.plot(x, y)
  plt.plot(p1[0], p1[1], 'ro')
  plt.text(p1[0] + 0.5, p1[1] + 0.5, 'p_1')
  plt.plot(p2[0], p2[1], 'bo')
  plt.text(p2[0] + 0.5, p2[1] + 0.5, 'p_2')
  plt.plot(p3[0], p3[1], 'go')
  plt.text(p3[0] + 0.5, p3[1] + 0.5, 'p_3')
  plt.plot([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], '--', color="gray")
  plt.show()

def demo_quat_inter():
  import matplotlib.pyplot as plt
  p1 = np.array([10,10])
  p2 = np.array([0,40])
  p3 = np.array([120,50])
  p4 = np.array([80,60])

  line = quat_bezier_curve(p1, p2,p3, p4, 50)
  x, y = line[:,0], line[:,1]
  plt.plot(x, y)
  plt.plot(p1[0], p1[1], 'ro')
  plt.text(p1[0] + 0.5, p1[1] + 0.5, 'p_1')
  plt.plot(p2[0], p2[1], 'bo')
  plt.text(p2[0] + 0.5, p2[1] + 0.5, 'p_2')
  plt.plot(p3[0], p3[1], 'go')
  plt.text(p3[0] + 0.5, p3[1] + 0.5, 'p_3')
  plt.plot(p4[0], p4[1], 'yo')
  plt.text(p4[0] + 0.5, p4[1] + 0.5, 'p_4')
  plt.plot([p1[0], p2[0], p3[0], p4[0]], [p1[1], p2[1], p3[1], p4[1]], '--', color="gray")
  plt.show()

if __name__ == "__main__":
  demo_quat_inter()
