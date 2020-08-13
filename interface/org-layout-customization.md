# Customization

Tip & tricks about RERO-ILS theme customization.

## Layout customization per organization

### In brief

* Each organization page have a `<body id="view-code">` where **code** is the
  organization code, ie `view-highlands`.
* Each organization page will download a `code.css` file where **code** is
  the organization code, ie `highlands.css`.
* The CSS is located on URL given by the
  `RERO_ILS_THEME_ORGANISATION_CSS_ENDPOINT` variable, ie
  `https://resources.rero.ch/ils/test/`.

### Some explanation

Each organization have a *code*. For example *Libraries of the Britisch Minitry
of Magic* has the code `highlands`. This implies a specific URL:
`https://localhost:5000/highlands/`.

On this page, the code `highlands` is used for the `<body>` tag of each
page:

```html
<body id="view-highlands">
```

which can be used to *customize* each organization page. In example:

```css
body#view-highlands nav.rero-ils-header {
    background-color: #333333 !important;
}

body#view-highlands nav.rero-ils-header img.rero-ils-logo {
    display: none;
}

div#highlands-logo {
    content: url('https://resources.rero.ch/ils/test/images/logo-highlands.png');
    max-height: 44px !important;
}
```

This will change the logo and the color of the header for `highlands`
organization page.

For this to work, you need to put your `code.css` (ie `highlands.css`) in
`RERO_ILS_THEME_ORGANISATION_CSS_ENDPOINT` directory.

For example it currently point out `https://resources.rero.ch/ils/test/` which
implies to have `https://resources.rero.ch/ils/test/highlands.css` on this
server.
