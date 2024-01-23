pipelineJob('NASA_REGRESSION_DSL_GENERATED') {
    definition {
        cpsScm {
            scm {
                git('https://github.com/sandro-ua/nasa-api')
            }
			scriptPath('cicd/JenkinsFile.groovy')
        }
    }
}