from tkinter import *
from PIL import ImageTk, Image

def print_ticket():
    city = city_var.get()
    cinema_hall = cinema_hall_var.get()
    movie = movie_var.get()
    num_tickets = num_tickets_var.get()
    timing = timing_var.get()
    
    ticket_info = f"City: {city}\nCinema Hall: {cinema_hall}\nMovie: {movie}\nNumber of Tickets: {num_tickets}\nTiming: {timing}"
    
    ticket_window = Toplevel(root)
    ticket_window.title("Ticket")
    
    ticket_label = Label(ticket_window, text=ticket_info, font=("Helvetica", 12), justify=LEFT)
    ticket_label.pack(padx=20, pady=20)

    # Calculate the Ticket Price
    
    ticket_price = 0

    # Price based on city
    if city == "Delhi":
        ticket_price += 10
    elif city == "Ghaziabad":
        ticket_price += 12
    elif city == "Lucknow":
        ticket_price += 15
    
    # Price based on cinema hall
    if cinema_hall == "PVR Cinemas":
        ticket_price += 5
    elif cinema_hall == "INOX":
        ticket_price += 8
    elif cinema_hall == "Cinepolis":
        ticket_price += 10
    
    # Price based on movie
    if movie == "The Flash":
        ticket_price += 10
    elif movie == "Avengers-Kang Dynasty":
        ticket_price += 12
    elif movie == "Fast XI":
        ticket_price += 15
    
    # Price based on timing
    if timing == "10:00 am":
        ticket_price *= 1.2
    elif timing == "12:45 pm":
        ticket_price *= 1.5
    elif timing == "3:10 pm":
        ticket_price *= 1.8
    
    # Calculate total price
    total_price = ticket_price * num_tickets
    
    price_label = Label(ticket_window, text=f"Total Price: ${total_price:.2f}", font=("Helvetica", 12), justify=LEFT)
    price_label.pack(pady=20)

# Create main window
root = Tk()
root.title("Movie Ticket Booking System")

# Configure window size and padding
root.geometry("1280x720")
root.configure(bg="#f2f2f2")
root.resizable(False, False)

#Load and set Background Image

bg_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Basit\Downloads\Bg_2.jpg"))
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# City selection
city_label = Label(root, text="Select City:", font=("Helvetica", 12))
city_label.pack(pady=10)

city_var = StringVar()
city_var.set("")

city_options = ["Delhi", "Ghaziabad", "Lucknow"]

city_dropdown = OptionMenu(root, city_var, *city_options)
city_dropdown.config(font=("Helvetica", 12), bg="#ffffff")
city_dropdown.pack(pady=(0, 10))

# Cinema hall selection
cinema_hall_label = Label(root, text="Select Cinema Hall:", font=("Helvetica", 12))
cinema_hall_label.pack(pady=10)

cinema_hall_var = StringVar()
cinema_hall_var.set("")

cinema_hall_options = ["PVR Cinemas", "INOX", "Cinepolis"]

cinema_hall_dropdown = OptionMenu(root, cinema_hall_var, *cinema_hall_options)
cinema_hall_dropdown.config(font=("Helvetica", 12), bg="#ffffff")
cinema_hall_dropdown.pack(pady=(0, 10))

# Movie selection
movie_label = Label(root, text="Select Movie:", font=("Helvetica", 12))
movie_label.pack(pady=10)

movie_var = StringVar()
movie_var.set("")

movie_options = ["The Flash", "Avengers-Kang Dynasty", "Fast XI"]

movie_dropdown = OptionMenu(root, movie_var, *movie_options)
movie_dropdown.config(font=("Helvetica", 12), bg="#ffffff")
movie_dropdown.pack(pady=(0, 10))

# Number of tickets entry
num_tickets_label = Label(root, text="Number of Tickets:", font=("Helvetica", 12))
num_tickets_label.pack(pady=10)

num_tickets_var = IntVar()
num_tickets_entry = Entry(root, textvariable=num_tickets_var, font=("Helvetica", 12), width=10)
num_tickets_entry.pack(pady=(0, 10))

# Timing selection
timing_label = Label(root, text="Select Timing:", font=("Helvetica", 12))
timing_label.pack(pady=10)

timing_var = StringVar()
timing_var.set("")

timing_options = ["10:00 am", "12:45 pm", "3:10 pm"]

timing_dropdown = OptionMenu(root, timing_var, *timing_options)
timing_dropdown.config(font=("Helvetica", 12), bg="#ffffff")
timing_dropdown.pack(pady=(0, 10))

# Submit button
submit_button = Button(root, text="Print Ticket", command=print_ticket, font=("Helvetica", 12), bg="#4caf50", fg="white", padx=20, pady=10, relief=FLAT)
submit_button.pack(pady=20)

# Run the main event loop
root.mainloop()
