# JSON schemas

:warning: **To be completed!**

These guidelines are also related to the
[UX charter](https://github.com/rero/rero-ils/wiki/UX-charter), specifically
the [Form design](https://github.com/rero/rero-ils/wiki/UX-charter#4-form-design)
section.

## Order

[To be completed. Try to normalize the order inside a JSON schema object].

## `$schema` property

- Mandatory.

## Key names

- Snail case is the main rule: `snail_case` instead of `camelCase`.
- Except when the key name (ie field name) is inspired from BIBFRAME. This is
the case with documents, as specified by the *metadata working group*.

## Title

- Title is the natural language form of the property.
- It does not have any punctuation mark.
- In English and French, only the first word has a capitalized initial!

## Description

- A description is optional.
- If used, it should add information to the title.
- It's considered as an help for the form user.
- It's a sentence, it begins with a capital letter and ends with a punctuation
mark.
- In English, only the first word has a capitalized initial.

## String

- Strings always set the `minLength` property, and if relevant the `maxLength`.
- If the `pattern` property is set and requires at least one character, the `minLength` property is not mandatory.

## Array

- Arrays always set the `minItems` property.

### How to handle plurals

In the following example, the main key is singular, but it's `title` is plural,
as it is the label in the editor, which will contain a list of elements.

On the contrary, the `title` of the `array` `items` is singular, as it is the
label of each item of the list.

The same logic would apply to the `description` if any where there.

```json
    "language": {
      "title": "Languages",
      "type": "array",
      "minItems": 1,
      "uniqueItems": true,
      "items": {
        "type": "object",
        "title": "Language",
        "required": [
          "type",
          "value"
        ],
        "additionalProperties": false,
        "propertiesOrder": [
          "type",
          "value"
        ],
        "properties": {
          "type": {
            "title": "Type",
            "description": "Type of the language.",
            "type": "string",
            "default": "bf:Language",
            "enum": [
              "bf:Language"
            ],
            "form": {
              "hideExpression": "true",
              "options": [
                {
                  "label": "bf:Language",
                  "value": "bf:Language"
                }
              ]
            }
          },
          "value": {
            "$ref": "#/definitions/language"
          }
        }
      }
    }
```

## Enum

- **form options**:
    - use the `value`/`label` method **only** if the codes need to be
      translated.
    - in the `label`, always use natural language, ie the string
      to be translated, not a code, snail case or camel case! Except for the
      language list and the country list.
