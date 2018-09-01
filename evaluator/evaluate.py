import subprocess
class Eval:

    def __init__(self,trec_file,qrels):

        self.trec_file = trec_file
        self.qrels = qrels
        self.metrics =["map","ndcg_cut.20","P.10","P.5"]

    @staticmethod
    def run_command(command):
        p = subprocess.Popen(command,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             shell=True)
        return iter(p.stdout.readline, b'')

    def run_evaluation(self):
        score_data = []
        for metric in self.metrics:
            command = "./trec_eval -m " + metric + " " + self.qrels + " " + self.trec_file
            for output_line in Eval.run_command(command):
                score = output_line.split()[-1].rstrip()
                score = str(score).replace("b'", "")
                score = score.replace("'", "")
                score_data.append((metric, str(score)))

        with open("results_of_retrieval",'w') as results_file:
            for result in score_data:
                record = result[0]+"\t"+result[1]
                print(record)
                results_file.write(record+"\n")


