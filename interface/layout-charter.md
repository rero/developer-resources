# Layout charter

## 1. Guiding principles of the interface

* The Bootstrap 4 framework is used to date (January 2020).

## 2. Information architecture

### Header & menus

Prov :
The main navigation consists of a horizontal bar composed of different menus, which open in mousehover. In the version for small screens, this bar is grouped into a hamburger menu.

### Administration bar (administration functions)

### Multi-windows

Web applications: multi-windows is managed through the web browser tabs.

## 3. Navigation and interaction

### Navigation areas

### Links

Intern to RERO ILS
* All internal links open in the current window.
* When the opening of a link results in the loss of current transactions, a modal window opens and asks for confirmation.

External to RERO ILS
* All links to another application (RERO or not) open in a new tab and are marked by a small icon, on the example of Wikipedia1.

### Buttons

1. Use mostly outline buttons.
1. Except if a specific action is to be encouraged (call to action): this is a
   primary button. Only once per page. Primary buttons are not mandatory.
1. All destructive actions are to be red (danger).
1. When there's enough room, use a label. An additional icon is optional.   
   :warning: In the same group of button, do not mix button with or without
   icon.
   Example:   
   ![Example](/interface/correct-button-outline.png)
1. When place is scarce, use a button with an icon only. Try to [make it
   accessible](https://developer.mozilla.org/fr/docs/Web/HTML/Element/button#Accessibilit%C3%A9)
   Example:
   ![Example](/interface/correct-button-icons.png)
   

<table>
    <tr>
        <th></th>
        <th>Primary action<br/>enabled/disabled</th>
        <th>Secondary action<br/>enabled/disabled</th>
    </tr>
    <tr>
        <td></td>
        <td>Usage: define the main action, only one per page if possible. Ex: save, request, delete (in delete confirmation popup)</td><td>Usage: for standard actions. Ex: edit, cancel, add</td>
    </tr>
    <tr>
        <td>Standard</td>
        <td><img src="https://user-images.githubusercontent.com/8154915/76531827-0faaed00-6476-11ea-89a7-f03a31455b32.png"/><br/>class="btn btn-primary"</td>
        <td><img src="https://user-images.githubusercontent.com/8154915/76531857-19cceb80-6476-11ea-808e-9db1241854e3.png"/><br/>class="btn btn-outline-primary"</td>
    </tr>
    <tr>
        <td>Negative<br/>Usage: destructive actions. Ex: cancel, delete</td>
        <td><img src="https://user-images.githubusercontent.com/8154915/76531882-22bdbd00-6476-11ea-8b8f-9c62dce22ea1.png"/><br/>class="btn btn-danger"</td>
        <td><img src="https://user-images.githubusercontent.com/8154915/76531924-310bd900-6476-11ea-81b0-a440bdc722a7.png"/><br/>class="btn btn-outline-danger"</td>
    </tr>
</table>

In general, using of Bootstrap's Outline buttons.

Buttons for indirect action, i.e. leading to an intermediate stage before the action is carried out, have a label followed by three small points

<img src="https://user-images.githubusercontent.com/8154915/74410173-bf217f00-4e38-11ea-98b2-918857b876cd.png" alt="button 2" />

Location of buttons
* The buttons are placed on the right of the objects concerned (examples: delete, edit).
* Save button
   * placed at the bottom right (and top right?) of the object concerned
   * visible at any time on an editor's page: sticky position
   * always associated with the cancel button on its left.
<img src="https://user-images.githubusercontent.com/8154915/76735507-4ed28a00-6765-11ea-8d18-8c03ab570d5c.png" alt="button save" />

### Input/search fields

### Drop-down menus

### Colours (for buttons and feedback infos)

## 4. Form design

## Help and description aspects

JSON schema field: **description**

In the context of RERO ILS
* The description is displayed as a tooltip when hovering over the name of a field with the mouse.
* Use description only if necessary/useful
* Objective: that the user understands the content of the field. It is a simplified help within the system.
* For cataloguing: indicate RDA toolkit extracts and MARC equivalences.

Example
![Description example](https://user-images.githubusercontent.com/8154915/74410509-89c96100-4e39-11ea-8225-02b3ae092ba4.png)

## Placeholder

JSON schema field: **placeholder**

Definition
* A placeholder is a text that appears inside an input field, in light gray. When text is inserted into this field, the placeholder disappears.

In the context of RERO ILS
* Use placeholder only if necessary/useful
* Objective: that the user knows how, in what form, to enter the data.
* Use the placeholder only for examples of allowed values or formatting.
* Prefix it with the word "Example" so as not to confuse it with a value already entered or default value.
* For cataloguing: indicate examples or RDA terms when they are only recommendations (see example below). If a field consist of a closed list of accepted values, a drop-down menu is displayed and no placeholder is needed.

Examples are:
![placeholder_example](https://user-images.githubusercontent.com/8154915/74410602-c432fe00-4e39-11ea-9df3-e49b8b6ced10.png)

## Validation aspects

JSON schema field: **validation / messages**

Definition
* A validation messages appears in red close to the field it applies to. It can exist only if a constraint has been defined in the data model, like a pattern (ex: e-mail), a datatype (ex: date as 4 integer) or a required field.

![validation_example](https://user-images.githubusercontent.com/8154915/75450742-a7391780-596f-11ea-965d-84751b69621b.png)

## 5. Error handling and help

## 6. Wait time management



*Translated with www.DeepL.com/Translator (free version)*
