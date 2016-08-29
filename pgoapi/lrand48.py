



class lrand48:
        a=long(0x5DEECE66D)
        c=long(0xB)
        seedval=long(0x330E)
        BITMASK=0xFFFFFFFFFFFF
	
	def __init__(self):
                self.x=long(0)
        
        def seed(self,xx):
                self.x=((xx&0xFFFFFFFF)<<16|lrand48.seedval)&lrand48.BITMASK#this is by design
        def next(self):
                self.x=self.x*lrand48.a+lrand48.c #this is by design
                self.x=self.x&lrand48.BITMASK
                return self.x
        def next_as_32(self):
                r=self.next()
                #I am going to bite whoever came up with this and 
                #now I want my 6 hours back:
                res= ((r>>32)&0xFFFF)<<15 |((r>>16)&0xFFFF)>>1
                return res


if __name__ == '__main__':
        r=lrand48()
        r.seed(4)
        print(format(r.next_as_32(),"02x"))
        print(format(r.next_as_32(),"02x"))
