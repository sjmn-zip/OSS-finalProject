import folium as f

def HTMLmaker(y, x, name):
    show_marker = False

    if x is None or y is None:
        location = [37.56682420267543, 126.978652258823] #seoul city hall
        zoom = 12
    else:
        if name is None:
            name = "보관 장소"
        show_marker = True
        location = [y , x]
        zoom = 18

    m = f.Map(location= location, zoom_start= zoom)
    if show_marker:
        f.Marker(location= location, tooltip= name).add_to(m)

    return m.get_root().render()


#m= f.Map(location=[37.56682420267543, 126.978652258823], zoom_start= 15)
#m.save("test.html")


    

