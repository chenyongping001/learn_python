# import pizza
# pizza.make_pizza(16,'pepperoni')
# pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

# from pizza import  make_pizza as mp
# mp(16,'pepperoni')
# mp(12,'mushrooms','green peppers','extra cheese')

# from pizza import *
# 一般不建议这种方法，有可能导致导入的函数名与现有的重复

import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')

