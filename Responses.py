from datetime import datetime

def sample_responses(input_text):
	user_message = str(input_text).lower()


	if user_message in ("hello","hi","kire",'good morning'):
		return "Hmm bol🙃"

	if user_message in ("kichu na","kichuna","hmm",'ok','hmmm','hm'):
		return "Meyeder moto reply dish ken?"

	if user_message in ("rishad"):
		return "Luccha public, er kotha bolbi na"

	if user_message in ('labu'):
		return "Shroud lite, veja pussy(biral)"

	if user_message in ('amake chinis?','amake chinis'):
		return "Naam bol dekh chini kina"

	if user_message in ('kibria','nawab'):
		return "premik chele, world class coder"

	if user_message in ('shakib','shanto'):
		return "Amar creator, eka public, valo manush"

	if user_message in ('vai','ki bolbo','ki bolbo?'):
		return "Hmm bolen vaijan ki bolben"

	if user_message in ('shakib','shanto'):
		return "Amar creator, eka public, valo manush"

	if user_message in ('shafiq'):
		return "Creative Cloud"

	if user_message in ('valo lagena','vallagena'):
		return "Meyeder moto kotha"

	if user_message in ('hasasasa','hasasa','hasa'):
		return "Eta shanto r labur bepar, tui k?"

	if user_message in ("kichu na","kichuna","hmm",'ok','hmmm','hm','ki'):
		return "Meyeder moto reply dish ken?"

	if user_message in ("ki parish tui?","ki parish tui","tui ki parish",'ability ki tor','ability ki tor?','ki ki parish tui?','ki ki parish tui'):
		return "Early stage development a achi, apatoto normal kotha bolte pari, depression katate pari, prem er advice dite pari etc."

	if user_message in ("k tui","ke tui","tui k",'tor shomporke bol','who are you?','ke banaiche toke?','ke banaiche toke','ke baniyeche toke','ke baniyeche toke?'):
		return "Ami Mokhles bhai, basha telegram e, Shanto banaiche amake"

	if user_message in ("amio","me too","same",'hmm amio'):
		return "Mil ache amader"

	if user_message in ("porashona","porashona valo lagena","porashona valo lage na"):
		return "Mil ache amader, ki r kora"

	if user_message in ("ki korish","korish ki","ki korish?","ki korish ekhon?"):
		return "Telegram a er baranday shuye theke mobile chapi, tui?"

	if user_message in ("kemon achis","kemon achis?","ki khobor?",
		"valo achis?","dinkal kemon jay?","valo achis",'ki khobor'):
		return "Ei achi kono rokom, Tui to valo nai jani, taw bol kemon achis?"

	if user_message in ("alhamdulillah","valo","Hmm valo","fine","valo, thanks",'depression'):
		return "Valo thakbi, kharap theke lav ki bol duidiner duniyay"


	if user_message in ("time", "time?","shomoy bol", "koyta baje?"):
		now = datetime.now()
		date_time = now.strftime("%d/%m/%y , %H:%M:%S")

		return str(date_time)

	if user_message in ("x","ekta x de","porn",'sex video','valo x de','sex'):
		return "Chi Chi, manush ho shomoy thakte"


	if user_message in ("prem korbo","meye nai","hahakar",'prem','valobasha','meye','suicide korbo','depression kemne katash?'):
		return "Eta shon pagla: https://www.youtube.com/watch?v=FP5F6DdDl88"

	if user_message in ("bye","bye valo thak","valo thak",'good night'):
		return "Ok bye, Tui o valo thak🙃"

	return "Kichui bujhlam na bara ki bolli 🙁, Takla vashay bolle kintu bujhbona, R amaar sathe TUI kore kotha bol"

