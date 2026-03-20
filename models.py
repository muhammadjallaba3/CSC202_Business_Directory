from datetime import datetime

class Business:
    # Requirement: OOP Class with __init__
    def __init__(self, name, category, location):
        self.name = name
        self.category = category
        self.location = location
        # Requirement: Using datetime API for timestamping
        self.date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Requirement: Custom behavior method
    def get_summary(self):
        return f"Business: {self.name} | Category: {self.category} | Location: {self.location} | Added: {self.date_added}"


class DirectoryManager:
    def __init__(self):
        self.all_businesses = []  # List to store all our business objects
        # Requirement: Implement a Stack (LIFO) for Recently Added/Viewed
        self.recent_history_stack = [] 

    def add_business(self, business_obj):
        self.all_businesses.append(business_obj)
        self.recent_history_stack.append(business_obj) # Push to stack

    def get_recently_added(self):
        """Returns the most recently added business using Stack logic (LIFO)"""
        if self.recent_history_stack:
            return self.recent_history_stack[-1] # Look at the top of the stack
        return None