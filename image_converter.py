import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter")

        self.source_image_path = ""
        self.target_format = ""

        # Create widgets
        self.label_source = tk.Label(root, text="Source Image:")
        self.label_source.pack()

        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()

        self.button_browse = tk.Button(root, text="Browse Image", command=self.browse_image)
        self.button_browse.pack()

        self.label_target_format = tk.Label(root, text="Save Format:")
        self.label_target_format.pack()

        self.entry_target_format = tk.Entry(root)
        self.entry_target_format.pack()

        self.button_convert = tk.Button(root, text="Convert", command=self.convert_image)
        self.button_convert.pack()

        self.label_status = tk.Label(root, text="")
        self.label_status.pack()

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

        if file_path:
            self.source_image_path = file_path
            self.load_image()

    def load_image(self):
        image = Image.open(self.source_image_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)

        self.canvas.config(width=photo.width(), height=photo.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def convert_image(self):
        if not self.source_image_path:
            self.label_status.config(text="Select an image.")
            return

        target_format = self.entry_target_format.get().lower()

        if not target_format:
            self.label_status.config(text="Enter a format for saving.")
            return

        try:
            image = Image.open(self.source_image_path)
            target_path = filedialog.asksaveasfilename(defaultextension=f".{target_format}", filetypes=[(f"Images (*.{target_format})", f"*.{target_format}")])

            if target_path:
                image.save(target_path)
                self.label_status.config(text=f"Image successfully saved to {target_path}.")
            else:
                self.label_status.config(text="Canceled.")
        except Exception as e:
            self.label_status.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
