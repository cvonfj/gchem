#! /usr/bin/env python
# coding: utf-8

# Python Script Collection for GEOS-Chem Chemistry Transport Model (gchem)
# Copyright (C) 2012 Gerrit Kuhlmann
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""
This module contains (some) grid coordinates used with GEOS-Chem as numpy
arrays

Grid box longitude and latitude [degrees] for 2°x2.5° resolution:
    c_lon_2x25          center
    e_lon_2x25          edges
    c_lat_2x25          center
    e_lat_2x25          edges

Grid box longitude and latitude [degrees] for a 4°x5° resolution:
    c_lon_4x5           center
    e_lon_4x5           edges
    c_lat_4x5           center
    e_lat_4x5           edges

Grid box longitude and latitude [degrees] for a 0.5°x0.667° resolution for
China:
    c_lon_05x0667_CH    center
    e_lon_05x0667_CH    edges
    c_lat_05x0667_CH    center
    e_lat_05x0667_CH    edges

Generic grid longitudes and latitudes [degrees]:
    c_lon_generic       center
    e_lon_generic       edges
    c_lat_generic       center
    e_lat_generic       edges

Reduced GEOS 5 grid box level edges:
    e_eta_geos5_r       eta coordinate [1]
    e_km_geos5_r        altitude in km
    e_hPa_geos5_r       pressure in hPa

Reduced GEOS 5 grid box level centers:
    c_eta_geos5_r       eta coordinate¹
    c_km_geos5_r        altitude in km
    c_hPa_geos5_r       pressure in hPa


[1] eta = (p - p_TOA) / (p_S - p_TOA), S: surface, TOA: top of atmosphere

