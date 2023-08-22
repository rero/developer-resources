# Editor configurations

## Commit messages

For commit messages, your editor should help you to :

- Write titles shorter than 51 chars.
- Wrap body at 72 chars.
- Check the spelling at least in english.

### VI, Vim, Neovim

```bash
" Filetype detection
filetype plugin on

autocmd FileType gitcommit set textwidth=72
set colorcolumn=+1 " Colors the tw+1 column
autocmd FileType gitcommit set colorcolumn+=51
autocmd FileType gitcommit setlocal spell
autocmd FileType gitcommit setlocal spelllang=en
```
