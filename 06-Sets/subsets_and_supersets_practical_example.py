required_skills = [
    "python", "github", "linux"
]

candidates = {
    "anna": {"java", "linux", "windows", "github", "python", "full stack"},
    "bob": {"github", "linux", "python"},
    "carol": {"linux", "javascript", "html", "github", "python"},
    "daniel": {"pascal", "java", "c++", "github"},
    "ekani": {"html", "css", "github", "python", "linux"},
    "fenna": {"linux", "pascal", "java", "c", "lisp", "modula-2", "perl", "github"}
}

interviewees = set()
# for candidate, skills in candidates.items():
#     if skills.issuperset(required_skills):
#         interviewees.add(candidate)
#
# print(interviewees)


for candidate, skills in candidates.items():
    if skills > set(required_skills):
        interviewees.add(candidate)

print(interviewees)
