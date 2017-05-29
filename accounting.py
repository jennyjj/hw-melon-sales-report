
def tallies(file_):

    file_ = open(file_)
    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

    for line in file_:
        line.rstrip()
        data = line.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count

    return melon_tallies    

    f.close()

def revenue(tally):

    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0

    for melon_type in tally:
        price = melon_prices[melon_type]
        revenue = price * tally[melon_type]
        total_revenue += revenue
    # print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
        print "We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(tally[melon_type], melon_type, price, total_revenue)

def sales_report(file_):
    file_ = open(file_)
    sales = [0, 0]

    for line in file_:
        data = line.split("|")
        if data[1] == "0":
            sales[0] += float(data[3])
        else:
            sales[1] += float(data[3])
    
    print "Salespeople generated ${:.2f} in revenue.".format(sales[1])
    print "Internet sales generated ${:.2f} in revenue.".format(sales[0])

    if sales[1] > sales[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"

tally = tallies("orders-by-type.txt")
revenue(tally)
print 
sales_report("orders-with-sales.txt")