# Safari Animals

Write a program to print out the description of safari animal, based on user input.

## Your Task

In the starter code, there's a list of safari animals, and a list of descriptions. There's also a loop that prints out each of the animal names and numbers. (See 'Starter Code' section below.)

Prompt the user to type in a number. Based on the number they type in, show the name and description of that animal.

## Expected Results

Here's a transcript of a successful run of the program:

```
Enter a number to read a description of an animal.
1. Lion
2. Elephant
3. Leopard
4. Rhino
5. Buffalo
Choose an animal: 1
Lion
The lion (Panthera leo) is a large mammal of the Felidae (cat) family. Some large males weigh over 250 kg (550 lb). Today, wild lions live in sub-Saharan Africa and in Asia. Lions are adapted for life in grasslands and mixed areas with trees and grass. The relatively small females are fast runners over short distances, and coordinate their hunting of herd animals.
```

## Hints

Remember - list indices start at `0`. But, the user will type in the number of the animal, starting with `1`. So, you'll have to convert from the number to the list index.

## Starter Code

Lines 6 and 7 of the starter code list the animals, with numbers next to each animal.

```
for (i, animal) in enumerate(animals):
  print(f"{i+1}. {animal}")
```

`enumerate` is a new function. It takes a list like `animals`, and turns it into a list with the elements and the index of each element. Then, the for loop has two variables:
- `i` is the index (`0`, `1`, `2`, `3`, `4`)
- `animal` is the string (`"Lion"`, `"Elephant"`, `"Leopard"`, `"Rhino"`, `"Buffalo"`)

So the loop prints out the animals and the numbers. 

`enumerate` is a handy function to remember, in case you need the index of each element in a list when you're looping over it with `for`!

## Testing

First, try your program interactively with `python3 main.py`. Try out different
numbers and make sure the output looks right.

Then, test your program with `python3 test_main.py`.

## Credits

Descriptions from Wikipedia.
