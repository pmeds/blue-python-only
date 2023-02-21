pipeline {
  agent any
  stages {
    stage('get excel and python script') {
      steps {
        echo 'Getting the excel and python files'
        sh '''ls -la
chmod 754 CSV_formatter.py
chmod 754 post_req_prod.py'''
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
          if (fileExists('test-games-upload-locale.csv')) {
            sh 'echo "uploading games rules"'
            sh 'python3 post_req_prod.py test-games-upload-locale.csv'
            sh 'cp test-games-upload-locale.csv /resources/jenkins-ekvdata/games-upload-locale-`date +%Y-%m-%d-%H-%M`.csv'
          }
        }

      }
    }

    stage('Upload to support') {
      steps {
        echo 'Checking if there is a CSV file for support'
        script {
          if (fileExists('test-support-upload-locale.csv')) {
            sh 'echo "uploading support rules"'
            sh 'python3 post_req_prod.py test-support-upload-locale.csv'
            sh 'cp test-support-upload-locale.csv /resources/jenkins-ekvdata/test-support-upload-locale-`date +%Y-%m-%d-%H-%M`.csv'
          }
        }

      }
    }

    stage('Upload General') {
      steps {
        echo 'Checking for CSV for General'
        script {
          if (fileExists('test-general-upload-locale.csv')) {
            sh 'echo "uploading general rules"'
            sh 'python3 post_req_prod.py test-general-upload-locale.csv'
            sh 'cp test-general-upload-locale.csv /resources/jenkins-ekvdata/test-general-upload-locale-`date +%Y-%m-%d-%H-%M`.csv'
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
