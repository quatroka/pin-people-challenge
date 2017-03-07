# Test File for UVa problem 195 - Anagram

require_relative "uva_195_with_modules"
require "test/unit"


# Test class for testing permutations.
class TestPermutation < Test::Unit::TestCase
  # Test if method get_amount_results returns the correct
  # permutation amount.
  def test_amount_results
    assert_equal(6, get_permutation_list("abc").length)
    assert_equal(24, get_permutation_list("abcd").length)
    assert_equal(1, get_permutation_list("aaa").length)
    assert_equal(3, get_permutation_list("aab").length)
  end

  # Test if method get_permutation_list returns the 
  # permutation list corretily.
  def test_permutation_list
    assert_equal(["aaa"], get_permutation_list("aaa"))
    assert_equal(["abc", "acb", "bac", "bca", "cab", "cba"],
                  get_permutation_list("abc"))
  end
end
