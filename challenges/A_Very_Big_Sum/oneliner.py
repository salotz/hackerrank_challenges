# trying not to use the obvious solution which is just to sum the
# values because python handles big integers well

def aVeryBigSum(ar):
  return \
  int(str(
      list(it.accumulate(reversed([str(d) for d in [sum(pair) for pair in it.zip_longest(*[[q for q in [0] + list(g)[0]] if not k%2 else [r for r in list(g)[1]] 
         for k, g in enumerate(it.tee([[v for i, v in enumerate(divs) if i%2] if j%2 else 
         [v for i, v in enumerate(divs) if not i%2] 
              for j, divs in enumerate(
                  it.tee(it.chain(
                              *[(s // 10, s % 10) for s in 
                              [sum(column) for column in 
                                  zip(*[reversed(
                                          [int(digit) for digit in ('{%s}' % ':0<{}'.format(max([len(str(num)) for num in ar]))).format(a)])
                                           for a in ar])]])))]))    
                                          ], fillvalue=0)]]))
           )[-1]
           ))
