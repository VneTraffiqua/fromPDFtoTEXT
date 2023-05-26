import aspose.words as aw


def get_text_from_document(path):
    document = aw.Document(path)
    return document.get_text()


def get_payment_info(all_text):
    split_text_head, split_text_tail, *garbage = all_text.split('УСТАНОВИЛ:')
    head_cursor_pos = split_text_head.find('(тип должника: физическое лицо): ') + len(
        '(тип должника: физическое лицо): '
    )
    head_cursor_pos = split_text_head.find('(тип должника: физическое лицо): ') + len(
        '(тип должника: физическое лицо): '
    )
    user, inn, all_info = split_text_head[head_cursor_pos:].split(', ', 2)
    tail_cursor_pos = split_text_tail.find('Имущество должника:\r') + len(
        'Имущество должника:\r'
    )
    tail_cursor_end_pos = split_text_tail.find('.\r', tail_cursor_pos)
    user_accounts = split_text_tail[tail_cursor_pos:tail_cursor_end_pos]
    user_accounts_elems = user_accounts.split('\r')
    user_bank_accounts = []
    for elem in user_accounts_elems:
        if elem[:4].isdigit():
            user_bank_accounts.append(elem)

    tail_cursor_pos = split_text_tail.find('Реквизиты для перечисления задолженности:\r') + len(
        'Реквизиты для перечисления задолженности:\r'
    )
    tail_cursor_end_pos = split_text_tail.find('.', tail_cursor_pos)
    payment_info = split_text_tail[tail_cursor_pos:tail_cursor_end_pos]
    row_payment_info = []
    [row_payment_info.append(row) for row in payment_info.split('; ')]

    return user, inn, user_bank_accounts, row_payment_info


class Payment:

    def __init__(self, user, inn, user_bank_accounts, row_payment_info):
        self.user = user
        self.inn = inn
        self.user_bank_accounts = user_bank_accounts
        self.row_payment_info = row_payment_info

    def __str__(self):
        return f'{self.user}, {self.inn}, {self.user_bank_accounts}, {self.row_payment_info}'


if __name__ == '__main__':
    document_path = './111.pdf'
    text = get_text_from_document(document_path)
    info = get_payment_info(text)
    print(Payment(*info))
