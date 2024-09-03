def greet_user(name):
            return f"Hello, {name}!"

        def run_python():
            name_input = Element('variableName').element.value
            result = greet_user(name_input)
            Element('result').element.innerText = result

        Element('runPythonButton').element.onclick = run_python
