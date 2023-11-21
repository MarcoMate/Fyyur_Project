from app2 import db, Venue, Artist, Show

"""
name = "The Musical Hop"
genres = ["Jazz", "Reggae", "Swing", "Classical", "Folk"]
address = "1015 Folsom Street"
city = "San Francisco"
state = "CA"
phone = "123-123-1234"
website = "https://www.themusicalhop.com"
facebook_link = "https://www.facebook.com/TheMusicalHop"
seeking_talent = True
seeking_description= "We are on the lookout for a local artist to play every two weeks. Please call us."
image_link = "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"
past_show_count = 1
upcoming_show_count = 0
venue1 = Venue(name=name, genres=genres, address=address, city=city, state=state,phone=phone, website=website,
               facebook_link=facebook_link, seeking_talent=seeking_talent, seeking_description=seeking_description,
               image_link=image_link, past_show_count=past_show_count,upcoming_show_count=upcoming_show_count)

name = "The Dueling Pianos Bar"
genres = ["Classical", "R&B", "Hip-Hop"]
address = "335 Delancey Street"
city = "New York"
state = "NY"
phone = "914-003-1132"
website = "https://www.theduelingpianos.com"
facebook_link = "https://www.facebook.com/theduelingpianos"
seeking_talent = False
image_link = "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"
past_show_count = 0
upcoming_show_count = 0
venue2 = Venue(name=name, genres=genres, address=address, city=city, state=state,phone=phone, website=website,
               facebook_link=facebook_link, seeking_talent=seeking_talent,
               image_link=image_link, past_show_count=past_show_count,upcoming_show_count=upcoming_show_count)

name = "Park Square Live Music & Coffee"
genres = ["Rock n Roll", "Jazz", "Classical", "Folk"]
address = "34 Whiskey Moore Ave"
city = "San Francisco"
state = "CA"
phone = "415-000-1234"
website = "https://www.parksquarelivemusicandcoffee.com"
facebook_link = "https://www.facebook.com/ParkSquareLiveMusicAndCoffee"
seeking_talent = False
image_link = "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80"
past_show_count = 1
upcoming_show_count = 1
venue3 = Venue(name=name, genres=genres, address=address, city=city, state=state,phone=phone, website=website,
               facebook_link=facebook_link, seeking_talent=seeking_talent,
               image_link=image_link, past_show_count=past_show_count,upcoming_show_count=upcoming_show_count)


#Artists
name = "Guns N Petals"
genres = ["Rock n Roll"]
city = "San Francisco"
state = "CA"
phone = "26-123-5000"
website = "https://www.gunsnpetalsband.com"
facebook_link = "https://www.facebook.com/GunsNPetals"
seeking_venue = True
seeking_description= "Looking for shows to perform at in the San Francisco Bay Area!"
image_link = "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"
past_shows_count = 1
upcoming_shows_count = 0
artist1 = Artist(name=name, genres=genres, city=city, state=state,phone=phone, website=website,
               facebook_link=facebook_link, seeking_venue=seeking_venue, seeking_description=seeking_description,
               image_link=image_link, past_shows_count=past_shows_count,upcoming_shows_count=upcoming_shows_count)

name = "Matt Quevedo"
genres = ["Jazz"]
city = "New York"
state = "NY"
phone = "300-400-5000"
facebook_link = "https://www.facebook.com/mattquevedo923251523"
seeking_venue = False
image_link = "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80"
past_shows_count = 1
upcoming_shows_count = 0
artist2 = Artist(name=name, genres=genres, city=city, state=state,phone=phone,
               facebook_link=facebook_link, seeking_venue=seeking_venue,
               image_link=image_link, past_shows_count=past_shows_count,upcoming_shows_count=upcoming_shows_count)

name = "The Wild Sax Band"
genres = ["Jazz", "Classical"]
city = "San Francisco"
state = "CA"
phone = "432-325-5432"
seeking_venue = False
image_link = "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80"
past_shows_count = 0
upcoming_shows_count = 3
artist3 = Artist(name=name, genres=genres, city=city, state=state,phone=phone,
               seeking_venue=seeking_venue,
               image_link=image_link, past_shows_count=past_shows_count,upcoming_shows_count=upcoming_shows_count)



#Shows
start_time = "2019-05-21T21:30:00.000Z"
show1 = Show(start_time=start_time)
show1.artist = artist1
show1.venue = venue1

start_time = "2019-05-21T21:30:00.000Z"
show2 = Show(start_time=start_time)
show2.artist = artist2
show2.venue = venue3

start_time = "2019-05-21T21:30:00.000Z"
show3 = Show(start_time=start_time)
show3.artist = artist3
show3.venue = venue3

start_time = "2035-04-01T20:00:00.000Z"
show4 = Show(start_time=start_time)
show4.artist = artist3
show4.venue = venue3

start_time = "2035-04-08T20:00:00.000Z"
show4 = Show(start_time=start_time)
show4.artist = artist3
show4.venue = venue3

start_time = "2035-04-15T20:00:00.000Z"
show5 = Show(start_time=start_time)
show5.artist = artist3
show5.venue = venue3








db.session.add_all([venue1, venue2, venue3, artist1, artist2, artist3])
db.session.commit()
db.session.close()"""

from datetime import datetime

past_shows = db.session.query(Show, Venue, Artist).join(Venue).filter(Show.venue_id==Venue.id).join(Artist).filter(Show.artist_id==Artist.id).all()

print(past_shows)
temp_shows = []
for show in past_shows:
    temp = {}
    temp["venue_name"] = show[1].name
    temp["venue_id"] = show[0].venue_id
    temp["venue_image_link"] = show[1].image_link
    temp["start_time"] = show[0].start_time.strftime("%m/%d/%Y, %H:%M:%S")
    temp["artist_name"] = show[2].name


    temp_shows.append(temp)

print(temp_shows)

"""SELECT shows.id AS shows_id, shows.start_time AS shows_start_time, shows.artist_id AS shows_artist_id, shows.venue_id AS shows_venue_id, shows.upcoming AS shows_upcoming, "Venue".id AS "Venue_id", "Venue".name AS "Venue_name", "Venue".city AS "Venue_city", "Venue".state AS "Venue_state", "Venue".address AS "Venue_address", "Venue".phone AS "Venue_phone", "Venue".image_link AS "Venue_image_link", "Venue".facebook_link AS "Venue_facebook_link", "Venue".genres AS "Venue_genres", "Venue".website AS "Venue_website", "Venue".seeking_talent AS "Venue_seeking_talent", "Venue".seeking_description AS "Venue_seeking_description", "Venue".upcoming_show_count AS "Venue_upcoming_show_count", "Venue".past_show_count AS "Venue_past_show_count" 
FROM shows JOIN "Venue" ON "Venue".id = shows.venue_id 
WHERE shows.artist_id = "Venue".id"""

