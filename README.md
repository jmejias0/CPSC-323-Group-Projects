
# CPSC-323 Group Projects

This repository contains our CPSC-323 Compiler assignments, source code, and documentation. We use GitHub to collaborate, manage updates, and maintain a history of changes throughout the project.

## RAT26F Grammar Rules

The following grammar rules (R1–R28) define the syntax of the RAT26F programming language.

### Original Grammar (R1–R28)

- **R1:** `<Rat26F> ::= <Opt Function Definitions> @ <Opt Declaration List> @ <Statement List>`
- **R2:** `<Opt Function Definitions> ::= <Function Definitions> | <Empty>`
- **R3:** `<Function Definitions> ::= <Function> <Function Definitions Prime>`
- **R4:** `<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>`
- **R5:** `<Opt Parameter List> ::= <Parameter List> | <Empty>`
- **R6:** `<Parameter List> ::= <Parameter> <Parameter List Prime>`
- **R7:** `<Parameter> ::= <IDs> <Qualifier>`
- **R8:** `<Qualifier> ::= integer | boolean | real`
- **R9:** `<Body> ::= { <Statement List> }`
- **R10:** `<Opt Declaration List> ::= <Declaration List> | <Empty>`
- **R11:** `<Declaration List> ::= <Declaration> <Declaration List Prime>`
- **R12:** `<Declaration> ::= <Qualifier> <IDs>`
- **R13:** `<IDs> ::= <Identifier> <IDs Prime>`
- **R14:** `<Statement List> ::= <Statement> <Statement List Prime>`
- **R15:** `<Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>`
- **R16:** `<Compound> ::= { <Statement List> }`
- **R17:** `<Assign> ::= <Identifier> = <Expression> ;`
- **R18:** `<If> ::= if ( <Condition> ) <Statement> <If prime>`
- **R19:** `<Return> ::= return <Return Prime>`
- **R20:** `<Print> ::= put ( <Expression> );`
- **R21:** `<Scan> ::= get ( <IDs> );`
- **R22:** `<While> ::= while ( <Condition> ) <Statement>`
- **R23:** `<Condition> ::= <Expression> <Relop> <Expression>`
- **R24:** `<Relop> ::= == | != | > | < | <= | >=`
- **R25:** `<Expression> ::= <Term> <Expression Prime>`
- **R26:** `<Term> ::= <Factor> <Term Prime>`
- **R27:** `<Factor> ::= - <Primary> | <Primary>`
- **R28:** `<Primary> ::= <Identifier> <Primary Prime> | <Integer> | ( <Expression> ) | <Real> | true | false`
- **R29:** `<Empty> ::= ε`

---

## Additional Grammar Rules (R29–R38)

The following rules were introduced after applying left factorization and removing left recursion where necessary.

- **R30:** `<Primary Prime> ::= ( <IDs> ) | ε`
- **R31:** `<Function Definitions Prime> ::= <Function Definitions> | ε`
- **R32:** `<Parameter List Prime> ::= <Parameter List> | ε`
- **R33:** `<Declaration List Prime> ::= <Declaration List> | ε`
- **R34:** `<IDs Prime> ::= <IDs> | ε`
- **R35:** `<Statement List Prime> ::= <Statement List> | ε`
- **R36:** `<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | ε`
- **R37:** `<Expression Prime> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | ε`
- **R38:** `<Return Prime> ::= ; | <Expression> ;`
- **R39:** `<If Prime> ::= fi | else <Statement> fi`

---

## Development Notes

- After eliminating left recursion elimination and left factorization where needed
 there is a total of 38 functions

