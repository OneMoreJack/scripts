import argparse
import json
import os

import jenkins

# 读取配置文件
configPath = os.path.join(os.path.dirname(
    __file__), 'config.local.json')
jenkinsConfig = json.load(open(configPath, 'r')).get('jenkins')


jenkins_server_url = 'your_jenkins_url' # TODO replace with your jenkins url
user_id = jenkinsConfig.get('user_id')
api_token = jenkinsConfig.get('api_token')


server = jenkins.Jenkins(
    jenkins_server_url, username=user_id, password=api_token)


# 构建开发环境
def buildDevJob():
    server.build_job(
        'jenkins_job_name', # TODO replace with your jenkins job name
        parameters={
          # add params here if needed
        }
    )
    printLog('开发')


def printLog(environment: str):
    print(' 🚀 【{}】环境已发起 jenkins 构建'.format(environment))


def runJobs(envs):
    print('\n' + '=' * 40 + '\n')
    print('BUILDING JENKINS JOBS...' + '\n')
    if "dev" in envs:
        buildDevJob()
    # add more jobs here if needed
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build jenkins jobs")
    parser.add_argument('jobs', help="names of jobs to build", nargs='+')
    args = parser.parse_args()
    runJobs(args.jobs)
