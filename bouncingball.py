def bouncing_ball(h, bounce, window):
    if h < 0 or (bounce < 0 or bounce >= 1) or window >= h:
        return -1
    rebounds = 0
    while h > window:
        rebounds += 1
        h = h * bounce
        if h < window:
            break
        rebounds += 1

    return rebounds


print(bouncing_ball(30, 0.66, 1.5))