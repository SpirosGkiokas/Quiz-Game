#data missing screen
class error_screen_data_missing():
    def __init__(self, game_frame, background):
        self.game_frame = game_frame
        self.Error_Canvas = Canvas(self.game_frame)
        self.Error_Canvas.config(background="#002b87")
        self.Error_Canvas.create_text(960,400,text="Error: Important Files Not Found", fill="White",
                                      font=("Arial", 40, "bold"))
        self.Error_Canvas.create_text(960,480,text="Please Try Installing The Game Again", fill="White",
                                      font=("Arial", 40, "bold"))
        self.Exit_Game_Button = Button(self.game_frame, text="Exit Game", font=("Arial", 45, "bold"), fg="White", 
                                        bg="Blue",cursor="hand2", border=8, command=close_app)
        self.Exit_Game_Button.place(x="780",y="750")
        #version label
        self.version_label = Label(self.game_frame, text="version 0.8.0",fg="White",bg="#000883")
        self.version_label.place(x="10",y="1050",anchor="nw")
        self.Error_Canvas.pack(expand=True, fill="both")

#create first user screen
class create_first_user():
    def __init__(self, game_frame, background):
        self.game_frame = game_frame
        self.Create_First_User_Canvas = Canvas(self.game_frame)
        self.Create_First_User_Canvas.create_image( 0, 0, image = background,  
                            anchor = "nw") 
        self.Create_First_User_Canvas.create_text(960,300,text="Welcome To Quiz Game", fill="White",
                                      font=("Arial", 40, "bold"))
        self.Create_First_User_Canvas.create_text(960,380,text="Please Create Your First User:", fill="White",
                                      font=("Arial", 40, "bold"))
        self.first_user_input = Entry(self.game_frame, fg="Black", font=("Arial", 35, "bold"),borderwidth=6, justify="center")
        self.first_user_input.place(x="960",y="500", anchor="center")
        self.Create_User_Button = Button(self.game_frame, text="Create User", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", border=8, command=self.get_write_first_user)
        self.Create_User_Button.place(x="960",y="640",anchor="center")
        self.Exit_Game_Button = Button(self.game_frame, text="Exit Game", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", border=8, command=close_app)
        self.Exit_Game_Button.place(x="1600",y="950")
        #version label
        self.version_label = Label(self.game_frame, text="version 0.8.0",fg="White",bg="#000883")
        self.version_label.place(x="10",y="1050",anchor="nw")
        self.Create_First_User_Canvas.pack(expand=True, fill="both")

    #getting entry input and if valid write
    def get_write_first_user(self):
        first_user = self.first_user_input.get()
        if(first_user.strip() == "" or first_user == "Invalid Input"):
            self.first_user_input.delete(0,END)
            self.first_user_input.insert(0, "Invalid Input")
        else:
            with open(last_user_data_path, "w")as write:
                write.writelines(first_user)
                write.close()
            with open(user_list_data_path, "w")as write:
                write.write(f"{first_user}")
                write.close()
            with open(f"{highscore_folder_path}\\{first_user}.txt", "a")as create_write:
                create_write.writelines("0")
                create_write.close()
            self.destroy_to_main_menu()

    #go to main menu
    def destroy_to_main_menu(self):
        self.Create_First_User_Canvas.destroy()
        self.Create_User_Button.destroy()
        self.Exit_Game_Button.destroy()
        self.first_user_input.destroy()
        main_menu(game_frame, background)

class main_menu():
    def __init__(self, game_frame, background):
        self.last_user = read_last_user()
        self.highscore = read_highscore(self.last_user[0].strip())
        self.game_frame = game_frame
        #main menu canvas creation
        self.Main_Menu_Canvas = Canvas(self.game_frame)
        self.Main_Menu_Canvas.create_image( 0, 0, image = background,  
                            anchor = "nw")
        self.Main_Menu_Canvas.create_text(1760, 1020, text=f"Highscore: {self.highscore[0].strip()}", fill="White",
                                          font=("Arial", 25, "bold"))
        #logo image creation
        self.logo_image = Label(self.game_frame, image=logo, border=0)
        self.logo_image.place(x="940",y="250",anchor="center")
        #welcoming user
        self.welcome_last_user_label = Label(text=f"Welcome {self.last_user[0].strip()}!")
        self.welcome_last_user_label.config(font=("Arial", 40, "bold"), fg="white", bg="#000883")
        self.welcome_last_user_label.place(x="960", y="400", anchor="center")
        #help button
        self.help_button = Button(self.game_frame, image=help_image, bg="Blue", cursor="hand2", border=5, command=self.go_to_rules)
        self.help_button.place(x="13", y="970")
        #version label
        self.version_label = Label(self.game_frame, text="version 0.8.0",fg="White",bg="#000883")
        self.version_label.place(x="10",y="1050",anchor="nw")
        #button frame and creating the buttons
        self.Button_Frame = Frame(self.game_frame)
        self.Start_Game_Button = Button(self.Button_Frame, text="Start Game", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", padx=120, border=8, command=self.destroy_to_category_selection)
        self.Change_User_Button = Button(self.Button_Frame, text="Change User", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", padx=120, border=8, command=self.destroy_to_select_user)
        self.Exit_Game_Button = Button(self.Button_Frame, text="Exit Game", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", padx=120, border=8, command=close_app)
        self.Start_Game_Button.pack(fill="both", expand=True)
        self.Change_User_Button.pack(fill="both", expand=True)
        self.Exit_Game_Button.pack(fill="both", expand=True)
        self.Button_Frame.place(x="960", y="700", anchor="center")
        #display main menu
        self.Main_Menu_Canvas.pack(expand=True, fill="both")

    #go to category selection
    def destroy_to_category_selection(self):
        self.Main_Menu_Canvas.destroy()
        self.logo_image.destroy()
        self.welcome_last_user_label.destroy()
        self.Button_Frame.destroy()
        self.Start_Game_Button.destroy()
        self.Change_User_Button.destroy()
        self.Exit_Game_Button.destroy()
        self.version_label.destroy()
        self.help_button.destroy()
        category_selection(game_frame, background)
    
    #go to select user
    def destroy_to_select_user(self):
        self.Main_Menu_Canvas.destroy()
        self.logo_image.destroy()
        self.welcome_last_user_label.destroy()
        self.Button_Frame.destroy()
        self.Start_Game_Button.destroy()
        self.Change_User_Button.destroy()
        self.Exit_Game_Button.destroy()
        self.version_label.destroy()
        self.help_button.destroy()
        select_user(game_frame, background)

    def go_to_rules(self):
        self.Main_Menu_Canvas.destroy()
        self.logo_image.destroy()
        self.welcome_last_user_label.destroy()
        self.Button_Frame.destroy()
        self.Start_Game_Button.destroy()
        self.Change_User_Button.destroy()
        self.Exit_Game_Button.destroy()
        self.version_label.destroy()
        self.help_button.destroy()
        rules(game_frame, background)

class category_selection:
    def __init__(self, game_frame, background):
        self.game_frame = game_frame
        self.Category_Selection_Canvas = Canvas(self.game_frame)
        self.Category_Selection_Canvas.create_image( 0, 0, image = background,  
                            anchor = "nw")
        self.Category_Selection_Canvas.create_text(960, 300, text="Select Category:", font=("Arial", 40, "bold"), fill="White")
        self.Button_Frame = Frame(self.game_frame)
        self.Geography_Button = Button(self.Button_Frame, text="Geography", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", padx=120, border=8, command=self.load_geography)
        self.Music_Button = Button(self.Button_Frame, text="Music", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", padx=120, border=8, command=self.load_music)
        self.History_Button = Button(self.Button_Frame, text="History", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", padx=120, border=8, command=self.load_history)
        self.Movies_Button = Button(self.Button_Frame, text="Movies", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", padx=120, border=8, command=self.load_movies)
        self.Geography_Button.pack(fill="both", expand=True)
        self.Music_Button.pack(fill="both", expand=True)
        self.History_Button.pack(fill="both", expand=True)
        self.Movies_Button.pack(fill="both", expand=True)
        self.Button_Frame.place(x="960", y="600", anchor="center")
        self.Go_Back_Button = Button(self.game_frame, text="Go Back", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", border=8, command=self.go_back_to_main_menu)
        self.Go_Back_Button.place(x="1650",y="950")
        #version label
        self.version_label = Label(self.game_frame, text="version 0.8.0",fg="White",bg="#000883")
        self.version_label.place(x="10",y="1050",anchor="nw")
        self.Category_Selection_Canvas.pack(expand=True, fill="both")

    #go to main menu
    def go_back_to_main_menu(self):
        self.Category_Selection_Canvas.destroy()
        self.Button_Frame.destroy()
        self.Geography_Button.destroy()
        self.Music_Button.destroy()
        self.History_Button.destroy()
        self.Movies_Button.destroy()
        self.Go_Back_Button.destroy()
        self.version_label.destroy()
        main_menu(game_frame, background)

    def load_geography(self):
        self.game_questions = geography_list
        self.generate_random_questions()

    def load_music(self):
        self.game_questions = music_list
        self.generate_random_questions()

    def load_history(self):
        self.game_questions = history_list
        self.generate_random_questions()

    def load_movies(self):
        self.game_questions = movies_list
        self.generate_random_questions()

    def generate_random_questions(self):
        len_question_list = int(len(self.game_questions) * 0.20)
        random_question_list = []
        for i in range(0, len_question_list):
            num = random.randint(0, len_question_list-1)
            while(num in random_question_list):
                num = random.randint(0, len_question_list-1)
            random_question_list.append(num)
        self.Category_Selection_Canvas.destroy()
        self.Button_Frame.destroy()
        self.Geography_Button.destroy()
        self.Music_Button.destroy()
        self.History_Button.destroy()
        self.Movies_Button.destroy()
        self.Go_Back_Button.destroy()
        self.version_label.destroy()
        game_screen(game_frame, background, self.game_questions, random_question_list, len_question_list)
    
class game_screen():
    def __init__(self, game_frame, background, game_questions, random_question_list, len_question_list):
        self.stop_game_bool = False
        self.count = 0
        self.score = 0
        self.mistake_count = 0
        self.game_frame = game_frame
        self.game_questions = game_questions
        self.random_question_list = random_question_list
        self.len_question_list = len_question_list
        self.Game_Canvas = Canvas(self.game_frame)
        self.Game_Canvas.create_image( 0, 0, image = background,  
                            anchor = "nw")
        self.button_frame = Frame(game_frame, bd=0)
        self.button_frame.place(x="960", y="400", height=400, width=600, anchor="n")                    
        self.check_count()
        self.stop_game_button = Button(self.game_frame, text="Stop Game", font=("Arial", 30, "bold"), bd=8, bg="Blue", fg="White", cursor="hand2", command=self.stop_game)
        self.stop_game_button.place(x="1650",y="970")
        #version label
        self.version_label = Label(self.game_frame, text="version 0.8.0",fg="White",bg="#000883")
        self.version_label.place(x="10",y="1050",anchor="nw")
        self.Game_Canvas.pack(expand=True, fill="both")

    def check_count(self):
        self.answered_bool = False
        if(self.count < self.len_question_list and self.mistake_count < 3):
            self.create_question()
        else:
            self.Game_Canvas.destroy()
            self.button_frame.destroy()
            self.stop_game_button.destroy()
            self.version_label.destroy()
            game_over_screen(game_frame, background, self.score, self.mistake_count, self.stop_game_bool)

    def create_question(self):
        self.Game_Canvas.create_text(960, 250, text=(f"{self.count + 1}/{self.len_question_list}  {self.game_questions[self.random_question_list[self.count] * 5]}"), 
                                     fill="White", font=("Arial", 35, "bold"),tags="question")
        self.Game_Canvas.create_text(960, 900, text=(f"Score: {self.score}"), 
                                     fill="White", font=("Arial", 35, "bold"),tags="score")
        self.Game_Canvas.create_text(960, 970, text=(f"Mistakes: {self.mistake_count}"), 
                                     fill="White", font=("Arial", 35, "bold"),tags="mistakes")
        self.answer_a_button = Button(self.button_frame, text=(self.game_questions[self.random_question_list[self.count] * 5 + 1]), font=("Arial", 35, "bold"),
                                      border=8, bg="Blue", fg="White", cursor="hand2", disabledforeground="White", command=self.submit_answer_a)
        self.answer_b_button = Button(self.button_frame, text=(self.game_questions[self.random_question_list[self.count] * 5 + 2]), font=("Arial", 35, "bold"),
                                      border=8, bg="Blue", fg="White", cursor="hand2", disabledforeground="White", command=self.submit_answer_b)
        self.answer_c_button = Button(self.button_frame, text=(self.game_questions[self.random_question_list[self.count] * 5 + 3]), font=("Arial", 35, "bold"),
                                      border=8, bg="Blue", fg="White", cursor="hand2", disabledforeground="White", command=self.submit_answer_c)
        self.answer_a_button.pack(fill="both", expand=True)
        self.answer_b_button.pack(fill="both", expand=True)
        self.answer_c_button.pack(fill="both", expand=True)
        self.timer = Label(self.game_frame, text=f"Time: 20 seconds", font=('Arial', 35, "bold"), bg="#000883", fg="White")
        self.timer.place(x="960", y="320", anchor="center")
        self.update_timer(20)

    def update_timer(self, count):  
        if (self.answered_bool == False):    
            if (count < 10 and count != 0):
                self.timer['text'] = f"Time: 0{count} seconds"
            elif (count == 0):
                self.timer['text'] = f"Time Out!!"
                self.answer_a_button.config(state="disabled")
                self.answer_b_button.config(state="disabled")
                self.answer_c_button.config(state="disabled")
                self.mistake_count += 1
                app.after(1500, self.destroy_to_next_question)
            else:
                self.timer['text'] = f"Time: {count} seconds"
            if (count > 0):
                app.after(1000, self.update_timer, count-1)
            

    def submit_answer_a(self):
        self.answered_bool = True
        if(self.game_questions[self.random_question_list[self.count] * 5 + 4] == "a"):
            self.answer_a_button.config(bg="Green")
            self.score += 10
            self.show_correct()
        else:
            self.answer_a_button.config(bg="Red")
            self.mistake_count += 1
            self.show_wrong()

    def submit_answer_b(self):
        self.answered_bool = True
        if(self.game_questions[self.random_question_list[self.count] * 5 + 4] == "b"):
            self.answer_b_button.config(bg="Green")
            self.score += 10
            self.show_correct()
        else:
            self.answer_b_button.config(bg="Red")
            self.mistake_count += 1
            self.show_wrong()

    def submit_answer_c(self):
        self.answered_bool = True
        if(self.game_questions[self.random_question_list[self.count] * 5 + 4] == "c"):
            self.answer_c_button.config(bg="Green")
            self.score += 10
            self.show_correct()
        else:
            self.answer_c_button.config(bg="Red")
            self.mistake_count += 1
            self.show_wrong()

    def show_correct(self):
        self.answer_a_button.config(state="disabled")
        self.answer_b_button.config(state="disabled")
        self.answer_c_button.config(state="disabled")
        app.after(1500, self.destroy_to_next_question)

    def show_wrong(self):
        self.answer_a_button.config(state="disabled")
        self.answer_b_button.config(state="disabled")
        self.answer_c_button.config(state="disabled")
        app.after(1500, self.destroy_to_next_question)
    
    def destroy_to_next_question(self):
        self.Game_Canvas.delete("question")
        self.Game_Canvas.delete("score")
        self.Game_Canvas.delete("mistakes")
        self.answer_a_button.destroy()
        self.answer_b_button.destroy()
        self.answer_c_button.destroy()
        self.timer.destroy()
        self.count += 1
        self.check_count()

    def stop_game(self):
        self.stop_game_bool = True
        self.answer_a_button.destroy()
        self.answer_b_button.destroy()
        self.answer_c_button.destroy()
        self.Game_Canvas.destroy()
        self.button_frame.destroy()
        self.stop_game_button.destroy()
        self.version_label.destroy()
        game_over_screen(game_frame, background, self.score, self.mistake_count, self.stop_game_bool)

class game_over_screen():
    def __init__(self, game_frame, background, score, mistake_count, stop_game_bool):
        self.game_frame = game_frame
        self.score = score
        self.mistake_count = mistake_count
        self.last_user = read_last_user()
        self.highscore = read_highscore(self.last_user[0].strip())
        self.highscore = int(self.highscore[0].strip())
        self.Game_Over_Canvas = Canvas(self.game_frame)
        self.Game_Over_Canvas.create_image( 0, 0, image = background,  anchor = "nw")
        self.Game_Over_Canvas.create_text(960, 400, text="Game Over", font=("Arial", 55, "bold"), fill="White")
        if(self.mistake_count > 2):
            self.Game_Over_Canvas.create_text(960, 500, text="Maximum amount of mistakes reached!!", font=("Arial", 28, "bold"), fill="White")
        elif(stop_game_bool):
            self.Game_Over_Canvas.create_text(960, 500, text="Game Stopped!!", font=("Arial", 28, "bold"), fill="White")
        else:
            self.Game_Over_Canvas.create_text(960, 500, text="Out Of Questions!!", font=("Arial", 28, "bold"), fill="White")
        if(self.highscore > score):
           self.Game_Over_Canvas.create_text(960, 600, text=f"Score: {self.score}", font=("Arial", 50, "bold"), fill="White")
        else:
            self.Game_Over_Canvas.create_text(960, 600, text=f"New Highscore: {self.score}", font=("Arial", 50, "bold"), fill="White")
            with open(f"{highscore_folder_path}\\{self.last_user[0].strip()}.txt", "w")as write:
                write.writelines(str(self.score))
                write.close()
        self.go_back_to_main_menu_button = Button(self.game_frame, text="Go Back To Main Menu", font=("Arial", 35, "bold"), fg="White", 
                                    bg="Blue", cursor="hand2", border=8, command=self.go_back_to_main_menu)
        self.go_back_to_main_menu_button.place(x="960", y="900", anchor="center")
        #version label
        self.version_label = Label(self.game_frame, text="version 0.8.0",fg="White",bg="#000883")
        self.version_label.place(x="10",y="1050",anchor="nw")
        self.Game_Over_Canvas.pack(expand=True, fill="both")

    def go_back_to_main_menu(self):
        self.Game_Over_Canvas.destroy()
        self.go_back_to_main_menu_button.destroy()
        self.version_label.destroy()
        main_menu(game_frame, background)

class select_user():
    def __init__(self, game_frame, background):
        self.users = read_user_list()
        self.game_frame = game_frame
        self.Selection_User_Canvas = Canvas(self.game_frame)
        self.Selection_User_Canvas.create_image( 0, 0, image = background,  anchor = "nw")
        self.Selection_User_Canvas.create_text(960, 80, text="Select User:", font=("Arial", 50, "bold"), fill="White")
        self.Go_Back_Button = Button(self.game_frame, text="Go Back", font=("Arial", 35, "bold"), fg="White", 
                                    bg="Blue", cursor="hand2", border=8, command=self.go_back_to_main_menu)
        self.Go_Back_Button.place(x="1650",y="920")
        #user list box
        self.userlistbox = Listbox(self.game_frame, bg="Blue", fg="White", bd=2, font=("Arial", 45, "bold"), justify="center",selectmode=SINGLE)
        self.scrollbar = Scrollbar(self.userlistbox)
        self.scrollbar.pack(side = RIGHT, fill = BOTH) 
        self.userlistbox.place(x="960",y="150",anchor="n",height="630", width="700")
        for i in range (0, len(self.users)):
            self.userlistbox.insert(END,self.users[i].strip())
        self.userlistbox.config(yscrollcommand = self.scrollbar.set) 
        self.scrollbar.config(command = self.userlistbox.yview) 
        #select delete create buttons
        self.Delete_User_Button = Button(self.game_frame, text="Delete", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", border=8, padx=75, command=self.delete_user)
        self.Select_User_Button = Button(self.game_frame, text="Select", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", border=8, padx=75, command=self.select_to_main_menu)
        self.Create_New_User_Button = Button(self.game_frame, text="Create New User", font=("Arial", 35, "bold"), fg="White", 
                                            bg="Blue", cursor="hand2", border=8, padx=137, command=self.go_to_create_new_user)
        self.Delete_User_Button.place(x="610",y="800")
        if (len(self.users) < 2):
            self.Delete_User_Button.config(state="disabled")
        else:
            self.Delete_User_Button.config(state="normal")
        self.Select_User_Button.place(x="970",y="800")
        self.Create_New_User_Button.place(x="610",y="920")
        #version label
        self.version_label = Label(self.game_frame, text="version 0.8.0",fg="White",bg="#000883")
        self.version_label.place(x="10",y="1050",anchor="nw")
        self.Selection_User_Canvas.pack(expand=True, fill="both")

     #go to main menu
    def go_back_to_main_menu(self):
        self.Selection_User_Canvas.destroy()
        self.Go_Back_Button.destroy()
        self.version_label.destroy()
        self.userlistbox.destroy()
        self.scrollbar.destroy()
        self.Delete_User_Button.destroy()
        self.Select_User_Button.destroy()
        self.Create_New_User_Button.destroy()
        main_menu(game_frame, background)

    def select_to_main_menu(self):
        #if none selected go back with previous user
        self.new_last_user = self.userlistbox.get(ACTIVE)
        if (self.new_last_user == None):
            self.go_back_to_main_menu()
        else: 
            with open(last_user_data_path, "w")as write:
                write.writelines(self.new_last_user)
                write.close()
            self.Selection_User_Canvas.destroy()
            self.Go_Back_Button.destroy()
            self.version_label.destroy()
            self.userlistbox.destroy()
            self.scrollbar.destroy()
            self.Delete_User_Button.destroy()
            self.Select_User_Button.destroy()
            self.Create_New_User_Button.destroy()
            main_menu(game_frame, background)

    def go_to_create_new_user(self):
        self.Selection_User_Canvas.destroy()
        self.Go_Back_Button.destroy()
        self.version_label.destroy()
        self.userlistbox.destroy()
        self.scrollbar.destroy()
        self.Delete_User_Button.destroy()
        self.Select_User_Button.destroy()
        self.Create_New_User_Button.destroy()
        create_new_user(game_frame, background)

    def delete_user(self):
        self.user_to_delete = self.userlistbox.get(ACTIVE)
        if (self.user_to_delete == None):
            self.go_back_to_main_menu()
        else:
            self.users = [user.strip() for user in self.users if user.strip() != self.user_to_delete]
            self.new_user_list = [user for user in self.users if user]
            user_file_path = os.path.join(highscore_folder_path, f"{self.user_to_delete}.txt")
            if os.path.exists(user_file_path):
                os.remove(user_file_path)
            if self.new_user_list:
                with open(user_list_data_path, "w") as write:
                    write.writelines("\n".join(self.new_user_list))
            if read_last_user() not in self.new_user_list:
                with open(last_user_data_path, "w") as write:
                    write.write(self.new_user_list[0])
            self.Selection_User_Canvas.destroy()
            self.Go_Back_Button.destroy()
            self.version_label.destroy()
            self.userlistbox.destroy()
            self.scrollbar.destroy()
            self.Delete_User_Button.destroy()
            self.Select_User_Button.destroy()
            self.Create_New_User_Button.destroy()
            select_user(game_frame, background)     

class create_new_user:
    def __init__(self, game_frame, background):
        self.game_frame = game_frame
        self.Create_User_Canvas = Canvas(self.game_frame)
        self.Create_User_Canvas.create_image( 0, 0, image = background,  
                            anchor = "nw")
        self.Create_User_Canvas.create_text(960, 250, text="Create New User:", font=("Arial", 50, "bold"), fill="White")
        self.new_user_input = Entry(self.game_frame, fg="Black", font=("Arial", 35, "bold"),borderwidth=6, justify="center")
        self.new_user_input.place(x="960",y="400", anchor="center")
        self.Create_User_Button = Button(self.game_frame, text="Create User", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", border=8, command=self.write_new_user)
        self.Create_User_Button.place(x="960",y="540",anchor="center")
        self.Go_Back_Button = Button(self.game_frame, text="Go Back", font=("Arial", 35, "bold"), fg="White", 
                                        bg="Blue", cursor="hand2", border=8, command=self.go_back_to_select_user)
        self.Go_Back_Button.place(x="1650",y="920")
        #version label
        self.version_label = Label(self.game_frame, text="version 0.8.0",fg="White",bg="#000883")
        self.version_label.place(x="10",y="1050",anchor="nw")
        self.Create_User_Canvas.pack(expand=True, fill="both")

    def go_back_to_select_user(self):
        self.Create_User_Canvas.destroy()
        self.new_user_input.destroy()
        self.Create_User_Button.destroy()
        self.Go_Back_Button.destroy()
        self.version_label.destroy()
        select_user(game_frame, background)

    def write_new_user(self):
        self.new_user = self.new_user_input.get()
        self.user_list = read_user_list()
        if(self.new_user.strip() == "" or self.new_user.strip() == "Invalid Input" or self.new_user.strip() == "User Already Exists"):
            self.new_user_input.delete(0,END)
            self.new_user_input.insert("Invalid Input")
        elif (self.new_user.strip() in self.user_list):
            self.new_user_input.delete(0,END)
            self.new_user_input.insert("User Already Exists")
        else:
            with open(user_list_data_path, "a")as append:
                append.write(f"\n{self.new_user}")
                append.close()
            with open(last_user_data_path, "w")as write:
                write.writelines(self.new_user)
                write.close()
            with open(f"{highscore_folder_path}\\{self.new_user}.txt", "a")as create:
                create.writelines("0")
                create.close()
            self.Create_User_Canvas.destroy()
            self.new_user_input.destroy()
            self.Create_User_Button.destroy()
            self.Go_Back_Button.destroy()
            self.version_label.destroy()
            main_menu(game_frame, background)

class rules:
    def __init__(self, game_frame, background):
        self.game_frame = game_frame
        self.Rules_Canvas = Canvas(self.game_frame)
        self.Rules_Canvas.create_image( 0, 0, image = background,  
                            anchor = "nw")
        #rules section
        self.Rules_Canvas.create_text(960, 200, text="Rules:", font=("Arial", 50, "bold"), fill="White")
        self.Rules_Canvas.create_text(960, 350, text="1: You can not make more than 2 mistakes", font=("Arial", 30, "bold"), fill="White")
        self.Rules_Canvas.create_text(960, 450, text="2: There is a timer in place. If you run out of time,", font=("Arial", 30, "bold"), fill="White")
        self.Rules_Canvas.create_text(960, 500, text=" it counts as a mistake.", font=("Arial", 30, "bold"), fill="White")
        #go back button
        self.go_back_to_main_menu_button = Button(self.game_frame, text="Go Back To Main Menu", font=("Arial", 35, "bold"), fg="White", 
                                    bg="Blue", cursor="hand2", border=8, command=self.go_back_to_main_menu)
        self.go_back_to_main_menu_button.place(x="960", y="900", anchor="center")
        #version label
        self.version_label = Label(self.game_frame, text="version 0.8.0",fg="White",bg="#000883")
        self.version_label.place(x="10",y="1050",anchor="nw")
        self.Rules_Canvas.pack(expand=True, fill="both")

    def go_back_to_main_menu(self):
        self.Rules_Canvas.destroy()
        self.version_label.destroy()
        self.go_back_to_main_menu_button.destroy()
        main_menu(game_frame, background)
            
#data validation function
def validate_data():
    #critical data corrupted or deleted
    if(os.path.exists(data_path) == False or os.path.exists(assets_path) == False or os.path.exists(question_data_path) == False):
        error_screen_data_missing(game_frame, background)
    #if critical data exist
    else:    
        #less serious data
        if(os.path.exists(user_data_path) == False):
            os.mkdir(user_data_path)
        if(os.path.exists(highscore_folder_path) == False):
            os.mkdir(highscore_folder_path)
        if(os.path.exists(last_user_data_path) == False):
            with open(last_user_data_path,"a")as create:
                create.close()
        if(os.path.exists(user_list_data_path) == False):
            with open(user_list_data_path,"a")as create:
                create.close()
        #if last user is corrupted
        if(os.path.getsize(last_user_data_path) == 0 and os.path.getsize(user_list_data_path) != 0):
            user_list = read_user_list()
            first_user = user_list[0].strip()
            with open(last_user_data_path, "r")as write:
                write.writelines(first_user)
                write.close()
        #if user list is corrupted but last user has data
        if(os.path.getsize(user_list_data_path) == 0 and os.path.getsize(last_user_data_path) != 0):
            last_user = f"{read_last_user()}\n"
            with open(user_list_data_path,"w")as write:
                write.writelines(last_user)
                write.close()
        #highscore files validation
        user_list = read_user_list()
        for i in range(0, len(user_list)):
            if(os.path.exists(f"{highscore_folder_path}\\{user_list[i].strip()}.txt") == False):
                with open(f"{highscore_folder_path}\\{user_list[i].strip()}.txt", "a")as create_write:
                    create_write.writelines("0")
                    create_write.close()
            elif(os.path.getsize(f"{highscore_folder_path}\\{user_list[i].strip()}.txt") == 0):
                with open(f"{highscore_folder_path}\\{user_list[i].strip()}.txt", "w")as write:
                    write.writelines("0")
                    write.close()
        users = read_user_list()
        try:
            if(read_last_user() not in users):
                with open(last_user_data_path, "w")as write:
                    write.writelines(users[0])
        except:
            pass
        #if no user data found
        if(os.path.getsize(user_list_data_path) == 0 and os.path.getsize(last_user_data_path) == 0):
            create_first_user(game_frame, background)
        else:
            main_menu(game_frame, background)

#read user list function
def read_user_list():
    with open(user_list_data_path,"r")as read:
        user_list = read.readlines()
        read.close()
    return user_list

#read last user function
def read_last_user():
    with open(last_user_data_path,"r")as read:
        last_user = read.readlines()
        read.close()
    return last_user

def read_highscore(user):
    with open(f"{highscore_folder_path}\\{user}.txt","r")as read:
        highscore = read.readlines()
        read.close()
    return highscore

#close app function
def close_app():
    app.destroy()

#importing libs
from tkinter import *
import random
import os
import ctypes
from Data.QuestionData.questions import *

#paths for data
dir_path = os.getcwd()
data_path = f"{dir_path}\\Data"
assets_path = f"{data_path}\\Assets"
question_data_path = f"{data_path}\\QuestionData"
user_data_path = f"{data_path}\\Users"
last_user_data_path = f"{user_data_path}\\last_user.txt"
user_list_data_path = f"{user_data_path}\\user_list.txt"
highscore_folder_path = f"{user_data_path}\\Highscores"


#task bar show icon
myappid = 'Quiz_Game'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#initializing app
app = Tk()

#making app fullscreen and naming it
app.attributes("-fullscreen", True)
app.title("Quiz Game")

#PhotoImage
background = PhotoImage(file=f"{data_path}\\Assets\\background.png")
app_icon = PhotoImage(file=f"{data_path}\\Assets\\icon.png")
logo = PhotoImage(file=f"{data_path}\\Assets\\game_logo_main_menu.png")
help_image = PhotoImage(file=f"{data_path}\\Assets\\help.png")

#icon of window
app.iconphoto(False, app_icon)

#making game frame
game_frame = Frame(app)

#displaying game frame
game_frame.pack(expand="true", fill="both")

#validate data function and continue at the appropriate screen classes
validate_data()

#mainloop - display window
app.mainloop()