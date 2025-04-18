from pet import Pet

def main():
    # Create a pet
    my_pet = Pet("Lulu")
    
    print("Initial Status")
    my_pet.get_status()
    
    print("\n Testing eat()")
    my_pet.eat()
    my_pet.get_status()
    
    print("\n Testing play()")
    my_pet.play()
    my_pet.get_status()
    
    print("\n Testing sleep()")
    my_pet.sleep()
    my_pet.get_status()
    
    print("\n Testing play() when tired")
    for _ in range(4):  # Play until tired
        my_pet.play()
    my_pet.get_status()
    
    print("\n Testing training")
    my_pet.train("sit")
    my_pet.train("roll over")
    my_pet.train("shake hands")
    my_pet.show_tricks()
    
    print("\n Final Status")
    my_pet.get_status()

if __name__ == "__main__":
    main()