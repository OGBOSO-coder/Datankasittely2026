import copy


def mask(people):
    """Mask emails and phone numbers:

    - keep domain part of email, mask local part
    - keep last 2 digits of phone number, mask the rest with asterisks
    - return same datastructure with masked data without mutating original
    """
    # Otetaan syväkopio, jotta alkuperäisen users-listan tiedot eivät muutu
    masked_people = copy.deepcopy(people)

    for person in masked_people:
        person["crypted_name"] = person["name"][0] + "*" * (len(person["name"]) - 1)
        del person["name"]
        person["crypted_username"] = person["username"][0] + "*" * (len(person["username"]) - 1)
        del person["username"]
        # Sähköpostin maskaus
        email = person.get('email', '')
        if '@' in email:
            local_part, domain_part = email.split('@', 1)
            person['email'] = ('*' * len(local_part)) + '@' + domain_part

        # Puhelinnumeron maskaus (säilytetään 2 viimeistä merkkiä)
        phone = str(person.get('phone', ''))
        if len(phone) > 4:
            person['phone'] = ('*' * (len(phone) - 4)) + phone[-4:]
        else:
            person['phone'] = '**'

    return masked_people