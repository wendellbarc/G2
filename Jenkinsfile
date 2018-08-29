node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build new image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

	sh "docker build -t python-alpine ."
        echo "Image build complete"
    }


   stage('Testing new image'){
      sh 'docker run -d --rm  -p 5001:5000 --name python-temp python-alpine'
      sh 'docker port python-temp'
    }

    stage('Clean Docker test'){
      sh 'docker stop python-temp'
    }

    stage('Deploy new image') {
        /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. */
	 / * withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh 'docker push wendellbarc/python-teste2:latest' */
          sh 'docker stop python-alpine'
          sh 'docker rm python-alpine' 
          sh 'docker run -u root -d --restart always -p 8000:8000 -p 5000:5000 --name python-alpine python-alpine'
        }
    }
}
