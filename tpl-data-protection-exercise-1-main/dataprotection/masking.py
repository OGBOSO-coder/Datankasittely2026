def mask(people):
    """
    TODO: Mask emails and phone numbers:
    - keep domain part of email, mask local part
    - keep last 2 digits of phone number, mask the rest with asterisks
    - return same datastructure with masked data
    """
    for person in people:
        email = person['email']
        local_part, domain_part = email.split('@')
        masked_local_part = '*' * len(local_part)
        person['email'] = masked_local_part + '@' + domain_part

        phone = person['phone']
        masked_phone = '*' * (len(phone) - 2) + phone[-2:]
        person['phone'] = masked_phone
    
    return people