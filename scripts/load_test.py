import httpx, random, time

URL = "http://localhost:8000/chat"
QUERIES = ["oil change", "battery fault", "brake noise", "tire pressure", "engine misfire"]

def main():
    for i in range(100):
        q = random.choice(QUERIES)
        try:
            r = httpx.post(URL, json={"query": q}, timeout=10)
            r.raise_for_status()
        except Exception as e:
            print("err:", e)
        time.sleep(random.uniform(0.02, 0.15))

if __name__ == "__main__":
    main()
