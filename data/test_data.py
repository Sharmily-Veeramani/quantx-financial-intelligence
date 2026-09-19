from data.loader import load_asset

gold = load_asset(
    "GC=F",
    "2024-01-01",
    "2026-01-01"
)

bitcoin = load_asset(
    "BTC-USD",
    "2024-01-01",
    "2026-01-01"
)

nvidia = load_asset(
    "NVDA",
    "2024-01-01",
    "2026-01-01"
)
print("Gold rows:", len(gold))
print("Bitcoin rows:", len(bitcoin))
print("NVIDIA rows:", len(nvidia))
print("\n========== GOLD ==========")
print(gold.head())


print("\n========== BITCOIN ==========")
print(bitcoin.head())


print("\n========== NVIDIA ==========")
print(nvidia.head())