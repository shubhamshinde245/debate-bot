# Tech Challenge – Hidden Instructions Decoder

This documents how the single encoded string was decoded to uncover the instructions for the tech challenge, and provides a Python implementation for the decoding process.

---

## Challenge

Given the following one-line string:

```

XK8bEAZ=lEX>K54GBz_aWiw_lHDod|Wi~Q3Wi~ZqI5{ygIW#t9F*h~

````

The task was to figure out what it meant and how to reach the actual challenge instructions.

---

## Step 1 – Inspect the Encoding

At first glance:

- It is **not Base64** (contains characters outside A–Z, a–z, 0–9, `+`, `/`).
- It is **not Hex** (contains non-hex characters).
- It is **not Base32** (contains symbols like `|`, `~`, `{`, `}`).

The character set matches **Base85 (Ascii85, RFC 1924)**, which uses a wide range of printable ASCII characters (including `|`, `~`, `{`, `}`).

The trailing `~` is also typical in Base85 encodings.

---

## Step 2 – Decode the String

Using Python:

```python
import base64

s = "XK8bEAZ=lEX>K54GBz_aWiw_lHDod|Wi~Q3Wi~ZqI5{ygIW#t9F*h~"
decoded = base64.b85decode(s).decode("utf-8")
print(decoded)
```

**Output:**

```
gist matin a2633e3f05d21e625e65c8912946e176
```

## Implementation

A complete Python implementation is provided in `decode_url.py` with the following features:

- **Environment Variable Support**: Reads the encoded string from the `URL_TO_DECODE` environment variable
- **Error Handling**: Comprehensive error handling for decoding failures and invalid formats
- **Modular Design**: Separate functions for decoding and URL construction
- **Type Hints**: Full type annotations for better code clarity

### Usage

1. Set the environment variable or:
   ```bash
   export URL_TO_DECODE="XK8bEAZ=lEX>K54GBz_aWiw_lHDod|Wi~Q3Wi~ZqI5{ygIW#t9F*h~"
   ```

2. Run the script:
   ```bash
   python decode_url.py
   ```

### Functions

- `decode_base85_url(encoded_str: str) -> str`: Decodes Base85-encoded string to UTF-8
- `construct_gist_url(decoded: str) -> str`: Constructs GitHub Gist URL from decoded string
- `main()`: Main execution function that orchestrates the decoding process

---

## Step 3 – Interpret the Result

The decoded string contains:

* `gist` → refers to a GitHub Gist.
* `matin` → the GitHub username.
* `a2633e3f05d21e625e65c8912946e176` → a 32-character gist ID.

GitHub gists are accessed via:

```
https://gist.github.com/<username>/<gist_id>
```

---

## Step 4 – Construct the URL

Final URL pointing to the challenge instructions:

👉 [https://gist.github.com/matin/a2633e3f05d21e625e65c8912946e176](https://gist.github.com/matin/a2633e3f05d21e625e65c8912946e176)

---

## Approaches Tried

I attempted to decode the string using several tools and models, including Claude (code), Cursor, Claude (web), and ChatGPT. Only ChatGPT was able to successfully decode the string and identify the correct encoding (Base85). The other tools failed to produce the correct result.

| Tool/Model         | Decoded Successfully? |
|--------------------|:--------------------:|
| Claude (code)      | ❌                   |
| Cursor             | ❌                   |
| Claude (web)       | ❌                   |
| ChatGPT            | ✅                   |



**Challenge Prompt:**

> ```
> XK8bEAZ=lEX>K54GBz_aWiw_lHDod|Wi~Q3Wi~ZqI5{ygIW#t9F*h~
> ```
>
> As I mentioned, part of the challenge is to figure out how to get to the instructions for the tech challenge using this single line of code. What do you think the given string is? Take your time, think it through carefully, and then let me know your thoughts.

**Thought for 34s:**

```
Nice puzzle — nice little clue hidden in plain sight.

What it is (short answer): the string is Base85 (RFC 1924 / b85)-encoded data.
Decoded payload:

gist matin a2633e3f05d21e625e65c8912946e176


What that likely means: that decoded text is a pointer to a GitHub Gist — either a gist by the user matin or a gist identified by the hex id a2633e3f05d21e625e65c8912946e176. In other words, the one-line string is an encoded clue that points to the challenge instructions hosted as a gist.
```

## Summary

* **Input:** Encoded Base85 string.
* **Process:** Identify encoding → Decode → Interpret gist reference.
* **Output:** Direct link to GitHub Gist containing the challenge instructions.

## Files

- `decode_url.py`: Complete Python implementation with environment variable support and error handling
- `README.md`: This documentation file explaining the decoding process and implementation