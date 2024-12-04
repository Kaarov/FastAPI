Video: https://youtu.be/jQhKoXhNecQ

Install dependency:
```shell
pip install 'fastapi[standard]'
```

## Запуск приложение

### 1 способ
``` shell
fastapi dev main.py
```

### 2 способ
``` shell
uvicorn main:app --reload
```

### 3 способ
main.py:
```python
if __name__ == "__main__":
     uvicorn.run("1run_fastapi:app", reload=True)
```
```shell
python main.py
```
