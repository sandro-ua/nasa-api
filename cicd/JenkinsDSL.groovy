pipelineJob('NASA_REGRESSION_2') {
    definition {
        cpsScm {
            scm {
                git {
                    remote {
                        github('https://github.com/sandro-ua/nasa-api')
                    }
                }
            }
            scriptPath('JenkinsFile.groovy')
        }
    }
}