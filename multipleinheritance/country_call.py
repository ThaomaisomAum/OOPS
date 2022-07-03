from country import Country

#สร้าง object country
c1 = Country('Thailand',513120,66.93)
c1.setcordinate(15.8700,100.9925)
c1.setcelsius(31)
c1.show_detail()

#สร้าง object ของประเทศ Norway
c2 = Country('England', 130279, 55268100)
c2.setCordinate(51.5, -0.116667)
c2.setCelsius(9)
c2.showDetails()

c3 = Country('Canada', 9984670, 35151728)
c3.setCordinate(45.4, -75.666667)
c3.setCelsius(-3)
c3.showDetails()
