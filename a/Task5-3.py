import a.var

var1 = a.var.var(1, 3, 5, 7, 9, 11, 13)
print(var1)

from a.var import var

var2 = var(5, 6, 7, 8, 9)
print(var2)

from a.var import var as fc
var3 = fc(1, 2, 3, 4, 5, 6)