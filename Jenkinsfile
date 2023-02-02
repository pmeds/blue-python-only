pipeline {
  agent any
  stages {
    stage('get excel and python script') {
      steps {
        echo 'Getting the excel and python files'
        sh 'chmod 754 CSV_formatter.py'
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
        sh 'echo'
      }
    }

    stage('Upload to general') {
      steps {
        sh 'echo'
      }
    }

  }
}