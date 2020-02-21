from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sqlite3
from sqlite3 import Error
 




driver = webdriver.Firefox()




driver.get("https://www.booking.com/searchresults.en-us.html?label=gen173nr-1FCAEoggI46AdIM1gEaEaIAQGYATG4ARnIAQ_YAQHoAQH4AQKIAgGoAgO4ApvVr-8FwAIB&sid=be5d3ab434f12c34de37e0b0c0d3aa6e&tmpl=searchresults&class_interval=1&dest_id=197&dest_type=country&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&order=price&raw_dest_type=country&room1=A%2CA&sb_price_type=total&shw_aparth=1&slp_r_match=0&src=index&srpvid=3628813b27070142&ss=espa%C3%B1a&ssb=empty&top_ufis=1&track_hp_back_button=1&nflt=class%3D4%3Bclass%3D5%3Bht_id%3D204%3B&percent_htype_hotel=1&rsf=")


timeout = 3
try:
    element_present = EC.presence_of_element_located((By.ID, 'main'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")
    but4 = driver.find_element_by_css_selector(".c2-day-s-today")
    but4.click()

timeout = 1
try:
    element_present = EC.presence_of_element_located((By.ID, 'main'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")
    but5 = driver.find_element_by_css_selector(".-submit-button button")
    but5.click()



timeout = 10

element_present = EC.presence_of_element_located((By.ID, 'search_results_table'))
WebDriverWait(driver, timeout).until(element_present)

hotels = driver.find_elements_by_xpath("//div[@data-hotelid]")

for tit in hotels:
	#print(tit.text+	"\n")
	hotelid = tit.get_attribute("data-hotelid")
	hotelname = tit.find_element_by_class_name('sr-hotel__name').text
	roomdetails = tit.find_element_by_class_name('room_details ')
	
	try:
		price = roomdetails.find_elements_by_class_name('prco-ltr-right-align-helper')[1]
		precio = price.text

		# getting numbers from string  
		hprice = [int(i) for i in precio.split() if i.isdigit()]
		hotelprice = str(hprice[0]) 

	except IndexError:
		hotelprice = "unkown"

	def sql_connection():
		try:
			con = sqlite3.connect('booky.db')
			return con
		except Error:
			print(Error)

	def sql_table(con):
		cursorObj = con.cursor()
		sentencia= "INSERT INTO hoteles (hotelid, name) VALUES("+hotelid+",'"+ hotelname+"')"
		cursorObj.execute(sentencia) 
		con.commit()
 
	con = sql_connection()
 
	sql_table(con)

	


	print ("HOTEL:"+hotelid +","+hotelname+","+hotelprice)
	print("\n")








#driver.close()


