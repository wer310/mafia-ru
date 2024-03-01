ordered_roles = ["Don",
                 "Resident",
                 "Detective",
                 "Doctor",
                 "Mafia",
                 "Mafia",
                 "Mafia",
                 "Doctor",
                 "Chef",
                 "Mafia",
                 "Detective",
                 "Miller",
                 "Mafia",
                 "Mafia",
                 "Mafia",
                 "Mafia"]

nRoles = {"Boxer" : 2,
          "Bride" : 5,
          "Bulletproof" : 9,
          "Bus Driver" : 3,
          "Chef" : 3,
          "Clown" : 2,
          "Curious Kid" : 2,
          "Detective" : 3,
          "Doctor" : 10,
          "Don" : 4,
          "Genie" : 2,
          "Grandma" : 2,
          "Groom" : 4,
          "Hit Man" : 2,
          "Insane" : 3,
          "Jailer" : 2,
          "Judge" : 6,
          "Kind Wife" : 4,
          "Lawyer" : 3,
          "Made Man" : 2,
          "Mafia" : 9,
          "Magician" : 4,
          "Miller" : 3,
          "Postman" : 3,
          "Priest" : 3,
          "Rebel" : 3,
          "Reporter" : 6,
          "Resident" : 21,
          "Serial Killer" : 6,
          "Student" : 2,
          "Undercover Cop" : 2
          }

role2team = {"Boxer" : "mafia",
          "Bride" : "city",
          "Bulletproof" : "city",
          "Bus Driver" : "city",
          "Chef" : "city",
          "Clown" : "city",
          "Curious Kid" : "city",
          "Detective" : "city",
          "Doctor" : "city",
          "Don" : "mafia",
          "Genie" : "city",
          "Grandma" : "city",
          "Groom" : "city",
          "Hit Man" : "mafia",
          "Insane" : "city",
          "Jailer" : "city",
          "Judge" : "city",
          "Kind Wife" : "mafia",
          "Lawyer" : "mafia",
          "Made Man" : "mafia",
          "Mafia" : "mafia",
          "Magician" : "city",
          "Miller" : "city",
          "Postman" : "city",
          "Priest" : "city",
          "Rebel" : "city",
          "Reporter" : "city",
          "Resident" : "city",
          "Serial Killer" : "serial_killer",
          "Student" : "city",
          "Undercover Cop" : "city"
          }

