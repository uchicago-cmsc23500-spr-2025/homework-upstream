import psycopg2
import psycopg2.extras


class Boardgame:
    def __init__(self, g_id: int, name: str, avgscore: float, numvotes: int, 
            minplayers: int, maxplayers: int, 
            minplaytime: int, maxplaytime: int, designer=None):
        """
        Initialize a Boardgame object.

        Parameters:
        - g_id (int): The ID of the board game.
        - name (str): The name of the board game.
        - avgscore (float): The average score of the board game.
        - numvotes (int): The number of votes for the board game.
        - minplayers (int): The minimum number of players for the board game.
        - maxplayers (int): The maximum number of players for the board game.
        - minplaytime (int): The minimum playtime for the board game.
        - maxplaytime (int): The maximum playtime for the board game.
        - designer (str, optional): The designer of the board game.

        """
        self.id = g_id
        self.name = name
        self.avgscore = avgscore
        self.numvotes = numvotes
        self.minplayers = minplayers
        self.maxplayers = maxplayers
        self.minplaytime = minplaytime
        self.maxplaytime = maxplaytime

        self.designer = designer

    def __repr__(self) -> str:
        return f"Boardgame({self.name} ({self.id}))"

    def __hash__(self) -> int:
        return hash(self.id)


class Designer:
    def __init__(self, d_id: int, name: str, country: str):
        """
        Initializes a new instance of the Designer class.

        Args:
            d_id (int): The ID of the designer.
            name (str): The name of the designer.
            country (str): The country of the designer.
        """
        self.id = d_id
        self.name = name
        self.country = country

    def __repr__(self) -> str:
        return f"Designer({self.name} ({self.id}))"

    def __hash__(self) -> int:
        return hash(self.id)


class DBManager:
    def __init__(self, host, database, user, password):
            """ 
            Initialize a Database object.

            Args:
                host (str): The host name or IP address of the database server.
                database (str): The name of the database.
                user (str): The username for the database connection.
                password (str): The password for the database connection.
            """
            # TODO: Set up DB connection here
            raise NotImplementedError("TODO project sql") ### TODO

    def get_all_games(self) -> list[Boardgame]:
        """ Returns a list of all Boardgame objects. """
        #TODO: Complete this function
        raise NotImplementedError("TODO project sql") ### TODO


    def get_games_by_name(self, name) -> list[Boardgame]:
            """ Returns a list of Boardgame objects that match the given name. 
            The parameter `name` can be matched anywhere in boardgame's name, 
            case insensitive. 

            Args:
                name (str): The name to search for in the boardgame's name.

            Returns:
                list[Boardgame]: A list of Boardgame objects that match the given name.
            """
            games = []
            #TODO: Complete this function
            raise NotImplementedError("TODO project sql")


    def get_all_designers(self) -> list[Designer]:
            """Return a list of all Designer objects.

            Returns:
                list[Designer]: A list of all Designer objects.
            """
            designers = []
            # TODO: Complete this function
            raise NotImplementedError("TODO project sql")

    def get_games_by_designer(self, designer) -> list[Boardgame]:
            """ Return a list of Boardgame objects that match the given 
                designer name.

            Args:
                designer (str): The name of the designer to search for.

            Returns:
                list[Boardgame]: A list of Boardgame objects that match the 
                                 given designer name.

            """
            # TODO: Complete this function
            raise NotImplementedError("TODO project sql")

    def close(self) -> None:
         """
         Close the database connection
         """
         # TODO: Complete this function
         raise NotImplementedError("TODO project sql")