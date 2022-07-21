/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    var s1_map = createHashMapForString(s1);
    var s2_map = initS2map(s2.slice(0,s1.length),createAlphabetMap());
    var matches = getMatchesValue(s1_map,s2_map);
    if(matches == s1_map.size){
            return true;
        }
    for (let j = s1.length; j < s2.length; j++) {
        var char_lost = s2[j-s1.length];
        var char_add = s2[j];
        matches = moveOneIndex(s1_map,s2_map,char_add,char_lost);
        if(matches == s1_map.size){
            return true;
        }
    }
    return false;
};

function moveOneIndex(s1_map,s2_map,char_add,char_lost){
    s2_map.set(char_add,s2_map.get(char_add) + 1);
    s2_map.set(char_lost,s2_map.get(char_lost) - 1);
    return getMatchesValue(s1_map,s2_map);
}

function initS2map(s2,s2_map){
    for (let index = 0; index < s2.length; index++) {
        const element = s2[index];
        s2_map.set(element,s2_map.get(element) + 1);
    }
    return s2_map;
}

function createAlphabetMap(){
    var s2_map = new Map();
    var alphabet = "abcdefghijklmnopqrstuvwxyz";
    for (let i = 0; i < alphabet.length; i++) {
        s2_map.set(alphabet[i],0);
    }
    return s2_map;
}

function getMatchesValue(s1_map,s2_map){
    var matches = 0;
    for (const [key, value] of s2_map) {
        if(s1_map.has(key) && value == s1_map.get(key)){
            matches++
        }
    }
    return matches;
}

function createHashMapForString(str){
    var map = new Map();
    for (let i = 0; i < str.length; i++) {
        const char = str[i];
        addCharToHasMap(map,char);
    }
    return map;
}

function addCharToHasMap(map,char){
    if(map.has(char)){
        map.set(char,map.get(char) + 1);
    } else {
        map.set(char,1);
    }
}