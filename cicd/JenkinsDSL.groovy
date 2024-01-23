pipelineJob('NASA_REGRESSION_DSL_GENERATED') {
    definition {
        cpsScm {
            scm {
                git {
                    remote {
                        git 'https://github.com/sandro-ua/nasa-api'
                    }
                }
            }
            scriptPath('JenkinsFile.groovy')
        }
    }
}