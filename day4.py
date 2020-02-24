print ("Marry had a little lamb.")

print("its fleece was white as %s." % 'snow' )

print ("And everywhere that Mart went")

print ("." *10) # what'd that do?

formatter = "%r %r %r %r"
print (formatter % (1,2,3,4,))
print (formatter % ("one", "two","three","four"))
print (formatter % (True,False,False,True))
print formatter % (formatter, formatter, formatter, formatter)
