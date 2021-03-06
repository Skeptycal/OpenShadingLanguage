#!/usr/bin/env python

command = oslc("../common/shaders/testnoise.osl")
command += testshade ("-g 512 512 -od uint8 -o Cout out.tif -param noisename perlin testnoise")
command += testshade ("-g 512 512 -od uint8 -o Cout uout.tif -param noisename uperlin -param offset 0.0 -param scale 1.0 testnoise")
outputs = [ "out.txt", "out.tif", "uout.tif" ]
# expect some LSB failures on this test
failthresh = 0.004
failpercent = 0.05
