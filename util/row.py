# ----------------------------------------------------------------------------------------------------------------------


class Row:

    UP = 0
    LEFT = 1
    DIAG = 2
    NONE = 3

    UP_AND_LEFT_AND_DIAG = 4
    UP_AND_LEFT = 5
    UP_AND_DIAG = 6
    LEFT_AND_DIAG = 7

    row_dic = {
        0: u"\u2191",
        1: u"\u2190",
        2: u"\u2196",
        3: " "
    }

    @staticmethod
    def get(row_type):
        string = Row.row_dic[row_type]
        return string

# ----------------------------------------------------------------------------------------------------------------------