descriptions = {"Boxor" : "Боксирует или является членом мафиозной команды. Боксирует или бьет одного из игроков ночью.",
                "Bride" : "Невеста - член городской команды. Невеста недавно была помолвлена с женихом, ночью оба"
                        "они встанут и увидят друг друга после смерти каждого из них, другой может убить"
                        "любой в качестве мести своей возлюбленной на ночной фазе.",
                "Bulletproof" : "Bulletproof is the most powerful resident which doesn't hurt from night shots. he/she won't die"
                                " through night phase.",
                "Bus Driver" : "Bus Driver is city team member. He/She can switch two player which means each shot/question"
                               " from first one will hurt/asked from second one.",
                "Chef" : "Шериф является важным членом городской команды. После его/ее смерти городская команда должна победить, наконец, через 3 дня.",
                "Clown" : "Clown is a member of city team. Clown forces someone to reveal his/her role for another players."
                          " Clown can do this just for one time and this should take place at night, GOD should be informed"
                          " whos role to be reavealed.",
                "Curious Kid" : "He/She is a member of city team which can open his/her eyes and spy on mafias in the way"
                          " that no one can see him/her.",
                "Detective" : "Детектив из городской команды встает ночью и пытается спросить БОГА, хороший ли кто-то"
                                " (Житель, Доктор, бунтарь, пуленепробиваемый) или плохой (мафия), но на его/ее первую попытку спросить у "
                                " Дона БОГ может дать неверный ответ.",
                "Doctor": "Доктор - полезный участник городской команды, который встает вслед за командой мафии и пытается спасти человека"
                            " (или двух в первую ночь) от выстрела мафии.",
                "Don" : "Дон - босс мафиозной группировки. На ночной фазе Дон решает, кого убить из команды мафии."
                        "Детектив не может обнаружить Дона.",
                "Genie" : "Genie is a kind member of city team despite his/her name. Genie selects a player at night and GOD "
                          "will ask the player to wish something and his/her wish will come true. Genie can use his/her power"
                          " just three time in a game.",
                "Grandma" : "Grandma with gun is a frightening member of city team. She will kill anyone who tries to kill her"
                            " at night. Mafia and other roles with kiling power should be aware of her.",
                "Groom" : "Groom is a member of city team. Groom has been engaged to Bride recently at nigh both of"
                        " them will get up and see each other after death of each one of them, other one can kill"
                        " anyone as a revenge of his/her sweetheart at night phase.",
                "Hit Man" : "Hit Man is a rather powerful member of mafia team. His/Her shots won't fail even if the doctor save"
                            " or the victim is Bulletproof. Hit Man can use his shot only one time during the game his shot will"
                            " be replaced by one of mafia's night shot.",
                "Insane" : "Insane is a member of city team. GOD will infrom Insane who is aiming at his/her neighbors (left hand"
                           " player or right hand player).",
                "Jailer" : "Jailer is a member of city team. Jailer can bust any player at night phase, one who has been busted won't"
                           " play at earlier day phase just for a night.",
                "Judge" : "Judge is a member of city team. Judge can reveal his role and decide to kill a player at day phase, Judge"
                          " can use his/her power only once during the game.",
                "Kind Wife" : "Kind Wife is mafia team's sweetheart. After the day she died the mafia team get up and kill two suspects"
                              " instead of one to take her revenge.",
                "Lawyer" : "Lawyer is from mafia team. Lawyer wakes up at night and inform the GOD whom should be sued to be to the court"
                           " for next day phase.",
                "Made Man" : "Made Man is the one of the most powerful participant of the mafia team. Made Man gets up at night and turn"
                             " one of the members of city team to Mafia.",
                "Mafia" : "Мафия - простой участник мафиозной команды. Мафия встает ночью и пытается решить, кого из"
                          "игроков они хотят убить, детектив может обнаружить этот вид мафии в ночной фазе.",
                "Magician" : "Magician is member of city team. He/She decides to kill or save a player during night and can use his/her"
                             "power just once during the game.",
                "Miller" : "Miller is a member of city team. When Detective ask GOD about Millers role the result will be bad(Mafia) so"
                           " Detective will be confused about Millers role and asume he/she as a mafia team member.",
                "Postman" : "Postman is a member of city team. After Postman's death he/she can select a player to die with him/her."
                            " With this power Postman can help city team by killing a mafia member.",
                "Priest" : "",
                "Rebel" : "Rebel is from city team which gets up at night phase and kills a person.if the victim was chosen from"
                                " residents, Rebel (him/her)self may die.",
                "Reporter" : "Reporter is a city team member. GOD will inform Reporter who was chosen by Made Man to become Mafia.",
                "Resident" : "Resident is the typical player of the game. he/she has no power but to blame mafia in order to remove "
                             "them from the game in day phase.",
                "Serial Killer" : "Serial Killer is a seperate team. He/She wakes up once each two night and shot a player."
                                  " Serial Killer will win if He/She is in last three players.",
                "Student" : "Student is a innocent city team member. After His/Her death, players will kill two players at day court.",
                "Undercover Cop" : "Undercover Cop is a member of city team but he/she will act just like mafia (wakes up at night)"
                                   " and decide whome to be killed)."}

