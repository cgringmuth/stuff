#!/usr/bin/env python

# This script renders Bezier curvse. todo
# cf. http://en.wikipedia.org/wiki/B%C3%A9zier_curve

import numpy as np
from numpy import (array,)
import matplotlib.pyplot as plt

def binterpolate(t, p):
  if len(p) == 1:
    return p[0]
  elif len(p) < 1:
    print "Error happend"
  else:
    return (1-t) * binterpolate(t, p[:-1]) + t * binterpolate(t, p[1:])

def bezier_rec(p, samples=None):
  """calculates bezier curve of n control proints"""
  if samples is None:
    samples = 100
  t = np.linspace(0, 1, samples)
  ret = np.zeros((samples, p[0].size))

  for idx, _t in enumerate(t):
    ret[idx] = binterpolate(_t, p)

  return ret


def quat_inter(p1, p2, p3, p4, t):
  h = square_inter(p1, p2, p3, t)
  i = square_inter(p2, p3, p4, t)
  return h + t * (i - h)

def quat_bezier_curve(p1, p2, p3, p4, samples=None):
  """calculates bezier curve of 4 control points"""
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
  d = p1 + t * (p2 - p1)
  e = p2 + t * (p3 - p2)
  return d + t * (e - d)

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

def plot_control_pts(p):
  for idx, _p in enumerate(p):
    plt.plot(_p[0], _p[1], 'ro')
    plt.text(_p[0] + 0.5, _p[1] + 0.5, 'p_%s' % (str(idx+1), ))

  plt.plot([_p[0] for _p in p], [_p[1] for _p in p], '--', color="gray")

def demo_bezier_rec():
  p = [
        array([30,30]),
        array([70,120]),
        array([100,70]),
        array([140,100]),
        array([180,80]),
        array([140,65]),
      ]

  line = bezier_rec(p)
  x, y = line[:,0], line[:,1]
  plt.plot(x, y)
  plot_control_pts(p)
  plt.show()

if __name__ == "__main__":
  demo_bezier_rec()
