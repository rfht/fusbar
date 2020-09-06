#!/usr/bin/env python3

import os, sys
import fsb5

if len(sys.argv) < 2:
	print("ERROR: file argument missing")
	sys.exit(1)

args = sys.argv[1:]

print("MAIN")
for x in args:
	if os.path.isfile(x):
		print(x)
	else:
		print("ERROR: note a file - ", x)

	with open(x, 'rb') as f:
		fsb = fsb5.FSB5(f.read())

	print(fsb.header)
	ext = fsb.get_sample_extension()

	# iterate over samples
	for sample in fsb.samples:
		# print sample properties
		print('''\t{sample.name}.{extension}:
			Frequency: {sample.frequency}
			Channels: {sample.channels}
			Samples: {sample.samples}'''.format(sample=sample, extension=ext))

		# rebuild the sample and save
		with open('{0}.{1}'.format(sample.name, ext), 'wb') as f:
			rebuilt_sample = fsb.rebuild_sample(sample)
			f.write(rebuilt_sample)
