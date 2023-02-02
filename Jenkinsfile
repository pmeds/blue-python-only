pipeline {
  agent any
  stages {
    stage('get excel and python script') {
      steps {
        echo 'Getting the excel and python files'
        sh '''chmod 754 CSV_formatter.py
chmod 754 post_req.py'''
      }
    }

    stage('Running formatter') {
      steps {
        echo 'Running CSV formatter and generating CSV files'
        sh 'python3 CSV_formatter.py'
      }
    }

    stage('Upload to games') {
      steps {
        echo 'checking if there is a csv file for games'
        fileExists 'games-upload.csv'
        sh 'python3 post_req.py games-upload.csv'
      }
    }

    stage('Upload to general') {
      steps {
        echo 'Checking if there is a CSV file for general'
        fileExists 'test-general-upload.csv'
        sh 'python3 post_req.py general-upload.csv'
      }
    }

  }
}