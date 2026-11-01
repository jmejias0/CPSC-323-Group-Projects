
# CPSC-323 Group Projects

This repository contains our CPSC-323 Compiler assignments, source code, and documentation. We use GitHub to collaborate, manage updates, and maintain a history of changes throughout the project.

## RAT26F Grammar Rules

The following grammar rules (R1–R28) define the syntax of the RAT26F programming language.

Rules marked with ⭐ require modifications to remove left recursion or perform left factorization.

### Original Grammar (R1–R28)

- **R1:** `<Rat26F> ::= <Opt Function Definitions> @ <Opt Declaration List> @ <Statement List>`
- **R2:** `<Opt Function Definitions> ::= <Function Definitions> | <Empty>`
- **R3:** ⭐ `<Function Definitions> ::= <Function> | <Function> <Function Definitions>`
- **R4:** `<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>`
- **R5:** `<Opt Parameter List> ::= <Parameter List> | <Empty>`
- **R6:** ⭐ `<Parameter List> ::= <Parameter> | <Parameter> , <Parameter List>`
- **R7:** `<Parameter> ::= <IDs> <Qualifier>`
- **R8:** `<Qualifier> ::= integer | boolean | real`
- **R9:** `<Body> ::= { <Statement List> }`
- **R10:** `<Opt Declaration List> ::= <Declaration List> | <Empty>`
- **R11:** ⭐ `<Declaration List> ::= <Declaration> ; | <Declaration> ; <Declaration List>`
- **R12:** `<Declaration> ::= <Qualifier> <IDs>`
- **R13:** ⭐ `<IDs> ::= <Identifier> | <Identifier> , <IDs>`
- **R14:** ⭐ `<Statement List> ::= <Statement> | <Statement> <Statement List>`
- **R15:** `<Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>`
- **R16:** `<Compound> ::= { <Statement List> }`
- **R17:** `<Assign> ::= <Identifier> = <Expression> ;`
- **R18:** ⭐ `<If> ::= if ( <Condition> ) <Statement> fi | if ( <Condition> ) <Statement> else <Statement> fi`
- **R19:** ⭐ `<Return> ::= return ; | return <Expression> ;`
- **R20:** `<Print> ::= put ( <Expression> );`
- **R21:** `<Scan> ::= get ( <IDs> );`
- **R22:** `<While> ::= while ( <Condition> ) <Statement>`
- **R23:** `<Condition> ::= <Expression> <Relop> <Expression>`
- **R24:** `<Relop> ::= == | != | > | < | <= | >=`
- **R25:** ⭐ `<Expression> ::= <Expression> + <Term> | <Expression> - <Term> | <Term>`
- **R26:** ⭐ `<Term> ::= <Term> * <Factor> | <Term> / <Factor> | <Factor>`
- **R27:** `<Factor> ::= - <Primary> | <Primary>`
- **R28:** ⭐ `<Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false`

---

## Additional Grammar Rules (R29–R38)

The following rules were introduced after applying left factorization and removing left recursion where necessary.

- **R29:** `<Primary Prime> ::= ( <IDs> ) | ε`
- **R30:** `<Function Definitions Prime> ::= <Function Definitions> | ε`
- **R31:** `<Parameter List Prime> ::= <Parameter List> | ε`
- **R32:** `<Declaration List Prime> ::= <Declaration List> | ε`
- **R33:** `<ID's Prime> ::= <IDs> | ε`
- **R34:** `<Statement List Prime> ::= <Statement List> | ε`
- **R35:** `<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | ε`
- **R36:** `<Expression Prime> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | ε`
- **R37:** `<Return Prime> ::= ; | <Expression>`
- **R38:** `<If Prime> ::= fi | else <Statement> fi`

---

## Development Notes

- Implement the required grammar rules as parser functions.
- Apply left recursion elimination and left factorization where needed.
- Test parser functions using valid and invalid RAT26F inputs.
- Use Git commits to document changes and track project progress.
