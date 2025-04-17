var romanToInt = function(s) {
    const roman_numbers =
        {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        };

    let total = 0;

    for (let i = 0; i < s.length; i += 1) {
        const curr = roman_numbers[s[i]];
        const next = roman_numbers[s[i] + 1];

        if (curr < next) {
            total -= curr;
        } else {
            total += curr;
        }
    }
    return total

};

// Time and Space complexity are O(n) and O(1)