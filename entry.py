from dotenv import dotenv_values

config = {
      **dotenv_values(".env.shared"),
      **dotenv_values(".env.secret")
}

print(config)