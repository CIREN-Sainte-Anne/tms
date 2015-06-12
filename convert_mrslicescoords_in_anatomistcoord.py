#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

#input arguments:
if len( sys.argv ) != 4 or sys.argv[1] in ( '-h', '--help' ):
  print 'usage:', sys.argv[0], '<input x coordinate> <input y coordinate> <input z coordinate>'
  print 'A partir des coordonnees dans le repere de neuronav (MRSlices)'
  print 'donne les coordonnees dans Anatomis (dans le nifti genere par MRIConvert)).'
  print 'Exemple: convert_mrslice_in_anatomistcoord.py 107 3 89'
  sys.exit(1)

x_mrs,y_mrs,z_mrs = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

print 'x in anatomist: '+ str(y_mrs)
print 'y in anatomist: '+ str(255 - x_mrs)
print 'z in anatomist: '+ str(255 - z_mrs)
