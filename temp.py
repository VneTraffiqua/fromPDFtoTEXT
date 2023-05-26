
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
    print('Плательщик: ', user, )
    print(*inn.split(' '))
    tail_cursor_pos = split_text_tail.find('Имущество должника:\r') + len(
        'Имущество должника:\r'
    )
    tail_cursor_end_pos = split_text_tail.find('.\r', tail_cursor_pos)
    user_accounts = split_text_tail[tail_cursor_pos:tail_cursor_end_pos]
    user_accounts_elems = user_accounts.split('\r')
    for elem in user_accounts_elems:
        if elem[:4].isdigit():
            [print(account) for account in elem.split('. ')]

    tail_cursor_pos = split_text_tail.find('Реквизиты для перечисления задолженности:\r') + len(
        'Реквизиты для перечисления задолженности:\r'
    )
    tail_cursor_end_pos = split_text_tail.find('.', tail_cursor_pos)
    payment_info = split_text_tail[tail_cursor_pos:tail_cursor_end_pos]
    [print(row) for row in payment_info.split('; ')]


if __name__ == '__main__':
    document_path = './111.pdf'
    text = get_text_from_document(document_path)
    get_payment_info(text)


