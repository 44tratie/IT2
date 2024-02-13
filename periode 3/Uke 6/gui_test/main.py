import customtkinter


def main() -> None:
    app = customtkinter.CTk()
    app.title("my app")
    app.geometry("640x360")
    app.grid_columnconfigure(0, weight=1)
    button = customtkinter.CTkButton(app, text="my button")
    button.grid(row=0, column=0, padx=20, pady=20, sticky="we")

    app.mainloop()


if __name__ == "__main__":
    main()
