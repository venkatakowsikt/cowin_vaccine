from cowin_api import CoWinAPI


def display_centers(centers):
    for center in centers:
        print("Name: ", center['name'])
        print("Address:", center["address"])
        print("Block Name: ", center["block_name"])
        print("Pin code: ", center["pincode"])
        print("District Name:", center["district_name"])
        print("Pincode:", center["pincode"])
        print("Timings: ", center["from"], " To ", center["to"])
        print("Fee Type: ", center["fee_type"])
        flag = False
        for j in center["sessions"]:
            if(j["available_capacity"] != 0):
                flag = True
                print("\nDate: ", j["date"])
                print("Available Capacity: ", j["available_capacity"])
                print("Minimun Age Limit: ", j["min_age_limit"])
                print("Vaccine Name: ", j["vaccine"])
                print("Time Slots: ", j["slots"])
        if(not flag):
            print("No Available Slots")
        print("----------------------------------------------------")


def by_district(district, date, min_age):
    centers = CoWinAPI().get_availability_by_district(
        district, min_age)["centers"]
    display_centers(centers)


def by_district(district, min_age):
    centers = CoWinAPI().get_availability_by_district(
        district, min_age)["centers"]
    display_centers(centers)


def by_pincode(pincode, date, min_age):
    centers = CoWinAPI().get_availability_by_pincode(
        pincode, min_age)["centers"]
    display_centers(centers)


def by_pincode(pincode, min_age):
    centers = CoWinAPI().get_availability_by_pincode(
        pincode, min_age)["centers"]
    display_centers(centers)

# states = cowin.get_states()['states']
# for state in states:
#     print(state["state_id"], " ", state["state_name"])


state = 16  # Karnataka

# dis = cowin.get_districts(state)['districts']
# for i in dis:
#     print(i['district_id'], " ", i['district_name'])

dist1 = "276"  # Bangalore rural
dist2 = "265"  # Bangalore urban
dist3 = "294"  # BBMP

min_age = "18"  # either 18 or 45

by_district(dist3, min_age)
# by_pincode("560030", "18")
