from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver = webdriver.Firefox()

# driver.get("https://www.booking.com")



# elem = driver.find_element_by_name("ss")
# elem.clear()
# elem.send_keys("españa")
# elem.send_keys(Keys.RETURN)


# timeout = 5
# try:
#     element_present = EC.presence_of_element_located((By.ID, 'main'))
#     WebDriverWait(driver, timeout).until(element_present)
# except TimeoutException:
#     print("Timed out waiting for page to load")
# finally:
#     print("Page loaded")
#     but4 = driver.find_element_by_css_selector(".sort_price a")
#     but4.click()


# timeout = 10
# try:
#     element_present = EC.presence_of_element_located((By.ID, 'filter_class'))
#     WebDriverWait(driver, timeout).until(element_present)
#     but4 = driver.find_element_by_xpath('//a[@data-id="class-4"]')
#     but4.click()
#     but5 = driver.find_element_by_xpath('//a[@data-id="class-5"]')
#     but5.click()
# except TimeoutException:
#     print("Timed out waiting for page to load")
# finally:
#     print("Page loaded")
   





#driver.close()




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


	print ("HOTEL:"+hotelid +","+hotelname+","+hotelprice)
	print("\n")








#driver.close()


