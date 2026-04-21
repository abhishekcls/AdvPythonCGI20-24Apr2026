#Consumer
def writeDB():
    print("DB conn Open")
    try:
        while True:
            record=yield
            print(f"[DB] consumer save record {record}")
    except GeneratorExit:
        print("DB conn close")

#Producer
def data_scraper(consumer):
    fake_data=["Abhishek","Prabhu","Sudeep"]

    for item in fake_data:
        print(f"[Scraper] producer found data: {item}")
        #send data to waiting consumer
        consumer.send(item)

cons=writeDB()
next(cons) # Prime it

data_scraper(cons)

cons.close() #safely closing the consumer