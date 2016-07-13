from tim_app.models import Good
def create():
  w = Good(goodName = "water",unit = "liter", description = "wet")
  w.save()
  f = Good(goodName = "food",unit = "meals", description = "dry")
  f.save()
  c = Good(goodName = "clothes",unit = "people", description = "warm")
  c.save()
  fa = Good(goodName = "woundcare",unit = "kits", description = "cold")
  fa.save()
  a = Good(goodName = "accomodation",unit = "people", description = "big")
  a.save()
  m = Good(goodName = "other",unit = "none", description = "other")
  m.save()