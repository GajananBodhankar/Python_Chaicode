seasons=["spring", "Summer", "Rainy", "Winter"]

for index, item in enumerate(seasons):
    print(index, item)
    
def my_enum_yield(limit):
    n=0
    while n < limit:
        yield n
        n+=1

for item in my_enum_yield(4):
    print(item) # used to return number multiple times, so the output is 0,1,2,3
    
# =============================================================================================

list1=["John", "Brock", "Bruice", "Tom", "Max"]
list2=[1,2,3,4,5]

for item in zip(list2, list1):
    print(item)
    
#  walrus operator ============================================================================

# value=13
# remainder=value%2

# if remainder:
#     print("The remainder is ", value)

# with walrus operator
value=13
if(remainder := value % 5):
    print("the remainder is ", remainder)
    
# ==============================================================================================
users=[{"id":1, "total": 100, "coupon": "P20"},{ "id": 2, "total": 250.50,
    "coupon": "SAVE10"
  },
  {
    "id": 3,
    "total": 45,
    "coupon": "SAVE10"
  },
  {
    "id": 4,
    "total": 1200,
    "coupon": "WELCOME_2026"
  },
 
  {
    "id": 5,
    "total": 89.99,
    "coupon": "SUMMER_SALE"
  }]

discounts={"P20": (20, 0), 
           "SAVE10": (10, 0), 
           "WELCOME_2026": (0, 10),
           "SUMMER_SALE": (30, 0)
           }

for user in users:
    percent, fixed=discounts.get(user.get("coupon"))
    user.get("total")
    if percent>0:
        user["total"] = user["total"] - (user["total"]* (percent/100))
print(users)