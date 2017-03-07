# File to resolve UVa problem 195 - Anagra.
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=131


# Receive a letters sequence return your permutation.
#
# * Receive a letters sequence in string format, split that
# * in a list of characters and create a list of permutation
# * with that in a list of permutation in ascending order.
def get_permutation_list(letters_sequence)
  letters_sequence = letters_sequence.split(//)

  permutation_list = letters_sequence.permutation.to_a

  permutation_list = permutation_list.map{|x| x.join("")}

  return permutation_list.uniq.sort
end

# n_cases = gets.to_i

# result_list = []
# for i in 1..n_cases do
#   permutation_list = get_permutation_list(gets.chomp)
#   result_list << permutation_list
# end

# for j in 0..(result_list.length - 1) do
#     puts result_list[j]
# end
