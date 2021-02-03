for bulls in range(1, 100):
    for cows in range(1, 100):
        for calves in range(1, 100):
            if (10 * bulls + 5 * cows + 0.5 * calves == 100) and (bulls + cows + calves == 100):
                print(f'bulls = {bulls}, cows = {cows}, calves = {calves}')
