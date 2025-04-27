import numpy as np
import wandb

entity = "2021csb1100-indian-institute-of-technology-ropar"
project = "Strategically Conservative Q Learning"
metric_key = "eval/d4rl_score"

api = wandb.Api()


def final_eval_scores(run_ids):
    final_scores = []
    for run_id in run_ids:
        run = api.run(f"{entity}/{project}/{run_id}")
        history = run.history(keys=[metric_key])

        eval_scores = history[metric_key].dropna().to_numpy()

        if len(eval_scores) < 5:
            raise ValueError(f"Run {run_id} has less than 5 evaluation scores!")

        last_5_scores = eval_scores[-5:]

        avg_score = np.mean(last_5_scores)

        final_scores.append(avg_score)
        seed = run.config.get("seed", "unknown_seed")
        run_name = run.name
        print(
            f"Run: {run_id}, Seed: {seed}, Name: {run_name} Average of last 5 eval scores: {avg_score:.1f}"
        )

    final_scores = np.array(final_scores)
    mean_score = np.mean(final_scores)
    std_score = np.std(final_scores)

    print(f"{mean_score:.1f} ± {std_score:.1f}\n")


# SCQ
# scq-antmaze
run_ids = ["4hwcjy8n", "hyqsb00m", "ire9vi4v", "p2fjd41w", "z7wpbj5g"]
final_eval_scores(run_ids)

# scq-halfcheetah
run_ids = ["do8fis17", "l56zz9sz", "36j77evq", "f3bukm8j", "19n0fy2j"]
final_eval_scores(run_ids)

# scq-hopper
run_ids = ["wv8scnnf", "u5tkr3vx", "kb9q8boo", "pocffru0", "b886zzom"]
final_eval_scores(run_ids)

# scq-walker2d
run_ids = ["vy7p1fx9", "zdpgvl0m", "75zthuzs", "6e5xyyta", "z6y2vbe2"]
final_eval_scores(run_ids)

# Approach 1
# scq-ps-antmaze
run_ids = ["eu0h9flk", "1rmrzxsr", "1970po88", "oroalqzt", "qz8n1zoe"]
final_eval_scores(run_ids)

# scq-ps-halfcheetah
run_ids = ["f5g59tyt", "g3n4fanj", "n93bpez3", "srlgok1k", "ulsc32gs"]
final_eval_scores(run_ids)

# scq-ps-hopper
run_ids = ["qaienz44", "y1m6a19b", "993zhro7", "q4qf2rn0", "3oai72wz"]
final_eval_scores(run_ids)

# scq-ps-walker2d
run_ids = ["57yfyye1", "9608gz9a", "vju8pwht", "bffxnixx", "u423ck6d"]
final_eval_scores(run_ids)

# Approach 2
# scq-as-antmaze
run_ids = ["1ffg8tfx", "61kba6jl", "745c595f", "wge1ux22", "ufatjkja"]
final_eval_scores(run_ids)

# scq-as-halfcheetah
run_ids = ["sdgfvxo0", "b91i4q8e", "9otf5fcx", "zilr4ttm", "vd97wexf"]
final_eval_scores(run_ids)

# scq-as-hopper
run_ids = ["b51qd2gt", "567gta45", "s12fl2o3", "pbhdgai2", "ggyhks3x"]
final_eval_scores(run_ids)

# scq-as-walker2d
run_ids = ["xzgicj69", "61o2e117", "67kdckic", "7etx668o", "6a5adz5g"]
final_eval_scores(run_ids)
