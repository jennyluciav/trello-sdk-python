# Trello Python App

1. In .env file, update API_KEY, API_TOKEN and USERNAME values with your respective [Trello credentials](https://trello.com/app-key)
2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages needed to use Trello Python App.
```bash
pip install -r requeriments.txt
```

## Usage
Run the command and arguments below to add a Trello card with labels and a comment to the X column of board Y.
```bash
python main.py --board "Y" --list "X" --cardname "MyNewCard" --labels tag --comment "MyComment"
```
Aditionally you can add more than one label for your new card:
```bash
python main.py --board "Y" --list "X" --cardname "MyNewCard" --labels tag1 tag2 tag3 --comment "MyComment"
```
You can also review and use the main functions: **create_card** and **create_comment** among other complementary functions. **Important:**  If the board or list doesn't exists they will be created.
```python
import trello

trello = Trello(api_key, api_token, username)
trello.create_card(board, list, cardname, labels) # returns a new card
trello.create_comment(comment) # add a comment to the card
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Next steps
What do I hope to accomplish in the next version? Add new cards from a google sheets file or an excel. Also clone boards and add new lists and cards to this cloned board.

## License
[MIT](https://choosealicense.com/licenses/mit/)