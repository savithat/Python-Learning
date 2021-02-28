class Emp:
    def __init__(self, eid, ename, esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def display(self):
        print("eid = {}, ename = {}, esal = {}" .format(self.eid, self.ename, self.esal))
        print("eid=%d, ename=%s, esal=%g" %(self.eid, self.ename ,self.esal))

E = Emp(11,"savi",35000)
E.display()