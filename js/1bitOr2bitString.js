var isOneBitCharacter = function(bits) {
	count = bits.length
    if(bits[count - 1] != 0)
        return false

    var find = false
	var i = count - 2
	while(i > 0){
		if (bits[i] == 0){
            find = true
			break
		}
		i--
	}
    if (find)
        i++
	return (count-1 - i) % 2 == 0
};

console.log(isOneBitCharacter([1,1,0]))