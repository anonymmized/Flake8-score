import subprocess
import sys
from typing import Tuple

def run_command(command: list) -> str:
    """Выполняет команду и возвращает вывод."""
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

def calculate_score(flake8_errors: int, mi_score: float) -> Tuple[float, str]:
    """Рассчитывает итоговую оценку на основе flake8 и индекса поддерживаемости."""
    # Базовая оценка 10
    score = 10.0
    
    # Вычитаем баллы за ошибки flake8
    if flake8_errors > 0:
        score -= min(flake8_errors * 0.5, 5.0)
    
    # Учитываем индекс поддерживаемости
    if mi_score >= 90:
        score = score
    elif mi_score >= 80:
        score -= 1
    elif mi_score >= 70:
        score -= 2
    else:
        score -= 3
    
    # Определяем рейтинг
    if score >= 9.5:
        rating = "Perfect"
    elif score >= 8.5:
        rating = "Very Good"
    elif score >= 7.5:
        rating = "Good"
    elif score >= 6.5:
        rating = "Fair"
    else:
        rating = "Needs Improvement"
    
    return round(score, 1), rating

def analyze_code(file_path: str) -> None:
    """Анализирует код и выводит результаты."""
    print(f"\nAnalyzing {file_path}...")
    print("=" * 60)
    
    # Запуск flake8
    flake8_output = run_command(['flake8', file_path])
    flake8_errors = len(flake8_output.splitlines())
    
    # Получение индекса поддерживаемости
    mi_output = run_command(['radon', 'mi', file_path])
    try:
        mi_score = float(mi_output.split()[0])
    except (IndexError, ValueError):
        mi_score = 0.0
    
    # Расчет итоговой оценки
    score, rating = calculate_score(flake8_errors, mi_score)
    
    # Вывод результатов
    print(f"Code Quality Report:")
    print("-" * 60)
    print(f"Flake8 errors:           {flake8_errors}")
    print(f"Maintainability Index:   {mi_score:.1f}/100")
    print(f"Final Score:            {score}/10")
    print(f"Rating:                 {rating}")
    print("-" * 60)
    
    if flake8_errors > 0:
        print("\nDetailed Flake8 errors:")
        print(flake8_output)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python code_quality.py <file_path>")
        sys.exit(1)
    
    analyze_code(sys.argv[1])