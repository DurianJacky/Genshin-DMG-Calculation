class Enemy:
    def __init__(self, name, level=90, resist=10, DefReduction=0):
        self.name = name
        self.level = level
        self.resist = resist
        self.DefReduction = DefReduction
    
    def info(self):
        print(f"{self.__class__.__name__} 属性列表：")
        for key, value in self.__dict__.items():
            if(value != 0):
                value = round(value, 2) if isinstance(value, float) else value
                print(f"\t{key}: {value}")