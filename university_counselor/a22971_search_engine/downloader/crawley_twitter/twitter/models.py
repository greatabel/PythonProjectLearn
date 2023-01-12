from crawley.persistance import Entity, UrlEntity, Field, Unicode

class twitterProducts(Entity):

    #add your table fields here
    title = Field(Unicode(2000))
