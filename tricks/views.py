from django.shortcuts import render
import random

# --- Lists of tricks ---
math_tricks = [
    "Multiply any number by 5 — divide by 2 and add a zero!",
    "To multiply by 11, add the digits and place the sum in the middle: 23×11 = 253.",
    "Divisible by 9? The sum of digits is divisible by 9.",
    "To find 15% of a number, divide by 10 and add half of that result.",
    "Any number times 9 — the digits of the result sum to 9."
]

word_tricks = [
    "‘Racecar’ and ‘level’ are palindromes — same forward and backward.",
    "‘Dormitory’ → ‘Dirty room’ (anagram!)",
    "The word ‘queue’ has 4 silent letters in a row.",
    "‘Bookkeeper’ has three pairs of double letters in a row.",
    "‘Dreamt’ is the only English word ending with ‘mt’."
]

def home(request):
    context = {}
    if request.method == "POST":
        if "math" in request.POST:
            context["trick"] = f"🧮 Math Trick: {random.choice(math_tricks)}"
        elif "word" in request.POST:
            context["trick"] = f"🔤 Word Trick: {random.choice(word_tricks)}"
        elif "kaprekar" in request.POST:
            number = request.POST.get('number')
            if len(number) != 4 or len(set(number)) == 1:
                result = "❌ Please enter a 4-digit number with at least two different digits."
            else:
                n = int(number)
                steps = [f"Starting number: {n}"]
                count = 0
                while n != 6174 and count < 10:
                    digits = f"{n:04d}"
                    asc = int(''.join(sorted(digits)))
                    desc = int(''.join(sorted(digits, reverse=True)))
                    n = desc - asc
                    count += 1
                    steps.append(f"{count}. {desc} - {asc} = {n}")
                if n == 6174:
                    steps.append(f"\n✨ Reached 6174 in {count} steps!")
                result = "\n".join(steps)
            context["kaprekar_result"] = result

    return render(request, 'home.html', context)
