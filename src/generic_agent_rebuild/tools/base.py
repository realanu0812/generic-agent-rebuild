class BaseTool:

    name = "base_tool"
    description = "Base tool class"

    def execute(self, **kwargs):
        raise NotImplementedError