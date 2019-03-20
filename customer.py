from db import Db


class Customer:
    def __init__(self, first_name, last_name, phone, email,
                 address1, address2, postal_code, city, country,
                 customer_id=None, added_by=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address1 = address1
        self.address2 = address2
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.added_by = added_by

    def save(self):
        
        '''If self has been populated by database data - UPDATE.
        Otherwise - INSERT a new record.'''
        pass


    def build_from_row(row):
        if row is None:
            return None
        customer = Customer(row[0], row[1], row[2], row[3], row[4],
                            row[5], row[6], row[7], row[8], row[9])
        if len(row) >= 11:
            customer.customer_id = row[0]
            customer.added_by = row[10]
        return customer

    # Note: this is a CLASS function (no self!)
    def get(customer_id):
        '''Get a single Customer object that corresponds to the customer id.
        If none found, return None.'''
        pass

    # Note: this is a CLASS function (no self!)
    def get_all():
        query = "SELECT * FROM customer"
        db = Db()
        db.execute(query)
        objects = db.fetchall()
        print(objects)
        new_list = []
        for an_object in objects:
            info = Customer.build_from_row(an_object)
            new_list.append(info)

        print(new_list)
        return new_list




        '''Get a list of Customer objects - one for each row in the 
        relevant table in the database.'''




# customer = Customer(None,None,None,None,None,None,None,None,None)
# object_row_list =customer.get_all()

# list_of_customer_objects = objects.build_from_row()
# print(list_of_customer_objects)

        
