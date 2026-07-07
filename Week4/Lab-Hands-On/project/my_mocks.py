class Database:
    """
    Simulates a database class with a save method.
    """
    def save(self, data):
        # Imagine this writes data to a real database
        print(f"Saving {data} to the database")
        return True

def store_data(db, data):
    """
    Function that saves data using the provided database object.
    """
    return db.save(data)