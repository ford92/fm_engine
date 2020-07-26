from player import Player, Keeper

"""Every premier league team starting XI and each goalkeeper and outfield player creates 
class instance Keeper and Player respectively"""

teams_0 = ['Arsenal', Keeper('Leno', 9), Player('Tierney', 8, 2, 6, 7), Player('Bellerin', 8, 2, 6, 7), 
Player('Luiz', 8, 6, 3, 7), Player('Mustafi', 8, 2, 2, 7), Player('Xhaka', 9, 2, 4, 9), Player('Torreira', 9, 3, 9, 9),
Player('Pepe', 8, 7, 9, 2), Player('Saka', 9, 6, 9, 4), Player('Aubameyang', 8, 10, 9, 2), Player('Lacazette', 8, 9, 8, 3)]

teams_1 = ['Aston Villa', Keeper('Reina', 7), Player('N.Taylor', 5, 2, 6, 5), Player('Targett', 5, 2, 3, 4), 
Player('Mings', 7, 6, 3, 9), Player('Konsa', 6, 2, 2, 5), Player('Douglas Luiz', 6, 5, 6, 6), Player('Grealish', 8, 8, 8, 2),
Player('Trezeguet', 7, 7, 7, 2), Player('El Ghazi', 5, 4, 6, 4), Player('Samatta', 6, 6, 6, 2), Player('Davis', 4, 3, 2, 1)]

teams_2 = ['Bournemouth', Keeper('Rasmdale', 7), Player('Smith', 7, 2, 5, 7), Player('Rico', 8, 6, 5, 6), 
Player('S.Cook', 6, 2, 3, 6), Player('Ake', 8, 5, 7, 9), Player('L.Cook', 8, 4, 6, 8), Player('Lerma', 8, 4, 6, 8),
Player('Stanislas', 7, 7, 7, 4), Player('Brooks', 8, 8, 8, 4), Player('Wilson', 6, 7, 6, 2), Player('King', 6, 7, 7, 1)]

teams_3 = ['Brighton', Keeper('Ryan', 8), Player('Lamptey', 7, 2, 5, 5), Player('Burn', 8, 4, 4, 8), 
Player('Dunk', 7, 6, 5, 9), Player('Webster', 6, 5, 5, 8), Player('D. Stephens', 7, 2, 3, 9), Player('Gross', 8, 7, 8, 5),
Player('Trossard', 7, 5, 9, 3), Player('Mooy', 8, 7, 7, 8), Player('Maupay', 6, 8, 7, 7), Player('Connolly', 5, 5, 5, 4)]

teams_4 = ['Burnley', Keeper('Pope', 9), Player('Bardsley', 6, 2, 5, 8), Player('C.Taylor', 7, 4, 4, 8), 
Player('Mee', 7, 7, 2, 9), Player('Tarkowski', 7, 7, 2, 8), Player('Cork', 8, 2, 3, 8), Player('Westwood', 8, 6, 4, 7),
Player('McNeil', 8, 6, 9, 7), Player('Gudmundsson', 8, 7, 7, 7), Player('Wood', 5, 9, 3, 6), Player('A.Barnes', 5, 8, 5, 5)]

teams_5 = ['Chelsea', Keeper('Kepa', 7), Player('Azpilicueta', 9, 5, 5, 9), Player('Alonso', 9, 8, 4, 7), 
Player('Rudiger', 9, 6, 5, 10), Player('Zouma', 9, 5, 5, 9), Player('Jorginho', 9, 2, 7, 9), Player('Kante', 9, 5, 8, 10),
Player('Mount', 9, 8, 8, 5), Player('Willian', 9, 8, 9, 5), Player('Pulisic', 9, 8, 10, 5), Player('Giroud', 9, 7, 7, 8)]

teams_6 = ['Crystal Palace', Keeper('Guiata', 8), Player('Ward', 8, 2, 5, 7), Player('Van Aanholt', 9, 8, 7, 7), 
Player('Tomkins', 7, 5, 5, 8), Player('Sakho', 8, 5, 5, 8), Player('Milivojevic', 8, 8, 4, 9), Player('McArthur', 8, 6, 5, 8),
Player('Zaha', 8, 8, 10, 3), Player('Townsend', 8, 8, 7, 5), Player('Benteke', 6, 3, 5, 4), Player('Ayew', 7, 6, 8, 4)]

