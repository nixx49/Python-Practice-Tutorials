browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
# we can use append function to add values to list
print(browsing_session)
last = browsing_session.pop()
# we can use pop function to remove data from list
print(last)
print(browsing_session)
print("redirect", browsing_session[-2])
# using miners value we can get previous history

print(browsing_session)


if not browsing_session:
    browsing_session[-1]
#     print("disable")
# else:
#     print("enable")
