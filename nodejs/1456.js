/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
   var vowels = ['a', 'e', 'i', 'o', 'u'];
   var vowelMax = 0;
   var count = 0
   for(var i = 0; i < k; i++){
       if(vowels.includes(s[i])){
           count++
       }
   }

    vowelMax = count

    for(var j = i; j < s.length; j++){
        if(vowels.includes(s[j])){
            count++
        }
        if(vowels.includes(s[j - k])){
            count--
        }
        if(count > vowelMax){
            vowelMax = count
        }
    }

   return vowelMax; 
};