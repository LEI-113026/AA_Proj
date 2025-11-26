import json
import os
from typing import Type, Dict, Any


class ObjectFactory:
    def __init__(self, config_path: str):
        self.symbol_map = {}
        self.class_registry: Dict[str, Type] = {}

        self._load_config(config_path)

    def _load_config(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Config file not found: {path}")

        with open(path, 'r') as f:
            data = json.load(f)
            self.symbol_map.update(data.get("objects", {}))
            self.symbol_map.update(data.get("agents", {}))

    def register_class(self, class_name: str, cls: Type):
        self.class_registry[class_name] = cls

    def create(self, symbol: str, x: int, y: int) -> Any:
        type_name = self.symbol_map.get(symbol)
        if not type_name:
            return None

        cls = self.class_registry.get(type_name)
        if not cls:
            print(f"Warning: Symbol '{symbol}' maps to '{type_name}', but no Python class is registered.")
            return None
        return cls(x, y)