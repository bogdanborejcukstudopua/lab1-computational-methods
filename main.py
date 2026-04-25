# Модель: Математичне моделювання перехідних процесів в електричному ланцюзі (RLC)
# Автор: Борейчук Б.М., група AI-235

from scipy.integrate import odeint

class TransientModel:
    def __init__(self, params_dict):
        # Ініціалізація параметрів з Етапу 1 (R, L, C)
        self.R = params_dict['R']
        self.L = params_dict['L']
        self.C = params_dict['C']

    def system_equations(self, state, t, E_func):
        i, u_c = state
        E_val = E_func(t) # Джерело ЕРС може залежати від часу
        didt = (E_val - self.R * i - u_c) / self.L
        ducdt = i / self.C
        return [didt, ducdt]

    def solve(self, t_span, initial_cond, E_func):
        # Використання бібліотеки SciPy для інтегрування
        return odeint(self.system_equations, initial_cond, t_span, args=(E_func,))

if __name__ == "__main__":
    print("Модель RLC успішно завантажена. Готово до розрахунків!")
