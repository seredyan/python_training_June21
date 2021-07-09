# -*- coding: utf-8 -*-

from model.contact import Contact


def test_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    added_contact = Contact(name="Ivan",
                               lastname="Ivanov", address="Russia",
                               landline="111", mobile="777", email="gmail")
    app.contact.create(added_contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(added_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#
# def test_next_new_contact(app):

#     app.contact.create(Contact(name="Peter",
#                                lastname="Petrov", address="Lenina St, 10-11\nVoronezh, Russia",
#                                landline="3333333", mobile="888888", email="petrov@mail.ru"))
#
#
#



