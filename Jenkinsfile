pipeline {
  agent any
  stages {
    stage('get excel and python script') {
      steps {
        echo 'Getting the excel and python files'
        sh '''ls -la
chmod 754 CSV_formatter.py
chmod 754 post_req.py'''
      }
    }

    stage('Running formatter') {
      steps {
        echo 'Running CSV formatter and generating CSV files'
        sh 'python3 CSV_formatter.py'
        sh 'ls -la'
      }
    }

    stage('Upload to games') {
      steps {
        echo 'checking if there is a csv file for games'
        script {
          if (fileExists('test-games-upload.csv')) {
            sh 'echo "uploading games rules"'
            sh 'python3 post_req.py test-games-upload.csv'
          }
        }

      }
    }

    stage('Upload to support') {
      steps {
        echo 'Checking if there is a CSV file for support'
        script {
          if (fileExists('test-support-upload.csv')) {
            sh 'echo "uploading support rules"'
            sh 'python3 post_req.py test-support-upload.csv'
          }
        }

        script {
          if (fileExists('test-support-upload.csv')) {
            sshagent (credentials: ['git-log']) {
              sh 'cp support-upload.csv /resources/jenkins-ekvdata/support-upload-`date +%Y-%m-%d-%H-%M`.csv'
              sh '''cd /resources/jenkins-ekvdata
pwd
git pull
git add .
git commit -m "upload support `date +%Y-%m-%d-%H-%M`"
git branch -M main
git remote -v
git push origin main'''
            }
          }
        }

      }
    }

    stage('Upload General') {
      steps {
        echo 'Checking for CSV for General'
        script {
          if (fileExists('test-general-upload.csv')) {
            sh 'echo "uploading general rules"'
            sh 'python3 post_req.py test-general-upload.csv'
          }
        }

      }
    }

    stage('Delete environment') {
      steps {
        cleanWs(cleanWhenAborted: true, cleanWhenFailure: true, cleanWhenNotBuilt: true, cleanWhenSuccess: true)
      }
    }

  }
}