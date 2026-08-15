from agent.agent import ViralAgent

print("=== VIRAL AGENT V1.1 TEST ===")
agent = ViralAgent()
result = agent.run("Gojo aura edit")

print("\n=== RESULT ===")
print("Song:", result["song"])
print("Beats:", result["beats"])
print("Status:", result["status"])
