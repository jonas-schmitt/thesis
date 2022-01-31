import subprocess as sp
import os
import shutil
import pathlib

base_dir = "./tree_generation_scripts"
target_dir ="./figures/trees"
check_if_exists = False
for i, file_name in enumerate(os.listdir(base_dir)):
    if file_name.endswith(".dot") and (not check_if_exists or pathlib.Path(file_name.replace(".dot", ".pdf")).is_file()):
        output = sp.run(["dot2tex", "-c", "-f", "tikz", "--prog", "dot", "--preproc", f"{base_dir}/{file_name}"], stdout=sp.PIPE).stdout.decode("utf-8")
        tmp_file_name = f"tmp{i}.dot"
        with open(f"{base_dir}/{tmp_file_name}", "w") as tmp_file:
            tmp_file.write(output)
        output = sp.run(["dot2tex", "-c", "-f", "tikz", "--prog", "dot", "-tmath", f"{base_dir}/{tmp_file_name}"], stdout=sp.PIPE).stdout.decode("utf-8")
        output_file_name = file_name.replace(".dot", ".tex")
        with open(f"{base_dir}/{output_file_name}", "w") as output_file:
            output_file.write(output)
        cwd = os.getcwd()
        os.chdir(base_dir)
        res = sp.run(["pdflatex", output_file_name], stdout=sp.PIPE)
        os.chdir(cwd)
        pdf_file_name = file_name.replace(".dot", ".pdf")
        shutil.move(f"{base_dir}/{pdf_file_name}", f"{target_dir}/{pdf_file_name}")
        os.remove(f"{base_dir}/{tmp_file_name}")
        os.remove(f"{base_dir}/{output_file_name}")
        tmp = file_name.replace(".dot", ".aux")
        os.remove(f"{base_dir}/{tmp}")
        tmp = file_name.replace(".dot", ".log")
        os.remove(f"{base_dir}/{tmp}")




        # print(output)
        # dot2tex -c -f tikz --prog dot --preproc tree_generation_scripts/gp_expression_tree1.dot > tmp.dot
        # dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_expression_tree1.tex
        # pdflatex gp_expression_tree1.tex

