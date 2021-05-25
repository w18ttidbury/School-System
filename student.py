from enum import Enum

class punishmentType(Enum):
  DETENTION = 1,
  EXPULSION = 2

students = []

class Student:
  def __init__(self, uuid, name, dob, familyContacts):
    self.uuid = uuid
    self.name = name
    self.dob = dob
    self.familyContacts = familyContacts

  def getFamily(self):
    ret = {}
    for family in self.familyContacts:
      name, relation, phone, email, uuid = family.getAll()
      ret[uuid] = {
        "name": name,
        "relation": relation,
        "phone": phone,
        "email": email,
        "uuid": uuid
      }
    return ret

  def getAll(self):
    return self.name, self.dob, self.getFamily()
  
  def getUUID(self):
    return self.uuid

  def punish(self, type):
    print(".")

class FamilyContact:
  def __init__(self, uuid, name, relation, phone, email):
    self.uuid = uuid
    self.name = name
    self.relation = relation
    self.phone = phone
    self.email = email
  
  def getAll(self):
    return self.name, self.relation, self.phone, self.email, self.uuid

  def getUUID(self):
    return self.uuid
  
  def getName(self):
    return self.name
  def setName(self, name):
    self.name = name
    return self.name
  
  def getRelation(self):
    return self.relation
  def setRelation(self, relation):
    self.relation = relation
    return self.relation
  
  def getPhone(self):
    return self.phone
  def setPhone(self, phone):
    self.phone = phone
    return self.phone

  def getEmail(self):
    return self.email
  def setEmail(self, email):
    self.email = email
    return self.email