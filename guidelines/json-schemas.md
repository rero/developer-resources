# JSON schemas

:warning: **To be completed!**

These guidelines are also related to the
[UX charter](https://github.com/rero/rero-ils/wiki/UX-charter), specifically
the [Form design](https://github.com/rero/rero-ils/wiki/UX-charter#4-form-design)
section.

## `$schema` property

- Mandatory.

## Key names

- Snail case is the main rule: `snail_case` instead of `camelCase`.
- Except when the key name (ie field name) is inspired from BIBFRAME. This is
the case with documents, as specified by the *metadata working group*.

## Title

Title is the natural language form of the property. It does not have any
punctuation mark.

## Description

- A description is optional.
- If used, it should add information to the title.
- It's considered as an help for the form user.
- It's a sentence, it begins with a capital letter and ends with a punctuation
mark.

## String

- Strings always set the `minLength` property, and if relevant the `maxLength`.

## Array

- Arrays always set the `minItems` property.
