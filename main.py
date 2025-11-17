# Working with Sets 
from pyscript import display

club_Basketball = {"Seth", "Tax", "Koby", "Manuel"}
club_Volleyball = {"Enzo", "Ishan", "Manuel", "Vito"}

in_at_least_one = club_Basketball | club_Volleyball
in_both = club_Basketball & club_Volleyball
only_first = club_Basketball - club_Volleyball
only_second = club_Volleyball - club_Basketball
exactly_one = club_Basketball ^ club_Volleyball

display("Club Basketball: " + str(club_Basketball), target="output")
display("Club Volleyballl: " + str(club_Volleyball), target="output")
display("Students in at least one club: " + str(in_at_least_one), target="output")
display("Students in both clubs: " + str(in_both), target="output")
display("Students only in Club Basketball: " + str(only_first), target="output")
display("Students only in Club Volleyball: " + str(only_second), target="output")
display("Students in exactly one club: " + str(exactly_one), target="output")