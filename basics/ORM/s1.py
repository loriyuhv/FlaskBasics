import models


Session = sessionmaker(bind=engine)
obj = models.Users(name="alex", extra="12345")