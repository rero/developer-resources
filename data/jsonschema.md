# JSON schema

## Documentation

- JSON Schema: <http://json-schema.org>
- Understanding JSON Schema: <https://spacetelescope.github.io/understanding-json-schema/>

## Guidelines

These guidelines are also related to the [layout charter][1], specifically the
[form design][2] section.

:warning: Form options shoud be documented, somewhere.

[1]: interface/layout-charter.md
[2]: interface/layout-charter.md#4-form-design

### Order

Properties are ordered like this:

1. title
2. description
3. type
4. default (Default value)
5. Constraints (e.g. *minLength* or *pattern* or *minItems*)
6. additionalProperties (Only for objects)
7. properties (Only for objects)
8. propertiesOrder (Only for objects)
9. required (Only for objects)
10. items (Only for arrays)
11. form (Editor specific behavior)

## `$schema` property

- Mandatory.

## Key names

- Snake case is the main rule: `snake_case` instead of `camelCase`.
- Except when the key name (ie field name) is inspired from BIBFRAME. This is
the case with documents, as specified by the *metadata working group*.

## Title

- Title is the natural language form of the property.
- It does not have any punctuation mark.
- In English and French, only the first word has a capitalized initial!

## Description

- A description is optional.
- If used, it should add information to the title.
- It's considered as a form help for the end user.
- It's a sentence, it begins with a capital letter and ends with a punctuation
mark.
- In English, only the first word has a capitalized initial.

## String

- Always set the `minLength` and `maxLength` property. Adapt the ES mapping
  accordingly (see [ES doc on `ignore_above`](https://www.elastic.co/guide/en/elasticsearch/reference/current/ignore-above.html))
- If the `pattern` property is set and requires at least one character, the `minLength` property is not mandatory.

## Array

- Arrays always set the `minItems` property.

### How to handle plurals

In the following example, the main key is singular, but its `title` is plural,
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

- **For values**, apply the following rules to ease the translation work:
  - Use a standard controlled vocabulary if possible. Example: [RDA values](http://www.rdaregistry.info/termList/)
    - Use a prefix to identify the vocabulary, and separate it from the value with colon `:`
    - Example for RDA mode of issuance: `rdami:1001`. "rdami" refers to a URI.
  - If no standard controlled vocabulary exists
    - use natural language, or
    - create *home made* codes, if the values need specific translations that should not be confused with others.
      - add a *home made* prefix spearated by underscore `_` in the case of a list bigger than 8-10 values or if the code is too short (like sz for Switzerland).
      - Example of a home made code with prefix for Switzerland: `country_sz`.
      - Example of a home made code without prefix: `received_and_complete_or_ceased`
- **Form options**:
  - Use the `value`/`label` method **only** if the codes need to be
      translated.
  - In the `label` value, use the same value as the one of the `value` key.
      This is to avoid translating the label and the value, as it is sometimes
      needed.
  - In case of a list and sublist with `oneOf` (ex: main type/subtype), use the same text for `title` of the 1st-level element, as for `value` and `label`. This will ease the translations.