descriptions_fa = {"Boxor" : "بوکسور عضو تیم مافیا است. او یک فرد را در شب انتخاب میکند و به او مشت میزند پس از این حرکت آن فرد نمیتواند در روز بعد صحبت کند.",
                   "Bride" : "عروس عضو تیم شهروندان است. او که به تازگی با داماد وصلت کرده است دوران عاشقی را میگذراند. در صورتی که داماد کشته شود عروس میتواند یک فردرا به دلخواه بکشد.",
                   "Bulletproof" : "ضد ضربه قوی ترين شهروند بازی ميباشد ،و از هر تير مافیا در فاز شب در امان ميباشد.بنابرين ضد ضربه توسط مافيا در فاز شب قابل کشته شدن نميباشد",
                   "BusDriver" : "راننده اتوبوس عضو تیم شهروندان است و میتواند جای دو نفر را عوض کند یعنی استعلامات و ضربه های روی نفر اول روی نفر دوم اثر میکند.",
                   "Chef" : "آشپز عضو تیم شهروندان است و با مرگ او شهروندان تنها ۳ روز دیگر برای برد وقت دارند و در غیر این صورت از گشنگی می میرند و مافیا برنده می شود",
                   "Clown" : "دلقک عضو تیم شهروندان است. در هر بازی میتواند یکبار یک فرد را انتخاب کند تا نقش خود را فاش کند.",
                   "Curious Kid" : "کودک کنجکاو عضو تیم شهروندان است. وی باید در شب به شکلی که کسی متوجه نشود تیم مافیا را تشخیص دهد.",
                   "Detective" : "کارآگاه يکی از اعضای تیم شهروند ميباشد که در فاز شب چشم هايش را باز کرده و ميتواند از خدای بازی هويت يکی از افراد بازی را بپرسد ، و خدا با اشاره بله يا خیر به کاراگاه ميگويد که فرد استعلام شده جزو اعضای مافيا هست يا نه",
                   "Doctor": "دکتر يکی از اعضای تیم شهروند ميباشد که در فاز شب به فرمان خدای بازی چشم هايش را باز کرده و ميتواند خود و يا يکی از بازيکنان را از حذف شدن و کشته شدن در فاز شب بازی نجات دهد.",
                   "Don" : "اين نقش سردسته تيم مافيا مي باشد و مسئوليت تيم مافيا بر عهده دُن است.امتياز حائز اهميتی که دُن در بازی دارد اين است که استعلامش توسط کاراگاه همانند شهروندان منفی میباشد.",
                   "Genie" : "غول چراغ جادو عضو تیم شهروندان است. در مجموع می تواند ۳ آرزو را برآورده کند. در شب مشخص می شود که آرزو چه کسی را برآورده کند در روز با آرزو کردن آن شخص آرزو او برآروده می شود",
                   "Grandma" : "مادربزرگ با اسلحه عضو تیم شهروندان است. در شب هر کسی که به وی سر بزند (بخواهد او را بکشد) خودش خواهد مرد.",
                   "Groom" : "داماد عضو تیم شهروندان است. او که به تازگی با عروس وصلت کرده است و دوران عاشقی خود را می گذراند . در صورتی که عروس در بازی بمیرد میتواند یک فرد را به دلخواه بکشد.",
                   "Hit Man" : "آدمکش یکی از حرفه ای ترین مافیا ها است. او تنها یک تیر دارد که جایگزین یکی از قتل های مافیا میشود. اگر تصمیم بگیرد کسی را بکشد چیزی جلوی او را نمیگیرد (نه دکتر و نه ضد ضربه بودن آن شخص)",
                   "Insane" : "دیوانه عضو تیم شهروندان است. در شب میتواند ببیند که چه کسی فرد کناری او را انتخاب کرده است.",
                   "Jailer" : "زندان بان عضو تیم شهروندان است. او هر شب به دلخواه یک فرد را انتخاب میکند تا به زندان برود و یک شب از بازی محروم شود.",
                   "Judge" : "قاضی عضو تیم شهروندان است. او نقش خود را فاش میکند و یک فرد را به دلخواه اعدام میکند.",
                   "Kind Wife" : "همسر مهربان عضو تیم مافیا است. با مرگ او مافیا ۲ نفر را در فاز شب میکشد.",
                   "Lawyer" : "وکیل عضو تیم مافیا است. او در شب بیدار میشود و تصمیم میگیرد که چه کسی باید امشب به دادگاه برود.",
                   "Made Man" : "آدم اجیر کن عضو تیم مافیا است. او شب از خواب بلند میشود و یک فرد از شهروندان را تبدیل به مافیا میکند.",
                   "Mafia" : "از اعضای تیم مافیا میباشد و اگر کارآگاه از او استعلام بگیرد، استعلامش مثبت می شود",
                   "Magician" : "جادوگر عضو تیم شهروندان است. او می تواند تنها یکبار یک فرد را بکشد یا نجات دهد.",
                   "Miller" : "آسیابان عضو تیم شهروندان است. استعلام آسیابان توسط کارآگاه منفی (شبیه مافیا) است .",
                   "Postman" : "پستچی یکی از اعضای شروندان است. او پس از مرگ یک فرد دیگر را برای مرگ انتخاب میکند و همراه خودش میکشد.",
                   "Priest" : "",
                   "Rebel" : "از اعضای تیم شهروند میباشد و در فاز شب میتواند کسی را که فکر میکند مافیا است را هدف قرار دهد اگر شخص مافیا بود خواهد مرد.اما اگر شورشی به اشتباه یک شهروند را هدف قرار دهد خودش خواهد مرد.",
                   "Reporter" : "گزارشگر عضو تیم شهروندان است. هنگامی که آدم اجیر کن بازیکنی را برای تیم مافیا انتخاب میکند به گزارشگر اطلاع داده می شود.",
                   "Resident" : "شهروند عضو ساده شهر است. تنها قدرتی که شهروند دارد حذف افراد به واسطه رای گیری در روز است",
                   "Serial Killer" : "قاتل سریالی یک تیم جدا است که اگر در ۳ نفر آخر باشد برنده است. او یک شب در میان بلند می شود و یک فرد را به دلخواه میشکد",
                   "Student" : "دانش آموز شهروند بیگناهی است که در صورت کشته شدن تیم شهروندان در فاز روز ۲ تفر را در دادگاه می شکند.",
                   "Undercover Cop" : "پلیس مخفی عضو تیم شهروندان است او به همراه مافیا بازی میکند و به همراه آن ها در شب بیدار میشود و افراد را برای مرگ انتخاب میکند ولی در نهایت باید به نفع شهروندان عمل کند."}

