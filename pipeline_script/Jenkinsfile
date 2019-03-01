pipeline {
	agent any
	stages {
		stage ('Git-checkout'){
			steps{	
				echo "Checking from Git Repo";
				git "https://github.com/smailmedjadi/jenkins_blueocean.git"
			}
		}
		stage ('Build'){
			steps{
				echo "Building the checkout project";
				bat "pipeline_script\build.bat"
			}
		}
		stage ('Unit-test'){
			steps{
				echo "Verify project JUnit";
				bat "pipeline_script\Unit.bat"			
			}
		}
		stage ('Quality-Gate'){
			steps{
				echo "Verifying Quality Gates";
				bat "pipeline_script\Quality.bat"
			}
		}
		stage ('Deploy'){
			steps{
				echo "Deploying with XDeploy on ASS Enivronment";
				bat "pipeline_script\Deploy.bat"
			}
		}
	}
	
	post {
		always {
			echo''
		}
        failure {
        	echo 'Message if pipeline fails to execute'
        }
        success{
        	echo 'Pipeline success message'
        } 
        
        unstable{
    		echo 'Pipeline unstable message'
		}
        
        changed{
			echo 'If the messages shows up, it means the state of the pipeline has changed'
		}
	}
}
	
	 
	 
	 
}