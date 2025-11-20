import requests, time

def monitor_new_memes():
    print("Мониторинг новых мемкоинов на Solana (dexscreener)...")
    seen = set()
    while True:
        r = requests.get("https://api.dexscreener.com/latest/dex/tokens/new")
        for pair in r.json().get("pairs", []):
            if pair["chainId"] != "solana": continue
            addr = pair["baseToken"]["address"]
            if addr in seen: continue
            seen.add(addr)
            price = float(pair["priceUsd"])
            if price < 0.001:  # только ультра-дешёвые
                print(f"НОВЫЙ МЕМ!\n"
                      f"{pair['baseToken']['symbol']} / {pair['quoteToken']['symbol']}\n"
                      f"Цена: ${price:.10f}\n"
                      f"Ликвидность: ${pair['liquidity']['usd']:,.0f}\n"
                      f"DEX: {pair['dexId'].upper()}\n"
                      f"https://dexscreener.com/solana/{addr}\n"
                      f"{'-'*50}")
        time.sleep(8)

if __name__ == "__main__":
    monitor_new_memes()
