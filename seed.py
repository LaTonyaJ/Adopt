from models import Pet, db
from app import app

db.drop_all()
db.create_all()

spike = Pet(name='spike', species='dog', age='2',
            photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT36OGUq8X23zUYSRF3TEcQCcZbxdZvIphwcQ&usqp=CAU')


stan = Pet(name='stan', species='cat', age='5',
           photo_url='https://i.guim.co.uk/img/media/8a13052d4db7dcd508af948e5db7b04598e03190/0_294_5616_3370/master/5616.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=bcaa4eed2c1e6dab61c41a61e41433d9')

db.session.add(spike)
db.session.add(stan)
db.session.commit()
