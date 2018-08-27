node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

	sh "cd /home/vagrant/challenge/; sudo docker build -t python-teste2 ."
        echo "Image build complete"
    }


   stage('Docker test'){
      sh 'sudo docker run -d --rm python-teste2 -p 5000:5000 -p 8000:8000'
    }

    stage('Clean Docker test'){
      sh 'sudo docker rmi python-teste2'
    }

    stage('Push image') {
        /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. */
	 withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh 'docker push wendellbarc/python-teste2:latest'
        }
    }
}
