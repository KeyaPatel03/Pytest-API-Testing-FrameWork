end_point_pet = "/v2/pet/"
end_point_user = "/v2/user/"
end_point_store = "/v2/store/order/"

end_point = 0
def end_point_request(data, key, response):
    global end_point
    if key == "id":
        for i in data.keys():
            if i == key:
                end_point = response.get(i)
                break
        return end_point
    else:
        for i in data.keys():
            if i == key:
                end_point = data.get(i)
                break
        return end_point


