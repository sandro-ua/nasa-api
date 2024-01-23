pipelineJob('NASA_REGRESSION_DSL_GENERATED') {
    definition {
        cpsScm {
            scm {
                git {
                    // Git repository URL
                    remote {
                        git 'https://github.com/sandro-ua/nasa-api'
                    }
                    branch 'master'
                }
            }
            scriptPath('JenkinsFile.groovy')
        }
    }
}
