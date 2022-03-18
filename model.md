models->

- rider

  - id
  - name

- cab

  - id
  - driverName
  - driverDetails
  - isAvailable
  - Location()

- trip

  - id
  - rider()
  - startLocation(location())
  - endLOcation
  - tripStatus
  - cab()
  - price

- location

  -x
  -y

services ->

- riderService

  - createRider

- cabService

  - createCab
  - updateCabLocation
  - updateCabAvailability

- tripService

  - trips(riderId,trip())
  - createTrip [riderBookingTrip]
  - endTrip

- locationService
  - createLocation
  - distance
