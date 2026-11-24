class Seller:
    sellerData = [
        {"id": "sh1", "name": "Alice", "contact": 9876543210, "location": "Hosur"},
        {"id": "sh2", "name": "Jame", "contact": 9876543320,  "location": "Krishnagiri"},
        {"id": "sh3", "name": "priya","contact" :8965231478, "location": "uthangarai"},
        {"id": "sh4", "name": "velu", "contact" :8974561234, "location":"palani"},
        {"id":"sh5" ,"name": "ktk","contact":8974561230,"location":"assam"},
    ]

    def __init__(self):
        self.sellers = {}

    def showSellerList(self):
        return self.sellerData

    def getSeller(self):
        newData = {}
        newData["name"] = input('sellerName :')
        newData["contact"]= input('sellercontact :')
        newData["location"] = input('sellerlocation :')

        self.setSeller(newData)

    def setSeller(self, data):
        self.sellerData.append(data)
        print("seller data added successfully")
    
    


        
