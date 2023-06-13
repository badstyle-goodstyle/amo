import csv
import random
import os


class Character:
    def __init__(self, strength, agility, magic, vitality, character_class):
        self.strength = strength
        self.agility = agility
        self.magic = magic
        self.vitality = vitality
        self.character_class = character_class

    def __str__(self):
        return f"Class: {self.character_class}, Strength: {self.strength}, Agility: {self.agility}, " \
               f"Magic: {self.magic}, Vitality: {self.vitality}"


def add_noise(value, noise_range):
    noise = random.randint(-noise_range, noise_range)
    return max(0, min(value + noise, 18))


def create_random_character():
    classes = ['Warrior', 'Archer', 'Mage']
    character_class = random.choice(classes)

    if character_class == 'Warrior':
        strength = random.randint(12, 15)
        agility = random.randint(5, 8)
        magic = random.randint(1, 4)
        vitality = random.randint(12, 15)

    elif character_class == 'Archer':
        strength = random.randint(5, 8)
        agility = random.randint(12, 15)
        magic = random.randint(1, 4)
        vitality = random.randint(12, 15)

    else:  # character_class == 'Mage'
        strength = random.randint(1, 4)
        agility = random.randint(5, 8)
        magic = random.randint(12, 15)
        vitality = random.randint(12, 15)

    total_points = strength + agility + magic + vitality
    stat_points = 20

    coefficient = stat_points / total_points

    strength = int(strength * coefficient)
    agility = int(agility * coefficient)
    magic = int(magic * coefficient)
    vitality = int(vitality * coefficient)

    strength = add_noise(strength, 2)
    agility = add_noise(agility, 2)
    magic = add_noise(magic, 2)
    vitality = add_noise(vitality, 2)

    return Character(strength, agility, magic, vitality, character_class)


def create_characters(number_of_characters):
    characters = []
    for _ in range(number_of_characters):
        characters.append(create_random_character())
    return characters


if __name__ == '__main__':
    characters = create_characters(100)
    random.shuffle(characters)

    split_ratio = 0.8  # 80% for training, 20% for testing
    split_index = int(len(characters) * split_ratio)
    train_data = characters[:split_index]
    test_data = characters[split_index:]

    # Create "train" and "test" folders if they don't exist
    if not os.path.exists('train'):
        os.makedirs('train')
    if not os.path.exists('test'):
        os.makedirs('test')

    train_file = os.path.join('train', 'train_characters.csv')
    test_file = os.path.join('test', 'test_characters.csv')

    with open(train_file, mode='w', newline='') as train_file:
        writer = csv.writer(train_file)
        writer.writerow(['Class', 'Strength', 'Agility', 'Magic', 'Vitality'])

        for character in train_data:
            writer.writerow([character.character_class, character.strength, character.agility,
                             character.magic, character.vitality])

    with open(test_file, mode='w', newline='') as test_file:
        writer = csv.writer(test_file)
        writer.writerow(['Class', 'Strength', 'Agility', 'Magic', 'Vitality'])

        for character in test_data:
            writer.writerow([character.character_class, character.strength, character.agility,
                             character.magic, character.vitality])

    print('Train data saved in train/train_characters.csv')
    print('Test data saved in test/test_characters.csv')
