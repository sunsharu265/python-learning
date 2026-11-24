class Customer
    def customerData[
        {"id" :"cu1","name": "ktk","contact:1236549870","location":"ooty" }
        {"id" :"cu1","name": "sankar","contact:1236549870","location":"england" }
        {"id" :"cu1","name": "divya","contact:1236549870","location":"paris" }
        {"id" :"cu1","name": "manjula","contact:1236549870","location":"africa" }
        {"id" :"cu1","name": "priya","contact:1236549870","location":"america" }

    def showCustomerList(self):
        return self.customer()
    
        def getcustomer(self):
            newData = {}
            newData["name"] = input('sellerName :')
            newData["contact"]= input('sellercontact :')
            newData["location"] = input('sellerlocation :')
    
            self.setcustomer(newData)
    
        def setSeller(self, data):
            self.customerData.append(data)
            print("seller data added successfully")
                
    ]
