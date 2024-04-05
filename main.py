import threading
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
from PyQt6.QtCore import QTimer
import time

Form, Window = uic.loadUiType("ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
errorWindow = QMessageBox()



cards = [
    {"name": "skeletons", "image_path": "img/skeletons.png", "elixir_cost": 1},
    {"name": "snow_spirits", "image_path": "img/snow_spirits.png", "elixir_cost": 1},
    {"name": "warmth_spell", "image_path": "img/warmth_spell.png", "elixir_cost": 1},
    {"name": "electrospirit", "image_path": "img/electrospirit.png", "elixir_cost": 1},
    {"name": "goblins", "image_path": "img/goblins.png", "elixir_cost": 2},
    {"name": "goblin_archer", "image_path": "img/goblin_archer.png", "elixir_cost": 2},
    {"name": "bats", "image_path": "img/bats.png", "elixir_cost": 2},
    {"name": "zap", "image_path": "img/zap.png", "elixir_cost": 2},
    {"name": "snowball", "image_path": "img/snowball.png", "elixir_cost": 2},
    {"name": "bomber", "image_path": "img/bomber.png", "elixir_cost": 2},
    {"name": "knight", "image_path": "img/knight.png", "elixir_cost": 3},
    {"name": "archers", "image_path": "img/archers.png", "elixir_cost": 3},
    {"name": "minion", "image_path": "img/minion.png", "elixir_cost": 3},
    {"name": "goblin_gang", "image_path": "img/goblin_gang.png", "elixir_cost": 3},
    {"name": "skeleton_balloon", "image_path": "img/skeleton_balloon.png", "elixir_cost": 3},
    {"name": "firecracker", "image_path": "img/firecracker.png", "elixir_cost": 3},
    {"name": "chaos_cannon", "image_path": "img/chaos_cannon.png", "elixir_cost": 3},
    {"name": "order_volley", "image_path": "img/order_volley.png", "elixir_cost": 3},
    {"name": "royal_delivery", "image_path": "img/royal_delivery.png", "elixir_cost": 3},
    {"name": "building_mortar", "image_path": "img/building_mortar.png", "elixir_cost": 4},
    {"name": "building_tesla", "image_path": "img/building_tesla.png", "elixir_cost": 4},
    {"name": "skeletondragon", "image_path": "img/skeletondragon.png", "elixir_cost": 4},
    {"name": "barbarians", "image_path": "img/barbarians.png", "elixir_cost": 5},
    {"name": "minion_horde", "image_path": "img/minion_horde.png", "elixir_cost": 5},
    {"name": "rascals", "image_path": "img/rascals.png", "elixir_cost": 5},
    {"name": "royalgiant", "image_path": "img/royalgiant.png", "elixir_cost": 6},
    {"name": "angry_barbarian", "image_path": "img/angry_barbarian.png", "elixir_cost": 6},
    {"name": "royal_recruits", "image_path": "img/royal_recruits.png", "elixir_cost": 6},
    {"name": "healspirit", "image_path": "img/healspirit.png", "elixir_cost": 1},
    {"name": "icegolem", "image_path": "img/icegolem.png", "elixir_cost": 2},
    {"name": "mega_minion", "image_path": "img/mega_minion.png", "elixir_cost": 3},
    {"name": "blowdart_goblin", "image_path": "img/blowdart_goblin.png", "elixir_cost": 3},
    {"name": "elixir_golem", "image_path": "img/elixir_golem.png", "elixir_cost": 3},
    {"name": "tombstone", "image_path": "img/tombstone.png", "elixir_cost": 3},
    {"name": "earthquake", "image_path": "img/earthquake.png", "elixir_cost": 3},
    {"name": "valkyrie", "image_path": "img/valkyrie.png", "elixir_cost": 4},
    {"name": "musketeer", "image_path": "img/musketeer.png", "elixir_cost": 4},
    {"name": "minipekka", "image_path": "img/minipekka.png", "elixir_cost": 4},
    {"name": "hog_rider", "image_path": "img/hog_rider.png", "elixir_cost": 4},
    {"name": "battle_ram", "image_path": "img/battle_ram.png", "elixir_cost": 4},
    {"name": "zappies", "image_path": "img/zappies.png", "elixir_cost": 4},
    {"name": "flying_machine", "image_path": "img/flying_machine.png", "elixir_cost": 4},
    {"name": "battle_healer", "image_path": "img/battle_healer.png", "elixir_cost": 4},
    {"name": "bomb_tower", "image_path": "img/bomb_tower.png", "elixir_cost": 4},
    {"name": "firespirit_hut", "image_path": "img/firespirit_hut.png", "elixir_cost": 4},
    {"name": "goblin_cage", "image_path": "img/goblin_cage.png", "elixir_cost": 4},
    {"name": "fire_fireball", "image_path": "img/fire_fireball.png", "elixir_cost": 4},
    {"name": "giant", "image_path": "img/giant.png", "elixir_cost": 5},
    {"name": "wizard", "image_path": "img/wizard.png", "elixir_cost": 5},
    {"name": "royal_hog", "image_path": "img/royal_hog.png", "elixir_cost": 5},
    {"name": "fire_furnace", "image_path": "img/fire_furnace.png", "elixir_cost": 5},
    {"name": "building_inferno", "image_path": "img/building_inferno.png", "elixir_cost": 5},
    {"name": "barbarian_hut", "image_path": "img/barbarian_hut.png", "elixir_cost": 6},
    {"name": "building_elixir_collector", "image_path": "img/building_elixir_collector.png", "elixir_cost": 6},
    {"name": "rocket", "image_path": "img/rocket.png", "elixir_cost": 6},
    {"name": "three_musketeers", "image_path": "img/three_musketeers.png", "elixir_cost": 9},
    {"name": "mirror", "image_path": "img/mirror.png", "elixir_cost": 1},
    {"name": "rage", "image_path": "img/rage.png", "elixir_cost": 2},
    {"name": "barb_barrel", "image_path": "img/barb_barrel.png", "elixir_cost": 2},
    {"name": "wallbreaker", "image_path": "img/wallbreaker.png", "elixir_cost": 2},
    {"name": "skeleton_horde", "image_path": "img/skeleton_horde.png", "elixir_cost": 3},
    {"name": "skeleton_warriors", "image_path": "img/skeleton_warriors.png", "elixir_cost": 3},
    {"name": "goblin_barrel", "image_path": "img/goblin_barrel.png", "elixir_cost": 3},
    {"name": "tornado", "image_path": "img/tornado.png", "elixir_cost": 3},
    {"name": "copy", "image_path": "img/copy.png", "elixir_cost": 3},
    {"name": "baby_dragon", "image_path": "img/baby_dragon.png", "elixir_cost": 4},
    {"name": "dark_prince", "image_path": "img/dark_prince.png", "elixir_cost": 4},
    {"name": "hunter", "image_path": "img/hunter.png", "elixir_cost": 4},
    {"name": "goblindrill", "image_path": "img/goblindrill.png", "elixir_cost": 4},
    {"name": "freeze", "image_path": "img/freeze.png", "elixir_cost": 4},
    {"name": "poison", "image_path": "img/poison.png", "elixir_cost": 4},
    {"name": "balloon", "image_path": "img/balloon.png", "elixir_cost": 5},
    {"name": "prince", "image_path": "img/prince.png", "elixir_cost": 5},
    {"name": "bowler", "image_path": "img/bowler.png", "elixir_cost": 5},
    {"name": "executioner", "image_path": "img/executioner.png", "elixir_cost": 5},
    {"name": "cannon_cart", "image_path": "img/cannon_cart.png", "elixir_cost": 5},
    {"name": "witch", "image_path": "img/witch.png", "elixir_cost": 5},
    {"name": "electro_dragon", "image_path": "img/electro_dragon.png", "elixir_cost": 5},
    {"name": "giant_skeleton", "image_path": "img/giant_skeleton.png", "elixir_cost": 6},
    {"name": "goblin_giant", "image_path": "img/goblin_giant.png", "elixir_cost": 6},
    {"name": "building_xbow", "image_path": "img/building_xbow.png", "elixir_cost": 6},
    {"name": "lightning", "image_path": "img/lightning.png", "elixir_cost": 6},
    {"name": "pekka", "image_path": "img/pekka.png", "elixir_cost": 7},
    {"name": "electrogiant", "image_path": "img/electrogiant.png", "elixir_cost": 7},
    {"name": "golem", "image_path": "img/golem.png", "elixir_cost": 8},
    {"name": "the_log", "image_path": "img/the_log.png", "elixir_cost": 2},
    {"name": "ice_wizard", "image_path": "img/ice_wizard.png", "elixir_cost": 3},
    {"name": "princess", "image_path": "img/princess.png", "elixir_cost": 3},
    {"name": "miner", "image_path": "img/miner.png", "elixir_cost": 3},
    {"name": "bandit", "image_path": "img/bandit.png", "elixir_cost": 3},
    {"name": "ghost", "image_path": "img/ghost.png", "elixir_cost": 3},
    {"name": "fisherman", "image_path": "img/fisherman.png", "elixir_cost": 3},
    {"name": "rage_barbarian", "image_path": "img/rage_barbarian.png", "elixir_cost": 4},
    {"name": "inferno_dragon", "image_path": "img/inferno_dragon.png", "elixir_cost": 4},
    {"name": "electro_wizard", "image_path": "img/electro_wizard.png", "elixir_cost": 4},
    {"name": "nightwitch", "image_path": "img/nightwitch.png", "elixir_cost": 4},
    {"name": "magic_archer", "image_path": "img/magic_archer.png", "elixir_cost": 4},
    {"name": "ram_rider", "image_path": "img/ram_rider.png", "elixir_cost": 5},
    {"name": "graveyard", "image_path": "img/graveyard.png", "elixir_cost": 5},
    {"name": "zap_machine", "image_path": "img/zap_machine.png", "elixir_cost": 6},
    {"name": "lava_hound", "image_path": "img/lava_hound.png", "elixir_cost": 7},
    {"name": "mega_knight", "image_path": "img/mega_knight.png", "elixir_cost": 7},
    {"name": "skeletonking", "image_path": "img/skeletonking.png", "elixir_cost": 4},
    {"name": "motherwitch", "image_path": "img/motherwitch.png", "elixir_cost": 4},
    {"name": "phoenix", "image_path": "img/phoenix.png", "elixir_cost": 4},
    {"name": "little_prince", "image_path": "img/little_prince.png", "elixir_cost": 3},
    {"name": "mightyminer", "image_path": "img/mightyminer.png", "elixir_cost": 4},
    {"name": "goldenknight", "image_path": "img/goldenknight.png", "elixir_cost": 4},
    {"name": "archerqueen", "image_path": "img/archerqueen.png", "elixir_cost": 5},
    {"name": "monk", "image_path": "img/monk.png", "elixir_cost": 5},
]



current_item_index = [1]
def label_clicked(image_path, elixir_cost, elixir_label):
    try:
        def handler(event):
            nonlocal elixir_label

            if current_item_index[0] <= 8:
                current_item = getattr(form, f"item{current_item_index[0]}")
                pixmap = QPixmap(image_path)
                pixmap = pixmap.scaled(83, 100)
                current_item.setPixmap(pixmap)
                current_item_index[0] += 1

                current_text = form.elixir.text()
                current_count = float(current_text) if current_text else 0
                new_count = max(0, current_count - elixir_cost)
                form.elixir.setText(str(round(new_count, 1)))
        return handler
    except Exception as e:
        print(e)

for i in range(len(cards)):
    pixmap = QPixmap(cards[i]['image_path'])
    pixmap = pixmap.scaled(83, 100)
    card_widget = getattr(form, f"{cards[i]['name']}")
    card_widget.setPixmap(pixmap)
    card_widget.mousePressEvent = label_clicked(cards[i]['image_path'], cards[i]['elixir_cost'], form.elixir)



active_labels = []
def deck_label_clicked(i, elixir_cost, cards):
    def handler(event):
        global active_labels

        if len(active_labels) == 4:
            last_label = active_labels.pop(0)
            last_label.setStyleSheet("")

        chosen = getattr(form, f"item{i}")

        if chosen in active_labels:
            active_labels.remove(chosen)
        else:
            active_labels.append(chosen)
            chosen.setStyleSheet("background-color: rgba(255, 0, 0, 0.7)")
    return handler

for i in range(1, 9):
    label = getattr(form, f"item{i}")
    label.mousePressEvent = deck_label_clicked(i, form.elixir, cards)

for i in range(1, 5):
    label = getattr(form, f"item{i}")
    label.setStyleSheet("background-color: rgba(255, 0, 0, 0.7)")
    active_labels.append(label)











is_function_running = False
def thread_table():
    global is_function_running
    if is_function_running:
        return
    is_function_running = True
    try:
        while True:
            time.sleep(0.28)
            current_text = form.elixir.text()
            print(current_text)
            current_count = float(current_text) if current_text else 0
            if current_count < 10:
                current_count += 0.1
                form.elixir.setText(str(round(current_count, 1)))
    finally:
        is_function_running = False

def thread_start():
    thread_conn = threading.Thread(target=thread_table)
    thread_conn.start()

form.start.clicked.connect(thread_start)

def subtract_one():
    current_text = form.elixir.text()
    current_count = float(current_text) if current_text else 0
    new_count = max(0, current_count - 1)
    form.elixir.setText(str(round(new_count, 1)))
form.calc_1.clicked.connect(subtract_one)
def subtract_two():
    current_text = form.elixir.text()
    current_count = float(current_text) if current_text else 0
    new_count = max(0, current_count - 2)
    form.elixir.setText(str(round(new_count, 1)))
form.calc_2.clicked.connect(subtract_two)
def subtract_three():
    current_text = form.elixir.text()
    current_count = float(current_text) if current_text else 0
    new_count = max(0, current_count - 3)
    form.elixir.setText(str(round(new_count, 1)))
form.calc_3.clicked.connect(subtract_three)
def subtract_four():
    current_text = form.elixir.text()
    current_count = float(current_text) if current_text else 0
    new_count = max(0, current_count - 4)
    form.elixir.setText(str(round(new_count, 1)))
form.calc_4.clicked.connect(subtract_four)
def subtract_five():
    current_text = form.elixir.text()
    current_count = float(current_text) if current_text else 0
    new_count = max(0, current_count - 5)
    form.elixir.setText(str(round(new_count, 1)))
form.calc_5.clicked.connect(subtract_five)
def subtract_six():
    current_text = form.elixir.text()
    current_count = float(current_text) if current_text else 0
    new_count = max(0, current_count - 6)
    form.elixir.setText(str(round(new_count, 1)))
form.calc_6.clicked.connect(subtract_six)
def subtract_seven():
    current_text = form.elixir.text()
    current_count = float(current_text) if current_text else 0
    new_count = max(0, current_count - 7)
    form.elixir.setText(str(round(new_count, 1)))
form.calc_7.clicked.connect(subtract_seven)
def subtract_eight():
    current_text = form.elixir.text()
    current_count = float(current_text) if current_text else 0
    new_count = max(0, current_count - 8)
    form.elixir.setText(str(round(new_count, 1)))
form.calc_8.clicked.connect(subtract_eight)



window.show()
app.exec()
