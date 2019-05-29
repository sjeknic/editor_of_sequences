def complement(seq):
	lower = seq.lower()
	lower = lower.replace('a', 'T')
	lower = lower.replace('t', 'A')
	lower = lower.replace('c', 'G')
	lower = lower.replace('g', 'C')
	lower = lower.replace('n', 'N')

	return lower

def reverse(seq):
	return seq[::-1]

def import_seq(file='sequence.txt'):
	with open(file, 'r') as f:
		sequence = f.read()
		return sequence.strip()