role2fa = {"Boxer" : "بوکسور",
          "Bride" : "عروس",
          "Bulletproof" : "ضدضربه",
          "Bus Driver" : "راننده اتوبوس",
          "Chef" : "آشپز",
          "Clown" : "دلقک",
          "Curious Kid" : "کودک کنجکاو",
          "Detective" : "کارآگاه",
          "Doctor" : "دکتر",
          "Don" : "دن",
          "Genie" : "غول چراغ جادو",
          "Grandma" : "مادربزرگ با اسلحه",
          "Groom" : "داماد",
          "Hit Man" : "آدم کش",
          "Insane" : "دیوانه",
          "Jailer" : "زندان بان",
          "Judge" : "قاضی",
          "Kind Wife" : "همسر مهربان",
          "Lawyer" : "وکیل",
          "Made Man" : "آدم اجیر کن",
          "Mafia" : "مافیا",
          "Magician" : "جادوگر",
          "Miller" : "آسیابان",
          "Postman" : "پست چی",
          "Priest" : "کشیش",
          "Rebel" : "شورشی",
          "Reporter" : "خبرنگار",
          "Resident" : "شهروند",
          "Serial Killer" : "قاتل سریالی",
          "Student" : "دانش آموز",
          "Undercover Cop" : "پلیس مخفی"}
