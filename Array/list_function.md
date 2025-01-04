#### Boyer-Moore Voting Algorith
This is a way to find the majority voting algorithm in linear time using constant space.
- Maintain a candidate for the majority element.
- Use a count variable to track the vote for the candidate.
- Else, decrement count

After one pass the candidate will be the majority element. 
The Boyer-Moore Voting Algorithm will not work correctly if there is no guarantee that a majority element exists.