const {contacts}=data=require('./addressbook.json');

Object.entries(contacts).forEach(([key, value]) => console.log(key, value))

Object.keys(contacts).forEach(key =>console.log(key, data.contacts[key]));

for (let key in contacts) {
    if (data.contacts.hasOwnProperty(key)) {
        console.log(key, data.contacts[key]);
    }
}

// node main.js