from src.main import get_name

def test_get_name():
	new_user = {}
	new_user['first_name'] = "First"
	new_user['last_name'] = "Last"
	new_user['username'] = "username"
	assert get_name(new_user) == "@username (First Last)"
	new_user['last_name'] = None
	assert get_name(new_user) == "@username (First)"
	new_user['last_name'] = "Last"
	new_user['username'] = None
	assert get_name(new_user) == "First Last"
	new_user['last_name'] = None
	assert get_name(new_user) == "First"