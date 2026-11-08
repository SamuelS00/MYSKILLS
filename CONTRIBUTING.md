# Contribuindo

Para adicionar ou atualizar uma skill, leia `AGENTS.md`, procure uma equivalente e defina um escopo específico. Edite somente os arquivos necessários e mantenha o conteúdo da skill em inglês. A documentação voltada a leitores deste repositório pode ser escrita em português.

## Checklist

- [ ] Nome em kebab-case, igual ao diretório e ao campo `name`.
- [ ] `description` específica, indicando quando usar a skill.
- [ ] Instruções curtas, práticas e sem dependência desnecessária de fornecedor.
- [ ] Referências e scripts apenas quando necessários; sem diretórios vazios.
- [ ] Casos positivos, negativos e de limite considerados.
- [ ] `python3 validate_skills.py` e `python3 -m unittest discover -s tests` executados.
- [ ] Alterações relacionadas somente ao objetivo da contribuição; commit e push após validação.

## Commits

Use Conventional Commits: `tipo(escopo opcional): descrição curta`.
Tipos aceitos: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore` e `revert`.
Escreva o assunto no imperativo, sem ponto final, e mantenha cada commit focado em uma mudança.
Use `!` antes de `:` e explique a incompatibilidade no corpo com `BREAKING CHANGE:` quando necessário.

Exemplos:

- `feat(skills): add repository search skill`
- `fix(validation): reject mismatched skill names`
- `docs: clarify contribution workflow`

O hook versionado em `.githooks/commit-msg` verifica o formato do assunto. Ative-o neste clone com `git config core.hooksPath .githooks`.
