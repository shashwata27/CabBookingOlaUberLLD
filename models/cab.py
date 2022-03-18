class Cab:
    def __init__(self,id,location,driverName,driverDetails={},isAvailable=True) -> None:
        self.id=id
        self.location=location
        self.driverName=driverName
        self.driverDetails=driverDetails
        self.isAvailable=isAvailable


    def getId(self):
        return self.id
    def setId(self,id):
        self.id=id

    def getLocation(self):
        return self.location
    def setLocation(self,location):
        self.location=location

    def getDriverName(self):
        return self.driverName
    def setDriverName(self,driverName):
        self.driverName=driverName

    def getDriverDetails(self):
        return self.driverDetails
    def setDriverDetails(self,driverDetails):
        self.driverDetails=driverDetails

    def getIsAvailable(self):
        return self.isAvailable
    def setIsAvailable(self,isAvailable):
        self.isAvailable=isAvailable