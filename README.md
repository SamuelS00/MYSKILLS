# myskills

Biblioteca reutilizável de Agent Skills, baseada na [especificação aberta](https://agentskills.io/specification). O conteúdo canônico fica em `skills/` e pode ser usado por diferentes agentes e modelos, inclusive OpenCode com DeepSeek.

## Estrutura

- `skills/<nome>/SKILL.md`: metadados e instruções da skill.
- `skills/<nome>/references/`: documentação complementar, somente quando necessária.
- `skills/<nome>/scripts/`: automação opcional.
- `tests/`: testes do validador.
- `validate_skills.py`: verificação local, sem serviços externos.
- `AGENTS.md` e `CLAUDE.md`: regras compartilhadas e entrada para Claude Code.

A primeira skill é `skill-creator`. Não há diretórios opcionais vazios.

## Criar uma skill

1. Confira se já existe uma skill equivalente e delimite objetivo, gatilhos e responsabilidades.
2. Crie `skills/<nome>/SKILL.md` com frontmatter YAML (`name` e `description`) e instruções objetivas em inglês.
3. Adicione referências ou scripts apenas quando forem úteis. Use progressive disclosure: detalhes longos ficam fora do `SKILL.md` e são lidos sob demanda.
4. Execute `python3 validate_skills.py` e `python3 -m unittest discover -s tests`.
5. Teste situações positivas, negativas e de limite antes de publicar.

Exemplo: peça ao agente “Create a skill for reviewing database migrations” para usar `skill-creator` quando ela estiver instalada.

## Instalação e descoberta

Os comandos abaixo são exemplos para executar na raiz de um projeto consumidor, com o caminho absoluto desta biblioteca em `MYSKILLS_DIR`. Links simbólicos mantêm uma única fonte de verdade. Em ambientes que não aceitam links simbólicos, use um mecanismo de instalação que preserve o diretório inteiro da skill.

```sh
MYSKILLS_DIR=/caminho/absoluto/para/myskills
mkdir -p .claude/skills .agents/skills
ln -s "$MYSKILLS_DIR/skills/skill-creator" .claude/skills/skill-creator
ln -s "$MYSKILLS_DIR/skills/skill-creator" .agents/skills/skill-creator
```

- **Claude Code:** descobre skills em `.claude/skills/<nome>/SKILL.md` no projeto ou `~/.claude/skills/` no usuário. Use o link em `.claude/skills/`.
- **OpenAI Codex:** usa `.agents/skills/<nome>/SKILL.md` no projeto ou `~/.agents/skills/` no usuário. Use o link em `.agents/skills/`.
- **OpenCode:** descobre `.opencode/skills/` e também os diretórios de compatibilidade `.claude/skills/` e `.agents/skills/`. Um único link em `.agents/skills/` atende Codex e OpenCode. A seleção da skill depende de nome, descrição e permissões configuradas no OpenCode; o modelo escolhido, como DeepSeek, não altera o formato dos arquivos.

Fontes oficiais: [Agent Skills](https://agentskills.io/specification), [Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://developers.openai.com/api/reference/cli), [OpenCode](https://docs.opencode.ai/docs/skills/).
