# scripts 📃
Useful scripts for daily work


## ✅ `gitMergeFlow.py`    
  Merge between branches in a roll.
  
  ```sh
  # usage
  python gitMergeFlow.py <branch1> <branch2> ... <branchN>
    
  # example
  # code form `dev` branch will be merge into `test`, then into `pre`
  python gitMergeFlow.py dev test pre
  ```

## ✅ buildJenkinsJobs.py

Build Jenkins jobs with scripts.

### Usage

First of all, add an file named `config.local.json` in the same directory with `buildJenkinsJobs.py`，and config your Jenkins user ID and API Token in it.

```json
{
  "jenkins": {
    "user_id": "your_user_id",
    "api_token": "your_api_token"
  }
}
```

Then, run the script with the environment name you want to build. ***By the way, the script can not be used out of box.*** You need to modify it to fit your own Jenkins jobs.

```bash
python buildJenkinsJobs.py [-h] env1 [env2...]
```

## ✅ `mergeAndBuildJenkins.py`

A combination of `gitMergeFlow.py` and `buildJenkinsJobs.py`. It will merge branches and if you run the scripts with `--build=true`, it will also build Jenkins jobs.

### Usage

```bash
mergeAndBuildJenkins.py [-h] branch1 [branch2...] [--build=true]
```

 