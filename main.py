from src.proj.tasks import add

result = add.delay(8, 8)
print('result ready:', result.get(timeout=1))
