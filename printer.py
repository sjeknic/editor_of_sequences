import seq_editor as sq

seq = sq.import_seq()
rev = sq.reverse(seq)
revcomp = sq.complement(rev)

print '\n seq \n', seq
print '\n rev \n', rev
print '\n revcomp \n', revcomp