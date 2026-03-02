// pipeline {
//     agent any

//     stages {

//         stage('Checkout Code') {
//             steps {
//                 git branch: 'main',
//                     url: 'https://github.com/jenish11052004/scientific-calculator.git'
//             }
//         }

//         stage('Set Up Python Environment') {
//             steps {
//                 sh 'python3 -m venv venv'
//                 sh './venv/bin/pip install --upgrade pip'
//                 sh './venv/bin/pip install -r requirements.txt'
//             }
//         }

//         stage('Run Tests') {
//             steps {
//                 sh './venv/bin/pytest -v'
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 sh "docker build -t jenish011/scientific-calculator:${BUILD_NUMBER} ."
//             }
//         }

//         stage('Push Docker Image') {
//             steps {
//                 withCredentials([usernamePassword(
//                     credentialsId: 'dockerhub-creds',
//                     usernameVariable: 'DOCKER_USER',
//                     passwordVariable: 'DOCKER_PASS'
//                 )]) {
//                     sh """
//                         echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
//                         docker push jenish011/scientific-calculator:${BUILD_NUMBER}
//                     """
//                 }
//             }
//         }
//     }

//     post {

//         success {
//             emailext (
//                 subject: "SUCCESS: Build #${BUILD_NUMBER} - ${JOB_NAME}",
//                 body: """
//                 BUILD SUCCESS !!!

//                 Job Name: ${JOB_NAME}
//                 Build Number: ${BUILD_NUMBER}
//                 Build URL: ${BUILD_URL}

//                 Docker Image Pushed:
//                 jenish011/scientific-calculator:${BUILD_NUMBER}

//                 All tests passed and image pushed successfully.
//                 """,
//                 to: "jenishvekariya011@gmail.com"
//             )
//         }

//         failure {
//             emailext (
//                 subject: "FAILED: Build #${BUILD_NUMBER} - ${JOB_NAME}",
//                 body: """
//                 BUILD FAILED !!!

//                 Job Name: ${JOB_NAME}
//                 Build Number: ${BUILD_NUMBER}
//                 Check Logs: ${BUILD_URL}

//                 Please review the error immediately.
//                 """,
//                 to: "jenishvekariya011@gmail.com"
//             )
//         }
//     }
// }



pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/jenish11052004/scientific-calculator.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                    docker build -t jenish011/scientific-calculator:${BUILD_NUMBER} .
                    docker tag jenish011/scientific-calculator:${BUILD_NUMBER} jenish011/scientific-calculator:latest
                """
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push jenish011/scientific-calculator:${BUILD_NUMBER}
                        docker push jenish011/scientific-calculator:latest
                    '''
                }
            }
        }
    }

    post {

        success {
            emailext (
                subject: "SUCCESS: Build #${BUILD_NUMBER} - ${JOB_NAME}",
                body: """
                BUILD SUCCESS !!!

                Job Name: ${JOB_NAME}
                Build Number: ${BUILD_NUMBER}
                Build URL: ${BUILD_URL}

                Docker Images Pushed:
                - jenish011/scientific-calculator:${BUILD_NUMBER}
                - jenish011/scientific-calculator:latest

                All tests passed and image pushed successfully.
                """,
                to: "jenishvekariya011@gmail.com"
            )
        }

        failure {
            emailext (
                subject: "FAILED: Build #${BUILD_NUMBER} - ${JOB_NAME}",
                body: """
                BUILD FAILED !!!

                Job Name: ${JOB_NAME}
                Build Number: ${BUILD_NUMBER}
                Check Logs: ${BUILD_URL}

                Please review the error immediately.
                """,
                to: "jenishvekariya011@gmail.com"
            )
        }
    }
}