teams_7 = ['Everton', Keeper('Pickford', 8), Player('Coleman', 8, 2, 7, 9), Player('Digne', 9, 8, 7, 7), 
Player('Keane', 8, 4, 5, 8), Player('Mina', 8, 5, 5, 8), Player('Gomes', 8, 4, 4, 8), Player('T. Davies', 8, 4, 4, 8),
Player('Bernard', 7, 7, 9, 3), Player('Walcott', 8, 6, 8, 5), Player('Richarlison', 7, 8, 7, 8), Player('Calvert-Lewin', 6, 8, 6, 8)]

teams_8 = ['Leicester', Keeper('Schmeichel', 9), Player('Pereira', 9, 8, 7, 9), Player('Chilwell', 9, 5, 5, 7), 
Player('Evans', 9, 5, 5, 9), Player('Soyuncu', 9, 3, 5, 9), Player('Ndidi', 8, 3, 3, 9), Player('Tielemans', 9, 8, 6, 7),
Player('H.Barnes', 8, 8, 8, 5), Player('Perez', 8, 8, 8, 5), Player('Vardy', 8, 10, 8, 8), Player('Iheanacho', 7, 7, 7, 4)]

teams_9 = ['Liverpool', Keeper('Alisson', 10), Player('Robertson', 9, 4, 7, 8), Player('Alexander-Arnold', 10, 8, 6, 7), 
Player('Van Dijk', 9, 4, 6, 10), Player('Gomez', 9, 2, 2, 9), Player('Fabinho', 9, 8, 8, 9), Player('Keita', 9, 6, 9, 8),
Player('Salah', 9, 9, 9, 2), Player('Mane', 9, 9, 9, 3), Player('Firmino', 9, 8, 9, 6), Player('Origi', 7, 7, 6, 3)]

teams_10 = ['Manchester City', Keeper('Ederson', 9), Player('Walker', 9, 2, 6, 8), Player('Mendy', 9, 5, 8, 6), 
Player('Laporte', 9, 6, 7, 9), Player('Stones', 8, 5, 5, 6), Player('Fernandinho', 9, 5, 7, 9), Player('D.Silva', 9, 8, 9, 5),
Player('De Bruyne', 10, 8, 9, 8), Player('Mahrez', 9, 9, 10, 6), Player('Sterling', 9, 9, 10, 6), Player('Jesus', 9, 8, 8, 4)]

teams_11 = ['Manchester United', Keeper('De Gea', 8), Player('Wan-Bissaka', 9, 3, 6, 9), Player('Shaw', 9, 3, 7, 7),
 Player('Maguire', 9, 4, 7, 10), Player('Lindelof', 9, 2, 6, 8), Player('McTominay', 9, 3, 3, 9),
 Player('Pogba', 10, 8, 9, 8), Player('Rashford', 8, 8, 9, 2), Player('Greenwood', 8, 10, 8, 3),
 Player('Martial', 9, 9, 10, 3), Player('Fernandes', 9, 9, 8, 4)]

teams_12 = ['Newcastle', Keeper('Dubravka', 8), Player('Yedlin', 7, 2, 8, 6), Player('Ritchie', 8, 7, 4, 8), 
Player('Lascelles', 7, 5, 5, 8), Player('Fernandez', 7, 5, 5, 8), Player('Shelvey', 9, 6, 4, 7), Player('Hayden', 7, 6, 7, 7),
Player('Saint-Maximin', 7, 8, 9, 3), Player('Almiron', 8, 7, 8, 3), Player('Joelinton', 6, 5, 6, 3), Player('Gayle', 6, 8, 5, 4)]

teams_13 = ['Norwich', Keeper('Krul', 6), Player('Aarons', 5, 2, 6, 6), Player('Lewis', 7, 2, 2, 6), 
Player('Klose', 6, 2, 5, 4), Player('Godfrey', 6, 2, 5, 8), Player('Tettey', 5, 2, 3, 6), Player('McLean', 5, 3, 4, 5),
Player('Hernandez', 5, 5, 4, 3), Player('Cantwell', 6, 4, 7, 3), Player('Buendia', 8, 5, 4, 2), Player('Pukki', 4, 8, 3, 4)]

