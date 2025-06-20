from app.extensions import db

building_amenity = db.Table('building_amenity',
    db.Column('building_id', db.Integer, db.ForeignKey('building.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenity.id'), primary_key=True)
)

building_heating = db.Table('building_heating',
    db.Column('building_id', db.Integer, db.ForeignKey('building.id'), primary_key=True),
    db.Column('heating_id', db.Integer, db.ForeignKey('heating.id'), primary_key=True)
)

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    square_footage = db.Column(db.Float)
    construction_year = db.Column(db.Integer)
    land_area = db.Column(db.Float)
    registration = db.Column(db.Boolean)
    rooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    parking = db.Column(db.Boolean)
    price = db.Column(db.Float)

    estate_type_id = db.Column(db.Integer, db.ForeignKey('estate_type.id'))
    offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'))
    city_part_id = db.Column(db.Integer, db.ForeignKey('city_part.id'))

    estate_type = db.relationship('EstateType', backref='buildings')
    offer = db.relationship('Offer', backref='buildings')
    city_part = db.relationship('CityPart', backref='buildings')

    amenities = db.relationship('Amenity', secondary=building_amenity, backref='buildings')
    heating_types = db.relationship('Heating', secondary=building_heating, backref='buildings')


class BuildingFloor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)
    floor_level = db.Column(db.Integer)
    floor_total = db.Column(db.Integer)

    building = db.relationship('Building', backref='floors')
