# generate human-readable id (HRID)
import uuid

def hrid(id, sym_num=4):
    if isinstance(id, basestring):
        try:
            id = uuid.UUID(id)
        except:
            """
             Passed ID is not a hex-string 
            """
            return id
    hrid_number = id.int % 26**sym_num
    inds = []
    leftover = hrid_number
    for _ in range(sym_num):
        inds.append( leftover % 26 )
        leftover = (leftover - inds[-1]) /26
    return "".join([unichr(65 + ind) for ind in inds])

myid = uuid.uuid4()
print 'ID is:   ', str(myid)
print 'HRID is: ', hrid(str(myid))