teams_14 = ['Sheffield United', Keeper('Henderson', 9), Player('Basham', 8, 2, 5, 9), Player('Egan', 8, 4, 4, 9), 
Player('Connell', 8, 6, 5, 9), Player('Lundstram', 7, 6, 5, 7), Player('Berge', 8, 3, 3, 7), Player('Fleck', 9, 4, 5, 4),
Player('Baldock', 7, 5, 4, 8), Player('Stevens', 8, 6, 6, 8), Player('McBurnie', 6, 7, 4, 2), Player('McGoldrick', 7, 4, 6, 4)]

teams_15 = ['Southampton', Keeper('McCarthy', 8), Player('Walker-Peters', 7, 2, 7, 7), Player('Bertrand', 8, 7, 7, 8), 
Player('J. Stephens', 8, 6, 5, 9), Player('Bednarek', 8, 2, 4, 9), Player('Ward-Prowse', 9, 7, 6, 7), Player('Romeu', 8, 4, 5, 9),
Player('Armstrong', 9, 7, 7, 6), Player('Redmond', 8, 5, 9, 5), Player('Ings', 7, 10, 8, 4), Player('Adams', 5, 5, 5, 4)]

teams_16 = ['Tottenham', Keeper('Lloris', 9), Player('Aurier', 9, 5, 7, 7), Player('B. Davies', 9, 5, 5, 8), 
Player('D. Sanchez', 8, 4, 4, 9), Player('Alderweireld', 9, 4, 4, 9), Player('Sissoko', 9, 2, 7, 9), Player('Winks', 9, 2, 4, 9),
Player('Lo Celso', 9, 5, 6, 6), Player('Lucas', 8, 8, 8, 5), Player('Son', 9, 9, 10, 7), Player('Kane', 9, 10, 7, 6)]

teams_17 = ['Watford', Keeper('Foster', 8), Player('Kiko', 6, 2, 5, 5), Player('Masina', 7, 4, 4, 7), 
Player('Dawson', 7, 4, 5, 7), Player('Mariappa', 7, 2, 3, 7), Player('Capoue', 7, 2, 3, 7), Player('Doucoure', 9, 7, 8, 8),
Player('Sarr', 6, 8, 9, 3), Player('W. Hughes', 5, 4, 5, 5), Player('Deulofeu', 3, 7, 8, 7), Player('Deeney', 8, 8, 4, 7)]

teams_18 = ['West Ham', Keeper('Fabianski', 8), Player('Fredericks', 8, 5, 7, 6), Player('Cresswell', 7, 6, 5, 7), 
Player('Diop', 7, 3, 3, 7), Player('Ogbonna', 6, 2, 2, 7), Player('Rice', 9, 4, 2, 9), Player('Noble', 9, 4, 2, 8),
Player('Soucek', 7, 6, 5, 7), Player('Fornals', 9, 5, 7, 2), Player('Bowen', 7, 7, 6, 3), Player('Antonio', 7, 8, 8, 7)]

teams_19 = ['Wolves', Keeper('Rui Patricio', 8), Player('Boly', 6, 2, 5, 9), Player('Coady', 7, 4, 4, 8), 
Player('Saiss', 7, 6, 5, 8), Player('Doherty', 9, 6, 8, 7), Player('Jonny', 7, 4, 7, 7), Player('Neves', 9, 7, 5, 8),
Player('Mountinho', 9, 5, 5, 7), Player('Jota', 7, 7, 9, 4), Player('Traore', 6, 6, 10, 5), Player('Jimenez', 9, 9, 7, 5)]

# Store all teams in a list
total_teams =[teams_0, teams_1, teams_2, teams_3, teams_4, teams_5, teams_6, teams_7, teams_8,
teams_9, teams_10, teams_11, teams_12, teams_13, teams_14, teams_15, teams_16, teams_17, teams_18, teams_19]

"""
def select_team():
	global team_1
	global team_2
	for team in total_teams:
		print(team[0])
	print("\n")	
	active = True
	while active:	
		team_response = input("Type the name of the home team: ")
		for team in total_teams:
			if team_response.lower() == team[0].lower():
				team_1 = team
				print(f"The chosen home team is {team_1[0]}")
				active = False

	for team in total_teams:
		print(team[0])
	print("\n")			
	active = True
	while active:	
		team_response = input("Type the name of the away team: ")
		for team in total_teams:
			if team_response.lower() == team_1[0].lower():
				print("This team has already been chosen.")
				break
				
			elif team_response.lower() == team[0].lower():
				team_2 = team
				print(f"The chosen away team is {team_2[0]}")
				active = False

"""
