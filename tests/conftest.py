import asyncio
import pytest

# Настройка для использования глобального цикла событий
@pytest.fixture(scope="session")
def event_loop():
    """Создаем единый цикл событий для всей сессии тестирования."""
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    yield loop
    
    # Не закрываем цикл, чтобы избежать проблемы с повторным использованием
    # loop.close()