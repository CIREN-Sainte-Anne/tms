#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

#input arguments:

if len( sys.argv ) != 4 or sys.argv[1] in ( '-h', '--help' ):
  print 'usage:', sys.argv[0], '<input x coordinate> <input y coordinate> <input z coordinate>'
  print 'A partir des coordonnees dans coordonnees dans Anatomist (dans le nifti genere par MRIConvert)'
  print 'donne les coordonnees dans le repere de neuronav (MRSlices).'
  print 'Exemple: convert_anatomistcoord_in_mrslicescoord.py 104 39 199'
  sys.exit(1)

x_ana,y_ana,z_ana = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

print 'x in MRSlices: '+ str(255 - y_ana)
print 'y in MRSlices: '+ str(x_ana)
print 'z in MRSlices: '+ str(255 - z_ana)
