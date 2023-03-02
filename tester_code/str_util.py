import textwrap

def textWrapped(text, maxColumn):         #maxColumn can be fetched from Adafruit_Thermal.py (it is 32)
	textWrapped = textwrap.wrap(text, width=maxColumn)
	for i in range(len(textWrapped)):
		textWrapped[i]+='\n'

	textWrappedReversed = textWrapped[::-1]
	stringForPrinter = ''.join(list(textWrappedReversed))
	return stringForPrinter
