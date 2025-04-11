import asyncio

from onecompiler import OneCompiler, models


async def main():
    # compiler = AsyncOneCompiler()
    # print(await compiler.Studio.get_templates())
    # print(await compiler.Studio.launch("python"))
    # print(await compiler.Studio.workspaces())

    compiler = OneCompiler()
    # print(compiler.Studio.get_templates())
    # print(compiler.Studio.launch("python"))
    # print(compiler.Studio.workspaces())
    file1 = models.File(name="test.py", content="print('Я ГЕЕЕЕЕЕЕЙ')")
    print(compiler.Compiler.exec("python", [{"name": "main.py", "content": "import test"}, file1]))

if __name__ == "__main__":
    asyncio.run(main())
