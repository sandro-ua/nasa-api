pipelineJob('NASA_REGRESSION_DSL_GENERATED') {
    definition {
        cpsScm {
            scm {
                github('https://github.com/sandro-ua/nasa-api')
            }       
			scriptPath('JenkinsFile.groovy')
        }
    }
}