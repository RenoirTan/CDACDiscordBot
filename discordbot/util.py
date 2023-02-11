def railfence_encode(n_rails: int, plaintext: str) -> str:
    if n_rails == 1:
        return plaintext
    
    cycle_len = 2*(n_rails-1)
    
    rails = []
    for _ in range(n_rails):
        rails.append("")
    
    for index in range(len(plaintext)):
        character = plaintext[index]
        rail = index % cycle_len
        if rail >= n_rails:
            rail = cycle_len - rail
        rails[rail] += character
    
    output = ""
    for rail in rails:
        output += rail
    
    return output