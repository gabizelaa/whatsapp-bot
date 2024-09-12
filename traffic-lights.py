import sqlite3
import time

class TrafficLight:
    def __init__(self, id):
        self.id = id
        self.state = 'Red'
        self.setup_database()

    def setup_database(self):
        conn = sqlite3.connect('traffic_lights.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS traffic_lights (
                id INTEGER PRIMARY KEY,
                state TEXT
            )
        ''')
        c.execute('INSERT OR IGNORE INTO traffic_lights (id, state) VALUES (?, ?)', (self.id, self.state))
        conn.commit()
        conn.close()

    def update_light(self, state):
        conn = sqlite3.connect('traffic_lights.db')
        c = conn.cursor()
        c.execute('UPDATE traffic_lights SET state = ? WHERE id = ?', (state, self.id))
        conn.commit()
        conn.close()

    def red_light(self):
        self.state = 'Red'
        print("🔴 Semáforo Vermelho - Pare")
        self.update_light(self.state)
        time.sleep(5)

    def yellow_light(self):
        self.state = 'Yellow'
        print("🟡 Semáforo Amarelo - Atenção")
        self.update_light(self.state)
        time.sleep(2)

    def green_light(self):
        self.state = 'Green'
        print("🟢 Semáforo Verde - Siga")
        self.update_light(self.state)
        time.sleep(5)

    def start_traffic(self):
        while True:
            self.red_light()
            self.yellow_light()
            self.green_light()
            self.yellow_light()

# Inicializa o semáforo com um ID específico
traffic_light = TrafficLight(id=1)

# Inicia a simulação de tráfego
traffic_light.start_traffic()
