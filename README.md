Students Manager Application
 
Este projeto implementa um sistema para gerenciar estudantes, cursos e disciplinas. Ele permite adicionar estudantes, listar os estudantes aprovados com base em uma nota mínima e gerenciar os dados de cursos e disciplinas. O código foi estruturado com classes para representar as entidades principais e inclui funcionalidades interativas por meio de entrada do usuário.
 

Pré-requisitos
 
Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados no seu ambiente:

Python 3.8 ou superior
Um terminal ou ambiente que suporte a execução de scripts Python
 

Estrutura do Projeto
 
O projeto está organizado em dois arquivos principais:

models.py: Contém as classes principais para representar disciplinas (Subject), cursos (Course) e estudantes (Student).
manager.py: Contém a classe StudentsManager, responsável por gerenciar os estudantes, além do código principal de execução.
 

Como Executar o Projeto
 

Passo 1: Clone o repositório
 
Primeiro, clone o repositório para o seu ambiente local:


git clone https://github.com/sua-organizacao/students-manager.git  
 
Entre no diretório do projeto:


cd students-manager  
 
 

Passo 2: Execute o programa principal
 
Execute o arquivo manager.py para iniciar o sistema interativo:


python manager.py  
 
 

Passo 3: Interaja com o sistema
 
O programa é interativo e solicitará informações do usuário. Aqui estão as principais funcionalidades:

Adicionar um estudante
Quando o programa solicitar, insira as seguintes informações:
Nome do estudante
Nome do curso
Nome da disciplina
Nome do professor
Nota do estudante
Escolha a ação add para adicionar o estudante à lista.
Listar estudantes aprovados
Escolha a ação list para listar os estudantes aprovados.
Insira a nota mínima para aprovação.
O programa exibirá os estudantes aprovados com base na nota mínima.
Encerrar o programa
Digite exit para sair do programa.
 

Exemplo de Uso
 
Aqui está um exemplo de uma execução típica do programa:


Enter the student name: João  
Enter the course name: Matemática  
Enter the subject name: Álgebra  
Enter the professor name: Prof. Silva  
Enter the grade: 85  
Enter the action (list, add): add  
  
Enter the student name: Maria  
Enter the course name: Física  
Enter the subject name: Mecânica  
Enter the professor name: Prof. Santos  
Enter the grade: 70  
Enter the action (list, add): list  
Enter the minimum grade: 60  
  
Student: João, Course: Matemática  
Student: Maria, Course: Física  
  
Type 'exit' to quit or press Enter to continue:  
 
 

Estrutura das Classes
 

Subject
Representa uma disciplina com os seguintes atributos:

name (nome da disciplina)
professor (nome do professor)
grade (nota do estudante)

Métodos:
approved(min: float) — Retorna True se a nota do estudante for maior ou igual à nota mínima.
 

Course
Representa um curso com os seguintes atributos:

course_name (nome do curso)
subjs (lista de disciplinas)

Métodos:
calculate_mean() — Calcula a média das notas das disciplinas.
approved(min: float) — Retorna True se o estudante estiver aprovado em todas as disciplinas.
 

Student
Representa um estudante com os seguintes atributos:

name (nome do estudante)
course (curso do estudante)

Métodos:
approved(min: float) — Retorna True se o estudante estiver aprovado no curso.
 

StudentsManager
Gerencia uma lista de estudantes com os seguintes métodos:

from_input(first: bool) — Cria uma instância do gerenciador de estudantes com os dados inseridos pelo usuário.
from_dict(data: dict) — Cria uma instância do gerenciador a partir de um dicionário (geralmente carregado de um arquivo JSON).
add_student_from_input() — Adiciona um estudante à lista com os dados fornecidos pelo usuário.
get_approved_course_students_list(min: float) — Retorna uma lista de estudantes aprovados com base em uma nota mínima.

