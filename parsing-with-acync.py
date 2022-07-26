import requests
import time
import asyncio
import aiohttp
 
 
 
start_time = time.time()    # выводим время и скраппим
 
 
def get_page_data(category: str, page_id: int) -> str:
    if page_id:
        url = f'https://ozon.ru/brand/{category}/?page={page_id}'   # смотрим категории с ид
    else:
        url = f'https://ozon.ru/brand/{category}/'
    print(f'get url: {url}')
    response = requests.get(url)    # получаем текст
    return response.text
 
 
def load_site_data():
    categories_list = ['playstation-79966341', 'adidas-14402850', 'boch-7577796', 'lego-19159896']
    for cat in categories_list:
        for page in range(100):
            text = get_page_data(cat, page)     # заброс в функцию
 
 
if __name__ == '__main__':
    load_site_data()
 
    end_time = time.time() - start_time
    print(f'\nExecution time: {end_time} seconds')  # 90
 
start_time = time.time()
all_data = []   # массив для данных
 
 
async def get_page_data(session, category: str, page_id: int) -> str:
    if page_id:
        url = f'https://ozon.ru/brand/{category}/?page={page_id}'   # смотрим категории с ид
    else:
        url = f'https://ozon.ru/brand/{category}/'
    async with session.get(url) as resp:
        assert resp.status == 200
        print(f'get url: {url}')
        resp_text = await resp.text()
        all_data.append(resp_text)
        return resp_text
 
 
async def load_site_data():
    categories_list = ['playstation-79966341', 'adidas-14402850', 'boch-7577796', 'lego-19159896']
    async with aiohttp.ClientSession() as session:  # делаем мк
        tasks = []  # делаем массив задач для запуска
        for cat in categories_list:
            for page in range(100):
                task = asyncio.create_task(get_page_data(session, cat, page))   # создаем задачу для менеджера
                tasks.append(task)
            await asyncio.gather(*tasks)       # ждем пока список не сформируется
 
 
asyncio.run(load_site_data())   # запуск
 
end_time = time.time() - start_time
print(f'\nExecution time: {end_time} seconds')  # 1.4
