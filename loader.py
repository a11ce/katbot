from dataclasses import dataclass
import os
import importlib


def log(text):
    print(text)


@dataclass
class ModuleConfig:
    defaultInclude: bool
    include: list[str]
    exclude: list[str]


def moduleInList(moduleName: str, lst: list[str]) -> bool:
    for name in lst:
        if name in moduleName:
            return True
    return False


def shouldLoadModule(config: ModuleConfig, name: str) -> bool:
    if config.defaultInclude:
        return not moduleInList(name, config.exclude)
    else:
        return moduleInList(name, config.include)


def loadModules():
    config = ModuleConfig(True, [], [])
    with open("moduleConfig.txt") as mc:
        for line in mc:
            opt = line.strip().split(" ")
            name = opt[1]
            isInclude = opt[0] == "Include"
            if opt[1] == "*":
                config.defaultInclude = True if isInclude else False
            else:
                (config.include if isInclude else config.exclude).append(name)

    modules = []
    for moduleName in os.listdir("modules"):
        if "__" not in moduleName and ".py" in moduleName:
            if shouldLoadModule(config, moduleName):
                modules.append(
                    importlib.import_module('.' + moduleName[:-3], 'modules'))
            else:
                print(f"skipped loading {moduleName}")

    for module in modules:
        log("LOADED MODULE: " + module.INFO['name'])
    log(f"{len(modules)} modules loaded")
    return modules
