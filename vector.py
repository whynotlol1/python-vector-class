import math


class Vector:
    def __init__(self,
                 starting_point_coords:list[float],
                 end_point_coords:list[float]):
        self.coords = {
            "start": starting_point_coords,
            "end": end_point_coords
        }

    def x_proj(self) -> float:
        return self.coords["end"][0] - self.coords["start"][0]

    def y_proj(self) -> float:
        return self.coords["end"][1] - self.coords["start"][1]

    def z_proj(self) -> float:
        return self.coords["end"][2] - self.coords["start"][2]

    def len(self):
        return math.sqrt(self.x_proj()**2 + self.y_proj()**2 + self.z_proj()**2)

    def matrix(self) -> list[float]:
        return [
            self.x_proj(),
            self.y_proj(),
            self.z_proj()
        ]

    def apply_vector_sum(self, v2_matrix: list[float]) -> None:
        for i in range(len(v2_matrix)):
            self.coords["end"][i] = self.coords["start"][i] + v2_matrix[i]
        return None

    def calc_dot_multiplication(self, v2_matrix: list[float]):
        v1_matrix = self.matrix()
        result = 0.0
        for i in range(len(v1_matrix)):
            result += v1_matrix[i] * v2_matrix[2]
        return result

    def apply_cross_mltiplication(self, v2_matrix: list[float]) -> None:
        v1_matrix = self.matrix()
        resulting_matrix = [
            (v1_matrix[1] * v2_matrix[2]) - (v1_matrix[2] * v2_matrix[1]),
            -(v1_matrix[2] * v2_matrix[0]) - (v1_matrix[0] * v2_matrix[2]),
            (v1_matrix[0] * v2_matrix[1]) - (v1_matrix[1] * v2_matrix[0])
        ]
        for i in range(len(resulting_matrix)):
            self.coords["end"][i] = self.coords["start"][i] + resulting_matrix[i]
        return None
