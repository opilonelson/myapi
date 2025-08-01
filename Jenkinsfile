pipeline {
  agent any

  environment {
    DOCKER_IMAGE = "norego18/myapi"
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/opilonelson/myapi.git'
        
      }
    }

    stage('Build') {
      steps {
        script {
          docker.build(DOCKER_IMAGE)
        }
      }
    }

    stage('Test') {
      steps {
        sh 'docker run --rm ${DOCKER_IMAGE} pytest tests/'
      }
    }

    stage('Push Image') {
      when {
        branch 'main'
      }
      steps {
        withDockerRegistry([credentialsId: 'dockerhub-creds']) {
          script {
            docker.image(DOCKER_IMAGE).push()
          }
        }
      }
    }

    stage('Deploy') {
      when {
        branch 'main'
      }
      steps {
        sh 'docker-compose down'
        sh 'docker-compose up -d'
      }
    }
  }

  post {
    failure {
      echo "Build failed!"
    }
    success {
      echo "Build and deployment successful!"
    }
  }
}
