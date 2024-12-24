// Given two strings s and t, determine if they are isomorphic.
//
// Two strings s and t are isomorphic if the characters in s can be replaced to get t.
//
// All occurrences of a character must be replaced with another character while preserving the order of characters.
// No two characters may map to the same character, but a character may map to itself.

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    if (s.length !== t.length)  {
        return false
    }
    const sToT = new Map();
    const tToS = new Map();

    for(let i = 0; i < s.length; i += 1) {
        const c1 = s[i];
        const c2 = t[i];

        if(sToT.has(c1)) {
            if(sToT.get(c1) !== c2) return false
        } else {
            sToT.set(c1, c2)
        };

        if (tToS.has(c2)) {
            if (tToS.get(c2) !== c1) return false;
        } else {
            tToS.set(c2, c1);
        }
    }
    return true;
}

// Time and Space Complexity is O(n)