"""

import numpy

c_lon_4x5 = numpy.array(
      [-180., -175., -170., -165., -160., -155., -150., -145., -140.,
       -135., -130., -125., -120., -115., -110., -105., -100.,  -95.,
        -90.,  -85.,  -80.,  -75.,  -70.,  -65.,  -60.,  -55.,  -50.,
        -45.,  -40.,  -35.,  -30.,  -25.,  -20.,  -15.,  -10.,   -5.,
          0.,    5.,   10.,   15.,   20.,   25.,   30.,   35.,   40.,
         45.,   50.,   55.,   60.,   65.,   70.,   75.,   80.,   85.,
         90.,   95.,  100.,  105.,  110.,  115.,  120.,  125.,  130.,
        135.,  140.,  145.,  150.,  155.,  160.,  165.,  170.,  175.])

e_lon_4x5 = numpy.array(
      [-182.5, -177.5, -172.5, -167.5, -162.5, -157.5, -152.5, -147.5,
       -142.5, -137.5, -132.5, -127.5, -122.5, -117.5, -112.5, -107.5,
       -102.5,  -97.5,  -92.5,  -87.5,  -82.5,  -77.5,  -72.5,  -67.5,
        -62.5,  -57.5,  -52.5,  -47.5,  -42.5,  -37.5,  -32.5,  -27.5,
        -22.5,  -17.5,  -12.5,   -7.5,   -2.5,    2.5,    7.5,   12.5,
         17.5,   22.5,   27.5,   32.5,   37.5,   42.5,   47.5,   52.5,
         57.5,   62.5,   67.5,   72.5,   77.5,   82.5,   87.5,   92.5,
         97.5,  102.5,  107.5,  112.5,  117.5,  122.5,  127.5,  132.5,
        137.5,  142.5,  147.5,  152.5,  157.5,  162.5,  167.5,  172.5,
        177.5])

c_lat_4x5 = numpy.array(
      [-89., -86., -82., -78., -74., -70., -66., -62., -58., -54., -50.,
       -46., -42., -38., -34., -30., -26., -22., -18., -14., -10.,  -6.,
        -2.,   2.,   6.,  10.,  14.,  18.,  22.,  26.,  30.,  34.,  38.,
        42.,  46.,  50.,  54.,  58.,  62.,  66.,  70.,  74.,  78.,  82.,
        86.,  89.])

e_lat_4x5 = numpy.array(
      [-90., -88., -84., -80., -76., -72., -68., -64., -60., -56., -52.,
       -48., -44., -40., -36., -32., -28., -24., -20., -16., -12.,  -8.,
        -4.,   0.,   4.,   8.,  12.,  16.,  20.,  24.,  28.,  32.,  36.,
        40.,  44.,  48.,  52.,  56.,  60.,  64.,  68.,  72.,  76.,  80.,
        84.,  88.,  90.])

e_lon_2x25 = numpy.array(
      [-181.25, -178.75, -176.25, -173.75, -171.25, -168.75, -166.25,
       -163.75, -161.25, -158.75, -156.25, -153.75, -151.25, -148.75,
       -146.25, -143.75, -141.25, -138.75, -136.25, -133.75, -131.25,
       -128.75, -126.25, -123.75, -121.25, -118.75, -116.25, -113.75,
       -111.25, -108.75, -106.25, -103.75, -101.25,  -98.75,  -96.25,
        -93.75,  -91.25,  -88.75,  -86.25,  -83.75,  -81.25,  -78.75,
        -76.25,  -73.75,  -71.25,  -68.75,  -66.25,  -63.75,  -61.25,
        -58.75,  -56.25,  -53.75,  -51.25,  -48.75,  -46.25,  -43.75,
        -41.25,  -38.75,  -36.25,  -33.75,  -31.25,  -28.75,  -26.25,
        -23.75,  -21.25,  -18.75,  -16.25,  -13.75,  -11.25,   -8.75,
         -6.25,   -3.75,   -1.25,    1.25,    3.75,    6.25,    8.75,
         11.25,   13.75,   16.25,   18.75,   21.25,   23.75,   26.25,
         28.75,   31.25,   33.75,   36.25,   38.75,   41.25,   43.75,
         46.25,   48.75,   51.25,   53.75,   56.25,   58.75,   61.25,
         63.75,   66.25,   68.75,   71.25,   73.75,   76.25,   78.75,
         81.25,   83.75,   86.25,   88.75,   91.25,   93.75,   96.25,
         98.75,  101.25,  103.75,  106.25,  108.75,  111.25,  113.75,
        116.25,  118.75,  121.25,  123.75,  126.25,  128.75,  131.25,
        133.75,  136.25,  138.75,  141.25,  143.75,  146.25,  148.75,
        151.25,  153.75,  156.25,  158.75,  161.25,  163.75,  166.25,
        168.75,  171.25,  173.75,  176.25,  178.75])

c_lon_2x25 = numpy.array(
      [-180. , -177.5, -175. , -172.5, -170. , -167.5, -165. , -162.5,
       -160. , -157.5, -155. , -152.5, -150. , -147.5, -145. , -142.5,
       -140. , -137.5, -135. , -132.5, -130. , -127.5, -125. , -122.5,
       -120. , -117.5, -115. , -112.5, -110. , -107.5, -105. , -102.5,
       -100. ,  -97.5,  -95. ,  -92.5,  -90. ,  -87.5,  -85. ,  -82.5,
        -80. ,  -77.5,  -75. ,  -72.5,  -70. ,  -67.5,  -65. ,  -62.5,
        -60. ,  -57.5,  -55. ,  -52.5,  -50. ,  -47.5,  -45. ,  -42.5,
        -40. ,  -37.5,  -35. ,  -32.5,  -30. ,  -27.5,  -25. ,  -22.5,
        -20. ,  -17.5,  -15. ,  -12.5,  -10. ,   -7.5,   -5. ,   -2.5,
          0. ,    2.5,    5. ,    7.5,   10. ,   12.5,   15. ,   17.5,
         20. ,   22.5,   25. ,   27.5,   30. ,   32.5,   35. ,   37.5,
         40. ,   42.5,   45. ,   47.5,   50. ,   52.5,   55. ,   57.5,
         60. ,   62.5,   65. ,   67.5,   70. ,   72.5,   75. ,   77.5,
         80. ,   82.5,   85. ,   87.5,   90. ,   92.5,   95. ,   97.5,
        100. ,  102.5,  105. ,  107.5,  110. ,  112.5,  115. ,  117.5,
        120. ,  122.5,  125. ,  127.5,  130. ,  132.5,  135. ,  137.5,
        140. ,  142.5,  145. ,  147.5,  150. ,  152.5,  155. ,  157.5,
        160. ,  162.5,  165. ,  167.5,  170. ,  172.5,  175. ,  177.5])

e_lat_2x25 = numpy.array(
      [-90., -89., -87., -85., -83., -81., -79., -77., -75., -73., -71.,
       -69., -67., -65., -63., -61., -59., -57., -55., -53., -51., -49.,
       -47., -45., -43., -41., -39., -37., -35., -33., -31., -29., -27.,
       -25., -23., -21., -19., -17., -15., -13., -11.,  -9.,  -7.,  -5.,
        -3.,  -1.,   1.,   3.,   5.,   7.,   9.,  11.,  13.,  15.,  17.,
        19.,  21.,  23.,  25.,  27.,  29.,  31.,  33.,  35.,  37.,  39.,
        41.,  43.,  45.,  47.,  49.,  51.,  53.,  55.,  57.,  59.,  61.,
        63.,  65.,  67.,  69.,  71.,  73.,  75.,  77.,  79.,  81.,  83.,
        85.,  87.,  89.,  90.])


c_lat_2x25 = numpy.array(
      [-89.5, -88. , -86. , -84. , -82. , -80. , -78. , -76. , -74. ,
       -72. , -70. , -68. , -66. , -64. , -62. , -60. , -58. , -56. ,
       -54. , -52. , -50. , -48. , -46. , -44. , -42. , -40. , -38. ,
       -36. , -34. , -32. , -30. , -28. , -26. , -24. , -22. , -20. ,
       -18. , -16. , -14. , -12. , -10. ,  -8. ,  -6. ,  -4. ,  -2. ,
         0. ,   2. ,   4. ,   6. ,   8. ,  10. ,  12. ,  14. ,  16. ,
        18. ,  20. ,  22. ,  24. ,  26. ,  28. ,  30. ,  32. ,  34. ,
        36. ,  38. ,  40. ,  42. ,  44. ,  46. ,  48. ,  50. ,  52. ,
        54. ,  56. ,  58. ,  60. ,  62. ,  64. ,  66. ,  68. ,  70. ,
        72. ,  74. ,  76. ,  78. ,  80. ,  82. ,  84. ,  86. ,  88. ,
        89.5])

c_lon_05x0667_CH = numpy.array([
         70.   ,   70.667,   71.333,   72.   ,   72.667,   73.333,
         74.   ,   74.667,   75.333,   76.   ,   76.667,   77.333,
         78.   ,   78.667,   79.333,   80.   ,   80.667,   81.333,
         82.   ,   82.667,   83.333,   84.   ,   84.667,   85.333,
         86.   ,   86.667,   87.333,   88.   ,   88.667,   89.333,
         90.   ,   90.667,   91.333,   92.   ,   92.667,   93.333,
         94.   ,   94.667,   95.333,   96.   ,   96.667,   97.333,
         98.   ,   98.667,   99.333,  100.   ,  100.667,  101.333,
        102.   ,  102.667,  103.333,  104.   ,  104.667,  105.333,
        106.   ,  106.667,  107.333,  108.   ,  108.667,  109.333,
        110.   ,  110.667,  111.333,  112.   ,  112.667,  113.333,
        114.   ,  114.667,  115.333,  116.   ,  116.667,  117.333,
        118.   ,  118.667,  119.333,  120.   ,  120.667,  121.333,
        122.   ,  122.667,  123.333,  124.   ,  124.667,  125.333,
        126.   ,  126.667,  127.333,  128.   ,  128.667,  129.333,
        130.   ,  130.667,  131.333,  132.   ,  132.667,  133.333,
        134.   ,  134.667,  135.333,  136.   ,  136.667,  137.333,
        138.   ,  138.667,  139.333,  140.   ,  140.667,  141.333,
        142.   ,  142.667,  143.333,  144.   ,  144.667,  145.333,
        146.   ,  146.667,  147.333,  148.   ,  148.667,  149.333,  150.   ])

c_lat_05x0667_CH = numpy.array([
   -11. , -10.5, -10. ,  -9.5,  -9. ,  -8.5,  -8. ,  -7.5,  -7. ,
    -6.5,  -6. ,  -5.5,  -5. ,  -4.5,  -4. ,  -3.5,  -3. ,  -2.5,
    -2. ,  -1.5,  -1. ,  -0.5,   0. ,   0.5,   1. ,   1.5,   2. ,
     2.5,   3. ,   3.5,   4. ,   4.5,   5. ,   5.5,   6. ,   6.5,
     7. ,   7.5,   8. ,   8.5,   9. ,   9.5,  10. ,  10.5,  11. ,
    11.5,  12. ,  12.5,  13. ,  13.5,  14. ,  14.5,  15. ,  15.5,
    16. ,  16.5,  17. ,  17.5,  18. ,  18.5,  19. ,  19.5,  20. ,
    20.5,  21. ,  21.5,  22. ,  22.5,  23. ,  23.5,  24. ,  24.5,
    25. ,  25.5,  26. ,  26.5,  27. ,  27.5,  28. ,  28.5,  29. ,
    29.5,  30. ,  30.5,  31. ,  31.5,  32. ,  32.5,  33. ,  33.5,
    34. ,  34.5,  35. ,  35.5,  36. ,  36.5,  37. ,  37.5,  38. ,
    38.5,  39. ,  39.5,  40. ,  40.5,  41. ,  41.5,  42. ,  42.5,
    43. ,  43.5,  44. ,  44.5,  45. ,  45.5,  46. ,  46.5,  47. ,
    47.5,  48. ,  48.5,  49. ,  49.5,  50. ,  50.5,  51. ,  51.5,
    52. ,  52.5,  53. ,  53.5,  54. ,  54.5,  55. ])

e_lon_generic = numpy.arange(-180.0,181.0)
c_lon_generic = numpy.arange(-179.5,180.0)
e_lat_generic = numpy.arange(-90.0,91.0)
c_lat_generic = numpy.arange(-89.5,90.0)


#Grid box level edges (eta coordinate):
e_eta_geos5_r = numpy.array([
         1.00179600e+00,   9.86769000e-01,   9.71665000e-01,
         9.56562000e-01,   9.41459000e-01,   9.26356000e-01,
         9.11253000e-01,   8.96152000e-01,   8.81051000e-01,
         8.65949000e-01,   8.50848000e-01,   8.35748000e-01,
         8.20648000e-01,   8.00515000e-01,   7.75350000e-01,
         7.50186000e-01,   7.25026000e-01,   6.99867000e-01,
         6.74708000e-01,   6.36974000e-01,   5.99251000e-01,
         5.61527000e-01,   5.23819000e-01,   4.86118000e-01,
         4.48431000e-01,   4.10759000e-01,   3.73114000e-01,
         3.35486000e-01,   2.85974000e-01,   2.42774000e-01,
         2.06167000e-01,   1.75170000e-01,   1.48896000e-01,
         1.26563000e-01,   1.07578000e-01,   9.14420000e-02,
         7.77260000e-02,   5.58200000e-02,   3.97680000e-02,
         2.80770000e-02,   1.95860000e-02,   9.19100000e-03,
         4.02600000e-03,   1.62500000e-03,   6.01000000e-04,
         1.99000000e-04,   5.50000000e-05,   0.00000000e+00])

#Grid box level edges [km]:
e_km_geos5_r = numpy.array([
         6.00000000e-03,   1.35000000e-01,   2.66000000e-01,
         3.99000000e-01,   5.33000000e-01,   6.69000000e-01,
         8.06000000e-01,   9.45000000e-01,   1.08600000e+00,
         1.22900000e+00,   1.37400000e+00,   1.52000000e+00,
         1.66900000e+00,   1.87100000e+00,   2.12800000e+00,
         2.39200000e+00,   2.66300000e+00,   2.94100000e+00,
         3.22800000e+00,   3.67300000e+00,   4.14000000e+00,
         4.63100000e+00,   5.14900000e+00,   5.69800000e+00,
         6.28300000e+00,   6.91000000e+00,   7.58700000e+00,
         8.32400000e+00,   9.41100000e+00,   1.05050000e+01,
         1.15780000e+01,   1.26330000e+01,   1.36740000e+01,
         1.47060000e+01,   1.57310000e+01,   1.67530000e+01,
         1.77730000e+01,   1.98550000e+01,   2.20040000e+01,
         2.42400000e+01,   2.65960000e+01,   3.17160000e+01,
         3.75740000e+01,   4.42860000e+01,   5.17880000e+01,
         5.99260000e+01,   6.83920000e+01,   8.05810000e+01])

#Grid box level edges [hPa]:
e_hPa_geos5_r = numpy.array([
         1.01181400e+03,   9.96636000e+02,   9.81382000e+02,
         9.66128000e+02,   9.50874000e+02,   9.35621000e+02,
         9.20367000e+02,   9.05114000e+02,   8.89862000e+02,
         8.74610000e+02,   8.59358000e+02,   8.44107000e+02,
         8.28856000e+02,   8.08522000e+02,   7.83106000e+02,
         7.57690000e+02,   7.32279000e+02,   7.06869000e+02,
         6.81458000e+02,   6.43348000e+02,   6.05247000e+02,
         5.67147000e+02,   5.29062000e+02,   4.90984000e+02,
         4.52921000e+02,   4.14873000e+02,   3.76851000e+02,
         3.38848000e+02,   2.88841000e+02,   2.45210000e+02,
         2.08236000e+02,   1.76930000e+02,   1.50393000e+02,
         1.27837000e+02,   1.08663000e+02,   9.23660000e+01,
         7.85120000e+01,   5.63880000e+01,   4.01750000e+01,
         2.83680000e+01,   1.97920000e+01,   9.29300000e+00,
         4.07700000e+00,   1.65100000e+00,   6.17000000e-01,
         2.11000000e-01,   6.60000000e-02,   1.00000000e-02])

#Grid box level centers (eta-coordinates)
c_eta_geos5_r = numpy.array([
         9.94283000e-01,   9.79217000e-01,   9.64113000e-01,
         9.49010000e-01,   9.33908000e-01,   9.18805000e-01,
         9.03703000e-01,   8.88601000e-01,   8.73500000e-01,
         8.58399000e-01,   8.43298000e-01,   8.28198000e-01,
         8.10582000e-01,   7.87933000e-01,   7.62768000e-01,
         7.37606000e-01,   7.12447000e-01,   6.87287000e-01,
         6.55841000e-01,   6.18113000e-01,   5.80389000e-01,
         5.42673000e-01,   5.04968000e-01,   4.67274000e-01,
         4.29595000e-01,   3.91937000e-01,   3.54300000e-01,
         3.10730000e-01,   2.64374000e-01,   2.24471000e-01,
         1.90668000e-01,   1.62033000e-01,   1.37729000e-01,
         1.17070000e-01,   9.95100000e-02,   8.45840000e-02,
         6.67730000e-02,   4.77940000e-02,   3.39230000e-02,
         2.38320000e-02,   1.43890000e-02,   6.60900000e-03,
         2.82500000e-03,   1.11300000e-03,   4.00000000e-04,
         1.27000000e-04,   2.80000000e-05])

#Grid box level centers [km]
c_km_geos5_r = numpy.array([
         7.10000000e-02,   2.01000000e-01,   3.32000000e-01,
         4.66000000e-01,   6.01000000e-01,   7.37000000e-01,
         8.75000000e-01,   1.01600000e+00,   1.15700000e+00,
         1.30100000e+00,   1.44700000e+00,   1.59400000e+00,
         1.76900000e+00,   1.99900000e+00,   2.25900000e+00,
         2.52700000e+00,   2.80100000e+00,   3.08400000e+00,
         3.44800000e+00,   3.90400000e+00,   4.38200000e+00,
         4.88600000e+00,   5.41900000e+00,   5.98500000e+00,
         6.59100000e+00,   7.24100000e+00,   7.94700000e+00,
         8.84800000e+00,   9.93800000e+00,   1.10210000e+01,
         1.20860000e+01,   1.31340000e+01,   1.41700000e+01,
         1.51980000e+01,   1.62220000e+01,   1.72430000e+01,
         1.87270000e+01,   2.08360000e+01,   2.30200000e+01,
         2.53070000e+01,   2.86540000e+01,   3.40240000e+01,
         4.01660000e+01,   4.71350000e+01,   5.48340000e+01,
         6.30540000e+01,   7.21800000e+01])

#Grid box level centers [hPa]
c_hPa_geos5_r = numpy.array([
         1.00422500e+03,   9.89009000e+02,   9.73755000e+02,
         9.58501000e+02,   9.43247000e+02,   9.27994000e+02,
         9.12741000e+02,   8.97488000e+02,   8.82236000e+02,
         8.66984000e+02,   8.51732000e+02,   8.36481000e+02,
         8.18689000e+02,   7.95814000e+02,   7.70398000e+02,
         7.44984000e+02,   7.19574000e+02,   6.94163000e+02,
         6.62403000e+02,   6.24298000e+02,   5.86197000e+02,
         5.48105000e+02,   5.10023000e+02,   4.71952000e+02,
         4.33897000e+02,   3.95862000e+02,   3.57850000e+02,
         3.13844000e+02,   2.67025000e+02,   2.26723000e+02,
         1.92583000e+02,   1.63661000e+02,   1.39115000e+02,
         1.18250000e+02,   1.00514000e+02,   8.54390000e+01,
         6.74500000e+01,   4.82820000e+01,   3.42720000e+01,
         2.40800000e+01,   1.45420000e+01,   6.68500000e+00,
         2.86400000e+00,   1.13400000e+00,   4.14000000e-01,
         1.39000000e-01,   3.80000000e-02])

