from validations import generate_id

# tests that an empty members list returns 1 as the first id
def test_generate_id_return_1_when_list_empty():
    assert generate_id([]) == 1

# tests that the function returns the next highest id when ids are sequential
def test_generate_id_returns_next_max_number():
    members = [{"ID":1}, {"ID":2}, {"ID":10}]
    assert generate_id(members) == 11

# tests that ordering of ids does not affect the result
# ensures max() logic is used rather than relying on list position
def test_generate_id_return_next_number_unordered():
    members = [{"ID":10}, {"ID":2}, {"ID":21}]
    assert generate_id(members) == 22

# tests that string-based ids are correctly converted to integers
# before calculating the next available id
def test_generate_id_return_next_number_string():
    members = [{"ID":"4"}, {"ID":"2"}, {"ID":"13"}]
    assert generate_id(members) == 14
