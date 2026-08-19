import customtkinter as ctk
from tkinter import messagebox

# =========================================================
# Student data and original project logic
# =========================================================
students = {}


def add_student(name, grades):
    students[name] = grades


def avg_student(name):
    if name in students:
        return sum(students[name]) / len(students[name])
    return None


def best_student():
    if not students:
        return None

    best_avg = -1
    best_names = []

    for name, grades in students.items():
        average = sum(grades) / len(grades)

        if average > best_avg:
            best_avg = average
            best_names = [name]
        elif average == best_avg:
            best_names.append(name)

    return best_names, best_avg


def accepted_students():
    accepted = []

    for name in students:
        if avg_student(name) >= 15:
            accepted.append(name)

    return accepted


# =========================================================
# Appearance
# =========================================================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

BG = "#F3F5F8"
CARD = "#FFFFFF"
DARK = "#18212B"
TEXT = "#303A46"
MUTED = "#788493"
LINE = "#E1E6EC"
BLUE = "#2563EB"
BLUE_HOVER = "#1D4ED8"
GREEN = "#16A34A"
GREEN_HOVER = "#15803D"
RED = "#DC2626"
SOFT_BLUE = "#EEF4FF"
SOFT_GREEN = "#ECFDF3"
SOFT_ORANGE = "#FFF7ED"


class StudentApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Student Management System")
        self.geometry("1100x720")
        self.minsize(980, 650)
        self.configure(fg_color=BG)

        self.student_count_var = ctk.StringVar(value="0")
        self.overall_var = ctk.StringVar(value="—")
        self.best_var = ctk.StringVar(value="—")
        self.accepted_var = ctk.StringVar(value="0")

        self.build_sidebar()
        self.build_main()

        self.show_page("dashboard")
        self.refresh_all()

    # =====================================================
    # Sidebar
    # =====================================================
    def build_sidebar(self):
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0,
            fg_color=DARK
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        ctk.CTkLabel(
            self.sidebar,
            text="STUDENT",
            text_color="#AEB9C6",
            font=ctk.CTkFont(size=11, weight="bold")
        ).pack(anchor="w", padx=25, pady=(32, 0))

        ctk.CTkLabel(
            self.sidebar,
            text="Manager",
            text_color="white",
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(anchor="w", padx=23, pady=(0, 5))

        ctk.CTkLabel(
            self.sidebar,
            text="Python desktop application",
            text_color="#8491A0",
            font=ctk.CTkFont(size=10)
        ).pack(anchor="w", padx=25, pady=(0, 35))

        self.dashboard_btn = self.nav_button(
            "Dashboard", lambda: self.show_page("dashboard")
        )
        self.dashboard_btn.pack(fill="x", padx=15, pady=4)

        self.add_btn = self.nav_button(
            "Add Student", lambda: self.show_page("add")
        )
        self.add_btn.pack(fill="x", padx=15, pady=4)

        self.students_btn = self.nav_button(
            "Students", lambda: self.show_page("students")
        )
        self.students_btn.pack(fill="x", padx=15, pady=4)

        ctk.CTkFrame(
            self.sidebar,
            height=1,
            fg_color="#303B48"
        ).pack(fill="x", padx=25, pady=30)

        ctk.CTkLabel(
            self.sidebar,
            text="Built with Python",
            text_color="#718091",
            font=ctk.CTkFont(size=10)
        ).pack(side="bottom", pady=22)

    def nav_button(self, text, command):
        return ctk.CTkButton(
            self.sidebar,
            text=text,
            command=command,
            height=44,
            corner_radius=10,
            anchor="w",
            fg_color="transparent",
            hover_color="#293442",
            text_color="#D8E0E8",
            font=ctk.CTkFont(size=12, weight="bold")
        )

    # =====================================================
    # Main area
    # =====================================================
    def build_main(self):
        self.main = ctk.CTkFrame(
            self,
            fg_color=BG,
            corner_radius=0
        )
        self.main.pack(side="left", fill="both", expand=True)

        self.header = ctk.CTkFrame(
            self.main,
            height=78,
            fg_color=CARD,
            corner_radius=0,
            border_width=1,
            border_color=LINE
        )
        self.header.pack(fill="x")
        self.header.pack_propagate(False)

        self.page_title = ctk.CTkLabel(
            self.header,
            text="Dashboard",
            text_color=DARK,
            font=ctk.CTkFont(size=22, weight="bold")
        )
        self.page_title.pack(side="left", padx=28)

        self.page_subtitle = ctk.CTkLabel(
            self.header,
            text="Overview of your students",
            text_color=MUTED,
            font=ctk.CTkFont(size=10)
        )
        self.page_subtitle.pack(side="left", padx=(5, 0))

        self.pages = ctk.CTkFrame(self.main, fg_color=BG, corner_radius=0)
        self.pages.pack(fill="both", expand=True)

        self.build_dashboard()
        self.build_add_page()
        self.build_students_page()

    # =====================================================
    # Common card
    # =====================================================
    def card(self, parent, **kwargs):
        return ctk.CTkFrame(
            parent,
            fg_color=CARD,
            corner_radius=14,
            border_width=1,
            border_color=LINE,
            **kwargs
        )

    def page_heading(self, parent, title, subtitle):
        ctk.CTkLabel(
            parent,
            text=title,
            text_color=DARK,
            font=ctk.CTkFont(size=21, weight="bold")
        ).pack(anchor="w", padx=28, pady=(25, 2))

        ctk.CTkLabel(
            parent,
            text=subtitle,
            text_color=MUTED,
            font=ctk.CTkFont(size=10)
        ).pack(anchor="w", padx=28, pady=(0, 20))

    # =====================================================
    # Dashboard
    # =====================================================
    def build_dashboard(self):
        self.dashboard_page = ctk.CTkFrame(
            self.pages, fg_color=BG, corner_radius=0
        )

        self.page_heading(
            self.dashboard_page,
            "Dashboard",
            "A clean overview of your student data."
        )

        stats = ctk.CTkFrame(self.dashboard_page, fg_color="transparent")
        stats.pack(fill="x", padx=20)

        self.stat_card(stats, "TOTAL STUDENTS", self.student_count_var, SOFT_BLUE, BLUE)
        self.stat_card(stats, "OVERALL AVERAGE", self.overall_var, "#F5F3FF", "#7C3AED")
        self.stat_card(stats, "BEST STUDENT", self.best_var, SOFT_GREEN, GREEN)
        self.stat_card(stats, "ACCEPTED 15+", self.accepted_var, SOFT_ORANGE, "#EA580C")

        overview = self.card(self.dashboard_page)
        overview.pack(fill="both", expand=True, padx=28, pady=24)

        ctk.CTkLabel(
            overview,
            text="Project overview",
            text_color=DARK,
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(anchor="w", padx=24, pady=(22, 5))

        ctk.CTkLabel(
            overview,
            text=(
                "A practical Python student-management project. "
                "The application stores students and grades, calculates averages, "
                "finds the best student and shows accepted students."
            ),
            text_color=TEXT,
            justify="left",
            wraplength=800,
            font=ctk.CTkFont(size=11)
        ).pack(anchor="w", padx=24, pady=(0, 22))

    def stat_card(self, parent, title, variable, bg_color, accent):
        card = ctk.CTkFrame(
            parent,
            fg_color=CARD,
            corner_radius=14,
            border_width=1,
            border_color=LINE
        )
        card.pack(side="left", fill="both", expand=True, padx=7)

        ctk.CTkFrame(
            card,
            width=5,
            fg_color=accent,
            corner_radius=3
        ).pack(side="left", fill="y", padx=(12, 0), pady=14)

        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(side="left", fill="both", expand=True, padx=13, pady=15)

        ctk.CTkLabel(
            body,
            text=title,
            text_color=MUTED,
            font=ctk.CTkFont(size=9, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            body,
            textvariable=variable,
            text_color=DARK,
            font=ctk.CTkFont(size=17, weight="bold"),
            wraplength=170,
            justify="left"
        ).pack(anchor="w", pady=(5, 0))

    # =====================================================
    # Add page
    # =====================================================
    def build_add_page(self):
        self.add_page = ctk.CTkFrame(
            self.pages, fg_color=BG, corner_radius=0
        )

        self.page_heading(
            self.add_page,
            "Add Student",
            "Add a student and enter their grades."
        )

        card = self.card(self.add_page)
        card.pack(fill="x", padx=28, pady=5)

        ctk.CTkLabel(
            card,
            text="Student information",
            text_color=DARK,
            font=ctk.CTkFont(size=16, weight="bold")
        ).grid(row=0, column=0, columnspan=2, sticky="w", padx=25, pady=(23, 5))

        ctk.CTkLabel(
            card,
            text="Name",
            text_color=TEXT,
            font=ctk.CTkFont(size=11, weight="bold")
        ).grid(row=1, column=0, sticky="w", padx=(25, 12), pady=(18, 8))

        self.name_entry = ctk.CTkEntry(
            card,
            height=40,
            placeholder_text="Enter student name",
            border_color=LINE,
            fg_color="#FAFBFC",
            text_color=TEXT
        )
        self.name_entry.grid(row=1, column=1, sticky="ew", padx=(0, 25), pady=(18, 8))

        ctk.CTkLabel(
            card,
            text="Grades",
            text_color=TEXT,
            font=ctk.CTkFont(size=11, weight="bold")
        ).grid(row=2, column=0, sticky="w", padx=(25, 12), pady=8)

        self.grades_entry = ctk.CTkEntry(
            card,
            height=40,
            placeholder_text="Example: 18, 17.5, 20",
            border_color=LINE,
            fg_color="#FAFBFC",
            text_color=TEXT
        )
        self.grades_entry.grid(row=2, column=1, sticky="ew", padx=(0, 25), pady=8)

        ctk.CTkLabel(
            card,
            text="Grades must be between 0 and 20. Separate grades with commas.",
            text_color=MUTED,
            font=ctk.CTkFont(size=9)
        ).grid(row=3, column=1, sticky="w", padx=(0, 25), pady=(0, 20))

        card.grid_columnconfigure(1, weight=1)

        button_row = ctk.CTkFrame(card, fg_color="transparent")
        button_row.grid(row=4, column=0, columnspan=2, sticky="e", padx=25, pady=(0, 23))

        ctk.CTkButton(
            button_row,
            text="Clear",
            command=self.clear_form,
            width=110,
            height=40,
            corner_radius=9,
            fg_color="#F1F3F6",
            hover_color="#E5E8EC",
            text_color=TEXT
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            button_row,
            text="Add Student",
            command=self.save_student,
            width=140,
            height=40,
            corner_radius=9,
            fg_color=BLUE,
            hover_color=BLUE_HOVER,
            text_color="white",
            font=ctk.CTkFont(size=11, weight="bold")
        ).pack(side="left", padx=5)

    # =====================================================
    # Students page - grid/table with fixed columns
    # =====================================================
    def build_students_page(self):
        self.students_page = ctk.CTkFrame(
            self.pages, fg_color=BG, corner_radius=0
        )

        self.page_heading(
            self.students_page,
            "Students",
            "All students currently stored in the application."
        )

        card = self.card(self.students_page)
        card.pack(fill="both", expand=True, padx=28, pady=5)

        # Header row
        header_row = ctk.CTkFrame(
            card,
            fg_color="#F6F8FA",
            corner_radius=9
        )
        header_row.pack(fill="x", padx=15, pady=(15, 4))

        header_row.grid_columnconfigure(0, weight=3)
        header_row.grid_columnconfigure(1, weight=5)
        header_row.grid_columnconfigure(2, weight=2)

        for col, text in enumerate(("STUDENT", "GRADES", "AVERAGE")):
            ctk.CTkLabel(
                header_row,
                text=text,
                text_color=MUTED,
                font=ctk.CTkFont(size=9, weight="bold"),
                anchor="w"
            ).grid(
                row=0, column=col, sticky="ew",
                padx=(18 if col == 0 else 10, 10), pady=12
            )

        self.table_container = ctk.CTkScrollableFrame(
            card,
            fg_color=CARD,
            corner_radius=0
        )
        self.table_container.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.empty_label = ctk.CTkLabel(
            self.table_container,
            text="No students yet.\nAdd a student to see them here.",
            text_color=MUTED,
            font=ctk.CTkFont(size=12)
        )

    def refresh_table(self):
        for widget in self.table_container.winfo_children():
            widget.destroy()

        if not students:
            self.empty_label = ctk.CTkLabel(
                self.table_container,
                text="No students yet.\nAdd a student to see them here.",
                text_color=MUTED,
                font=ctk.CTkFont(size=12)
            )
            self.empty_label.pack(expand=True, pady=100)
            return

        self.table_container.grid_columnconfigure(0, weight=3, uniform="table")
        self.table_container.grid_columnconfigure(1, weight=5, uniform="table")
        self.table_container.grid_columnconfigure(2, weight=2, uniform="table")

        for row_index, (name, grades) in enumerate(students.items()):
            bg = CARD if row_index % 2 == 0 else "#FAFBFC"
            average = avg_student(name)
            grades_text = ", ".join(str(g) for g in grades)

            row = ctk.CTkFrame(
                self.table_container,
                fg_color=bg,
                corner_radius=8,
                border_width=1,
                border_color=LINE
            )
            row.grid(
                row=row_index,
                column=0,
                columnspan=3,
                sticky="ew",
                padx=2,
                pady=3
            )

            row.grid_columnconfigure(0, weight=3, uniform="row")
            row.grid_columnconfigure(1, weight=5, uniform="row")
            row.grid_columnconfigure(2, weight=2, uniform="row")

            ctk.CTkLabel(
                row,
                text=name,
                text_color=TEXT,
                font=ctk.CTkFont(size=10, weight="bold"),
                anchor="w"
            ).grid(row=0, column=0, sticky="ew", padx=(16, 8), pady=13)

            ctk.CTkLabel(
                row,
                text=grades_text,
                text_color=MUTED,
                font=ctk.CTkFont(size=10),
                anchor="w"
            ).grid(row=0, column=1, sticky="ew", padx=8, pady=13)

            average_bg = SOFT_GREEN if average >= 15 else "#FEF2F2"
            average_color = GREEN if average >= 15 else RED

            ctk.CTkLabel(
                row,
                text=f"{average:.2f}",
                text_color=average_color,
                fg_color=average_bg,
                corner_radius=8,
                font=ctk.CTkFont(size=10, weight="bold"),
                width=70
            ).grid(row=0, column=2, padx=12, pady=7)

    # =====================================================
    # Actions
    # =====================================================
    def save_student(self):
        name = self.name_entry.get().strip()
        raw_grades = self.grades_entry.get().strip()

        if not name:
            messagebox.showwarning("Missing name", "Please enter a student name.")
            return

        if not raw_grades:
            messagebox.showwarning("Missing grades", "Please enter at least one grade.")
            return

        try:
            parts = [part.strip() for part in raw_grades.split(",") if part.strip()]
            grades = [float(part) for part in parts]
        except ValueError:
            messagebox.showerror(
                "Invalid grades",
                "Grades must be numbers separated by commas.\nExample: 18, 17.5, 20"
            )
            return

        if any(grade < 0 or grade > 20 for grade in grades):
            messagebox.showerror(
                "Invalid grades",
                "Every grade must be between 0 and 20."
            )
            return

        add_student(name, grades)
        self.refresh_all()
        self.clear_form()

        messagebox.showinfo(
            "Student added",
            f"{name} was added successfully."
        )

    def clear_form(self):
        self.name_entry.delete(0, "end")
        self.grades_entry.delete(0, "end")
        self.name_entry.focus()

    def refresh_all(self):
        self.refresh_table()

        self.student_count_var.set(str(len(students)))

        if students:
            averages = [avg_student(name) for name in students]
            self.overall_var.set(f"{sum(averages) / len(averages):.2f}")
        else:
            self.overall_var.set("—")

        best = best_student()
        if best:
            names, average = best
            self.best_var.set(f"{' / '.join(names)}\n{average:.2f}")
        else:
            self.best_var.set("—")

        self.accepted_var.set(str(len(accepted_students())))

    def show_page(self, page):
        for frame in (
            self.dashboard_page,
            self.add_page,
            self.students_page
        ):
            frame.pack_forget()

        if page == "dashboard":
            self.dashboard_page.pack(fill="both", expand=True)
            self.page_title.configure(text="Dashboard")
            self.page_subtitle.configure(text="Overview of your students")

        elif page == "add":
            self.add_page.pack(fill="both", expand=True)
            self.page_title.configure(text="Add Student")
            self.page_subtitle.configure(text="Create or update student information")
            self.name_entry.focus()

        elif page == "students":
            self.students_page.pack(fill="both", expand=True)
            self.page_title.configure(text="Students")
            self.page_subtitle.configure(text="Student list and averages")
            self.refresh_table()


if __name__ == "__main__":
    app = StudentApp()
    app.mainloop()
