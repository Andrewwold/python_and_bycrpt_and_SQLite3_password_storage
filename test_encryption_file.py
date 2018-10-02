import bcrypt

def get_hashed_password(plain_text_password):
	return bcrypt.hashpw(plain_text_password.encode("utf8"), bcrypt.gensalt())

print(get_hashed_password('our'))

def check_password(plain_text_password, hashed_password):
	return bcrypt.checkpw(plain_text_password.encode("utf8"), hashed_password.encode("utf8"))

print(check_password('ourpassword', '$2a$12$0yT328AmHonELkREt48MJuRuw8lbX0P/Wzg8lLeik7P7rHxGMoUw.'))

print(check_password('our', '$2a$12$Aa7lKqXoDLU9UED0Z0iaDuQIYVXLcBlotRX4mvtSUs8QwxoXaRZii'))

print(check_password('ourpassword', '$2a$12$0yT328AmHonELkREt48MJuRuw9lbX0P/Wzg8lLeik7P7rHxGMoUw.'))