### Video Rental System ###

videos = []
customers = []


# Video class
class Video:
    def __init__(self, title, genre, video_id):
        self.title = title
        self.genre = genre
        self.video_id = video_id
        self.is_available = True
        #self.is_rented = False

    def __str__(self):
        status = "Available" if self.is_available else "Rented"
        return f"{self.title} ({self.genre}) - {status}"

    # def rent(self):
    #     if not self.is_rented:
    #         self.is_rented = True
    #         return f"{self.title} has been rented."
    #     else:
    #         return f"{self.title} is already rented."

    # def return_video(self):
    #     if self.is_rented:
    #         self.is_rented = False
    #         return f"{self.title} has been returned."
    #     else:
    #         return f"{self.title} was not rented."
        
# Customer class
class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.rented_videos = []

    def __str__(self):
        return f"{self.name} (ID: {self.customer_id})" ####

    # def rent_video(self, video):
    #     if not video.is_rented:
    #         video.rent()
    #         self.rented_videos.append(video)
    #         return f"{self.name} has rented {video.title}."
    #     else:
    #         return f"{video.title} is already rented."

    # def return_video(self, video):
    #     if video in self.rented_videos:
    #         video.return_video()
    #         self.rented_videos.remove(video)
    #         return f"{self.name} has returned {video.title}."
    #     else:
    #         return f"{self.name} did not rent {video.title}."
        
# Videostore class
class VideoStore:
    def __init__(self):
        self.videos = {}
        self.customers = {}

    def add_video(self, video):
        self.videos[video.video_id] = video
        print(f"Added: {video.title}")

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer
        print(f"Added: {customer.name}")
    
    def rent_video(self, customer_id, video_id):
        customer = self.customers.get(customer_id)
        video = self.videos.get(video_id)
        # customer = next((c for c in self.customers.values() if c.customer_id == customer_id), None)
        # video = next((v for v in self.videos.values() if v.video_id == video_id), None)
        if not customer or not video:
            print("Customer or video not found.")
            return
            # Check if video is available
        if video.is_available:
            video.is_available = False
            customer.rented_videos.append(video)
            print(f"{customer.name} has rented {video.title}.")
        else:
            print(f"Sorry, {video.title} is currently rented out.")
        
        # if customer and video:
        #     return customer.rent_video(video)
        # else:
        #     return "Customer or video not found."
        
    def return_video(self, customer_id, video_id):
        customer = self.customers.get(customer_id)
        video = self.videos.get(video_id)
        # customer = next((c for c in self.customers.values() if c.customer_id == customer_id), None)
        # video = next((v for v in self.videos.values() if v.video_id == video_id), None)
        if not customer or not video:
            print("Customer or video not found.")
            return
        if video in customer.rented_videos:
            video.is_available = True
            customer.rented_videos.remove(video)
            print(f"{customer.name} has returned {video.title}.")
        # if customer and video:
        #     return customer.return_video(video)
        else:
            print("That customer does not have this video.")
            #return "Customer or video not found."
        
    def list_available_videos(self):
        print("\n--- Available Videos ---")
        available = [video for video in self.videos.values() if video.is_available]
        for video in available:
            print(video)    
        if not available:
            print("No videos available.")
        # return available
    
    def list_customer_videos(self, customer_id):
        customer = self.customers.get(customer_id)
        # customer = next((c for c in self.customers.values() if c.customer_id == customer_id), None)
        if customer:
            print(customer)
            if not customer.rented_videos:
                print("No videos currently rented.")
            for video in customer.rented_videos:
                print(f"  Rented: {video}")
        # return self.customers   
    

# 1. Setup Store
store = VideoStore()

# 2. Add Content
store.add_video(Video("The Matrix", "Sci-Fi", "V01"))
store.add_video(Video("Inception", "Sci-Fi", "V02"))
store.add_customer(Customer("Alice", "C01"))

# 3. Simulate Operations
store.list_available_videos()
store.rent_video("C01", "V01")
store.list_customer_videos("C01")

# 4. Try renting same video again
store.rent_video("C01", "V01")

# 5. Return
store.return_video("C01", "V01")
store.list_available_videos()