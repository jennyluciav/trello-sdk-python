from trello import Trello
import argparse
import os
from dotenv import load_dotenv

def main():

	# Initialize parser
	parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

	# Adding optional argument
	parser.add_argument("-b", "--board", help="Trello board", required=True)
	parser.add_argument("-l", "--list", help="List inside the board", required=True)
	parser.add_argument("-cn", "--cardname", help="New card name", required=True)
	parser.add_argument("-lb", "--labels", help="Add the labels for your new card", required=True, nargs='+')
	parser.add_argument("-c", "--comment", help="Add a comment for your new card", required=True)

	# Read arguments from command line
	args = parser.parse_args()
	load_dotenv()
	
	if args.board and args.list and args.labels and args.comment:
		api_key = os.getenv('API_KEY')
		api_token = os.getenv('API_TOKEN')
		username = os.getenv('USER')
		try:
			trello = Trello(api_key, api_token, username)
			trello.create_card(args.board, args.list, args.cardname, args.labels)
			trello.create_comment(args.comment)
			print("New Card created succesfully!")
		except Exception as e:
			print("New Card can't be created")
			print("Error:", e)

if __name__ == "__main__":
    main()
