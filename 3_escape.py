a = "abcdefghijk \\ lmn" 

print(a)

# "\" use this for escape not "/" => \n-newline,\t-tab,\'-singlequote,\\-backslash

'''
"yash" = \"yash\"
| Escape Code | Meaning                       | Example Output                          |
| ----------- | ----------------------------- | --------------------------------------- |
| `\n`        | New line                      | `Hello\nWorld` →                        |
| `Hello`     |                               |                                         |
| `World`     |                               |                                         |
| `\t`        | Tab (4 spaces)                | `Hello\tWorld` → `Hello    World`       |
| `\\`        | Backslash                     | `\\` → `\`                              |
| `\'`        | Single quote                  | `'I\'m Yash'` → `I'm Yash`              |
| `\"`        | Double quote                  | `"He said, \"Hi!\""` → `He said, "Hi!"` |
| `\r`        | Carriage return (rarely used) | `Hello\rWorld` → `World`                |
| `\b`        | Backspace                     | `Helloo\b` → `Hello`                    |
| `\f`        | Form feed (rare)              | May break line (printer style)          |
| `\a`        | Bell (sound alert, beep)      | Beeps on some systems                   |
| `\uXXXX`    | Unicode character             | `\u2764` → ❤️ (Unicode for heart)       |

'''