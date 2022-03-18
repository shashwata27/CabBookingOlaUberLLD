import sys
sys.path.append(r'D:\Projects\CabBookingLLD')

from controllers.cab_controller import CabController
from controllers.rider_controller import RiderController
from controllers.trip_controller import TripController
from controllers.location_controller import LocationController

cabController=CabController()
riderController=RiderController()
tripController=TripController()
locationController=LocationController()

loc1=locationController.createLocation(1,1)
loc2=locationController.createLocation(2,2)
loc3=locationController.createLocation(2,1)
loc4=locationController.createLocation(20,25)
loc5=locationController.createLocation(0,15)
loc0=locationController.createLocation(0,0)
loc100=locationController.createLocation(100,100)




cab1=cabController.registerCab("cab1",loc4,"samal")
cab2=cabController.registerCab("cab2",loc1,"jodi")
cab3=cabController.registerCab("cab3",loc2,"kam")
cab4=cabController.registerCab("cab4",loc3,"gan")
cab5=cabController.registerCab("cab5",loc5,"que")

ride1=riderController.registerRider('rider1','shash')

#checking if cabs are getting marked as inProg and Finished
trip=tripController.createTrip('trip1',ride1,loc0,loc100)
print(trip)
trip2=tripController.createTrip('trip2',ride1,loc0,loc100)
print(trip2)
tripController.endTrip(trip)
print(trip)
trip3=tripController.createTrip('trip3',ride1,loc0,loc100)
print(trip3)

tripController.endTrip(trip2)
tripController.endTrip(trip3)

# checking if location updates
cabController.updateLocation(cab2,loc100)
trip4=tripController.createTrip('trip4',ride1,loc0,loc100)
print(trip4)

print()
print("USer History")
tp=tripController.allTripsByUsers('rider1')
for x in tp:
    print(x)







