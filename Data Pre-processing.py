{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# UCI - Dataset - Preprocessing"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Import "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import sklearn"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Fetching and Cleaning"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No of Features: 561\n"
     ]
    }
   ],
   "source": [
    "# get feature names from the file features.txt\n",
    "features = list()\n",
    "with open('UCI HAR Dataset/features.txt') as f:\n",
    "    features = [line.split()[1] for line in f.readlines()]\n",
    "\n",
    "print('No of Features: {}'.format(len(features)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Duplicate features:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "561"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "seen = set()\n",
    "uniq_features = []\n",
    "for idx, x in enumerate(features):\n",
    "    if x not in seen:\n",
    "        uniq_features.append(x)\n",
    "        seen.add(x)\n",
    "    elif x + 'n' not in seen:\n",
    "        uniq_features.append(x + 'n')\n",
    "        seen.add(x + 'n')\n",
    "    else:\n",
    "        uniq_features.append(x + 'nn')\n",
    "        seen.add(x + 'nn')\n",
    "len(uniq_features)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Obtain the train data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>tBodyAcc-mean()-X</th>\n",
       "      <th>tBodyAcc-mean()-Y</th>\n",
       "      <th>tBodyAcc-mean()-Z</th>\n",
       "      <th>tBodyAcc-std()-X</th>\n",
       "      <th>tBodyAcc-std()-Y</th>\n",
       "      <th>tBodyAcc-std()-Z</th>\n",
       "      <th>tBodyAcc-mad()-X</th>\n",
       "      <th>tBodyAcc-mad()-Y</th>\n",
       "      <th>tBodyAcc-mad()-Z</th>\n",
       "      <th>tBodyAcc-max()-X</th>\n",
       "      <th>...</th>\n",
       "      <th>angle(tBodyAccMean,gravity)</th>\n",
       "      <th>angle(tBodyAccJerkMean),gravityMean)</th>\n",
       "      <th>angle(tBodyGyroMean,gravityMean)</th>\n",
       "      <th>angle(tBodyGyroJerkMean,gravityMean)</th>\n",
       "      <th>angle(X,gravityMean)</th>\n",
       "      <th>angle(Y,gravityMean)</th>\n",
       "      <th>angle(Z,gravityMean)</th>\n",
       "      <th>subject</th>\n",
       "      <th>Activity</th>\n",
       "      <th>ActivityName</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>7201</th>\n",
       "      <td>0.297333</td>\n",
       "      <td>-0.025067</td>\n",
       "      <td>-0.111096</td>\n",
       "      <td>-0.988564</td>\n",
       "      <td>-0.971932</td>\n",
       "      <td>-0.972331</td>\n",
       "      <td>-0.990016</td>\n",
       "      <td>-0.970233</td>\n",
       "      <td>-0.972755</td>\n",
       "      <td>-0.920644</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.044727</td>\n",
       "      <td>0.292265</td>\n",
       "      <td>-0.03535</td>\n",
       "      <td>0.021019</td>\n",
       "      <td>-0.208864</td>\n",
       "      <td>-0.24274</td>\n",
       "      <td>-0.388783</td>\n",
       "      <td>30</td>\n",
       "      <td>4</td>\n",
       "      <td>SITTING</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1 rows × 564 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      tBodyAcc-mean()-X  tBodyAcc-mean()-Y  tBodyAcc-mean()-Z  \\\n",
       "7201           0.297333          -0.025067          -0.111096   \n",
       "\n",
       "      tBodyAcc-std()-X  tBodyAcc-std()-Y  tBodyAcc-std()-Z  tBodyAcc-mad()-X  \\\n",
       "7201         -0.988564         -0.971932         -0.972331         -0.990016   \n",
       "\n",
       "      tBodyAcc-mad()-Y  tBodyAcc-mad()-Z  tBodyAcc-max()-X  ...  \\\n",
       "7201         -0.970233         -0.972755         -0.920644  ...   \n",
       "\n",
       "      angle(tBodyAccMean,gravity)  angle(tBodyAccJerkMean),gravityMean)  \\\n",
       "7201                    -0.044727                              0.292265   \n",
       "\n",
       "      angle(tBodyGyroMean,gravityMean)  angle(tBodyGyroJerkMean,gravityMean)  \\\n",
       "7201                          -0.03535                              0.021019   \n",
       "\n",
       "      angle(X,gravityMean)  angle(Y,gravityMean)  angle(Z,gravityMean)  \\\n",
       "7201             -0.208864              -0.24274             -0.388783   \n",
       "\n",
       "      subject  Activity  ActivityName  \n",
       "7201       30         4       SITTING  \n",
       "\n",
       "[1 rows x 564 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# get the data from txt files to pandas dataffame\n",
    "X_train = pd.read_csv('UCI HAR Dataset/train/X_train.txt', delim_whitespace=True, header=None, names=uniq_features)\n",
    "\n",
    "# # add subject column to the dataframe\n",
    "X_train['subject'] = pd.read_csv('UCI HAR Dataset/train/subject_train.txt', header=None, squeeze=True)\n",
    "\n",
    "y_train = pd.read_csv('UCI HAR Dataset/train/y_train.txt', names=['Activity'], squeeze=True)\n",
    "y_train_labels = y_train.map({1: 'WALKING', 2:'WALKING_UPSTAIRS',3:'WALKING_DOWNSTAIRS',\\\n",
    "                       4:'SITTING', 5:'STANDING',6:'LAYING'})\n",
    "\n",
    "# # put all columns in a single dataframe\n",
    "train = X_train\n",
    "train['Activity'] = y_train\n",
    "train['ActivityName'] = y_train_labels\n",
    "train.sample()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7352, 564)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Obtain the test data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>tBodyAcc-mean()-X</th>\n",
       "      <th>tBodyAcc-mean()-Y</th>\n",
       "      <th>tBodyAcc-mean()-Z</th>\n",
       "      <th>tBodyAcc-std()-X</th>\n",
       "      <th>tBodyAcc-std()-Y</th>\n",
       "      <th>tBodyAcc-std()-Z</th>\n",
       "      <th>tBodyAcc-mad()-X</th>\n",
       "      <th>tBodyAcc-mad()-Y</th>\n",
       "      <th>tBodyAcc-mad()-Z</th>\n",
       "      <th>tBodyAcc-max()-X</th>\n",
       "      <th>...</th>\n",
       "      <th>angle(tBodyAccMean,gravity)</th>\n",
       "      <th>angle(tBodyAccJerkMean),gravityMean)</th>\n",
       "      <th>angle(tBodyGyroMean,gravityMean)</th>\n",
       "      <th>angle(tBodyGyroJerkMean,gravityMean)</th>\n",
       "      <th>angle(X,gravityMean)</th>\n",
       "      <th>angle(Y,gravityMean)</th>\n",
       "      <th>angle(Z,gravityMean)</th>\n",
       "      <th>subject</th>\n",
       "      <th>Activity</th>\n",
       "      <th>ActivityName</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>200</th>\n",
       "      <td>0.282062</td>\n",
       "      <td>-0.013705</td>\n",
       "      <td>-0.117537</td>\n",
       "      <td>-0.995089</td>\n",
       "      <td>-0.978343</td>\n",
       "      <td>-0.984182</td>\n",
       "      <td>-0.99586</td>\n",
       "      <td>-0.979005</td>\n",
       "      <td>-0.983087</td>\n",
       "      <td>-0.935646</td>\n",
       "      <td>...</td>\n",
       "      <td>0.016342</td>\n",
       "      <td>-0.085813</td>\n",
       "      <td>-0.338115</td>\n",
       "      <td>0.263447</td>\n",
       "      <td>-0.72632</td>\n",
       "      <td>0.175653</td>\n",
       "      <td>-0.16192</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>SITTING</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1 rows × 564 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     tBodyAcc-mean()-X  tBodyAcc-mean()-Y  tBodyAcc-mean()-Z  \\\n",
       "200           0.282062          -0.013705          -0.117537   \n",
       "\n",
       "     tBodyAcc-std()-X  tBodyAcc-std()-Y  tBodyAcc-std()-Z  tBodyAcc-mad()-X  \\\n",
       "200         -0.995089         -0.978343         -0.984182          -0.99586   \n",
       "\n",
       "     tBodyAcc-mad()-Y  tBodyAcc-mad()-Z  tBodyAcc-max()-X  ...  \\\n",
       "200         -0.979005         -0.983087         -0.935646  ...   \n",
       "\n",
       "     angle(tBodyAccMean,gravity)  angle(tBodyAccJerkMean),gravityMean)  \\\n",
       "200                     0.016342                             -0.085813   \n",
       "\n",
       "     angle(tBodyGyroMean,gravityMean)  angle(tBodyGyroJerkMean,gravityMean)  \\\n",
       "200                         -0.338115                              0.263447   \n",
       "\n",
       "     angle(X,gravityMean)  angle(Y,gravityMean)  angle(Z,gravityMean)  \\\n",
       "200              -0.72632              0.175653              -0.16192   \n",
       "\n",
       "     subject  Activity  ActivityName  \n",
       "200        2         4       SITTING  \n",
       "\n",
       "[1 rows x 564 columns]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# get the data from txt files to pandas dataffame\n",
    "X_test = pd.read_csv('UCI HAR Dataset/test/X_test.txt', delim_whitespace=True, header=None, names=uniq_features)\n",
    "\n",
    "# add subject column to the dataframe\n",
    "X_test['subject'] = pd.read_csv('UCI HAR Dataset/test/subject_test.txt', header=None, squeeze=True)\n",
    "\n",
    "# get y labels from the txt file\n",
    "y_test = pd.read_csv('UCI HAR Dataset/test/y_test.txt', names=['Activity'], squeeze=True)\n",
    "y_test_labels = y_test.map({1: 'WALKING', 2:'WALKING_UPSTAIRS',3:'WALKING_DOWNSTAIRS',\\\n",
    "                       4:'SITTING', 5:'STANDING',6:'LAYING'})\n",
    "\n",
    "\n",
    "# put all columns in a single dataframe\n",
    "test = X_test\n",
    "test['Activity'] = y_test\n",
    "test['ActivityName'] = y_test_labels\n",
    "test.sample()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2947, 564)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Check for Duplicates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No of duplicates in train: 0\n",
      "No of duplicates in test : 0\n"
     ]
    }
   ],
   "source": [
    "print('No of duplicates in train: {}'.format(sum(train.duplicated())))\n",
    "print('No of duplicates in test : {}'.format(sum(test.duplicated())))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. Checking for NaN/null values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We have 0 NaN/Null values in train\n",
      "We have 0 NaN/Null values in test\n"
     ]
    }
   ],
   "source": [
    "print('We have {} NaN/Null values in train'.format(train.isnull().values.sum()))\n",
    "print('We have {} NaN/Null values in test'.format(test.isnull().values.sum()))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. Check for data imbalance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.set_style('whitegrid')\n",
    "plt.rcParams['font.family'] = 'Dejavu Sans'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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iQkrERFVW1xzRURE1Q33WagYrmElIqJqi2uuiIiouuE+CxXDEVYiIiIiIiJSSUxYiYiIiIiISCUxYSUiIiJ6z0gLi5XGZYVcQ0dEqoVrWImIiIjeMzpaGrCfHKYQT1zgz3XhRKRSOMJKREREREREKokJKxEREREREakkJqxERERERESkkpiwEhERERERkUpiwkpEREREREQqiQkrERERERERqSQmrERERERERKSSmLASERERERGRSmLCSkRERERERCqJCSsRERERERGpJCasREREREREpJKYsBIRERFRtSIUSd9a3UUFBRWKEwGAtLC4QvHqTCZV/v1XWlzZ905Fvp80y12SiIiIiEgFqGnq4ObMjgrx5tNT37huTW1tzP5osEJ82sZtb1w31Vw6WhqwnxymEE9c4F8FvXm71HV0cLh7D4V4jyOHlZZX9j1Vke8njrASERERcHMxqQAAIABJREFUERGRSmLCSkRERERERCqJCSsRERERERGpJCasRERE78Db3CSGiIiopuKmS0RERO/A29wkhoiIqKbiCCsRERERERGpJCasREREREREpJKYsBIRERFVEmlhcbliRERUPlzDSkRERFRJdLQ0YD85TC6WuMC/inpDRFT9cYSViIiIiIiIVBITViIiIiIiIlJJTFhViLSUd/SVFiciIiLVx3fwEpGqq4x/p4re0np9rmFVITqaOv+vvfsPrqq+88f/CglEPiJSqCEjS39ItWVQqfPdLkWtrFiRriKI0taplmp3nN2tsoqVEanatUWE4tZVp7as211bf1REhPFHrRoUqOKvqquMoGuVCq6ELgIiYELC+f7hFMXci1Fzc96HPB5/JSfh3mcO97xznznn/T5xxDVHtNn+8DkP55AGAOgI7sELpK4jxqma7tVx7fl3ttl+9pVjPlY2Z1gBAABIksIKAABAkhRWAAAAklTRwvrmm2/GpEmTYvTo0fG1r30tnn766di4cWOcccYZMWrUqDjjjDNi06ZNlYyQOzcQB+DD2tFUevGLctsBYE9V0UWXpk+fHl/5ylfi6quvjubm5nj77bfj5z//eQwfPjzOOuusmDNnTsyZMycuuOCCSsbIlRuIA/BhdautjcVHjWizfcSSxTmkAYD8VOwM6+bNm+OJJ56IU045JSIievToEb17946GhoYYN25cRESMGzcuHnjggUpFAAAAoMAqdoZ1zZo10bdv35g6dWqsXLkyhgwZEtOmTYv169dHXV1dRETst99+sX79+kpFAAAAoMAqVlhbWlri+eefj4svvjiGDh0aP/7xj2POnDm7fE9VVVVUVVV94GM1NTXFihUrOjTf4MGDy36tI5+r3POUeo7OygRU3qc+c0Ds3bN2l21btjXFq6tezilRx/gwY1pnPfeHVemsHZWznM74HfVhFWWfep2+qyg5Iyp7THXk+7GuuE+9Tt9VLmvW0hRVNbUlv1ZKXu/5K/27q5T2/qwVK6z19fVRX18fQ4cOjYiI0aNHx5w5c6Jfv36xbt26qKuri3Xr1kXfvn0/8LFqa2s7dSd2xnN92OfI40UEfDyl5q/vqcdykX6uImUtJcX8KWYqpSg5I4qTtSg5y0nx/ViR9mlRsuaZs6qmNl697JBdtn3qkufKfn9R9mlHeP/PWq7AVmwO63777Rf19fXx8svvnE1YtmxZDBo0KEaOHBkLFiyIiIgFCxbEMcccU6kIAAAAFFhFVwm++OKL4/vf/35s3749Bg4cGDNmzIgdO3bEueeeG/PmzYv9998/rrrqqkpGAAAAoKAqWlgHDx4c8+fPb7P9hhtuqOTTAgAAsAeo2CXB5KOluflDbYeuZkdT04fanqdSmTorZ9aS3v4A0lKk8bQo7FMqrWl7a94RPrSKnmGl89X06BHTTzulzfZpN87LIQ2kp1ttbSw+akSb7SOWLM4hze6VytpZOUstEhGx+4UigK6lSONpUdinVFpt9+o2i0JGvLMwZKqcYQUAACBJCisAAABJUlgLIM95bAAAe6KWAs7lg67IHNYCyHMeGwDAnqime3Vce/6dbbaffeWYHNIA5TjDCgAAQJIUVgAAAJKksFI4pe4fVe6eUk1l7iXZWpB5we7H9tGV+78HAD4+a6zQWcxhpXBK3T+q3L2jamtq44hrjmiz/eFzHi7EvGD3Y/vodvd/DwB8PNZYobM4wwoAAECSFFYAAACSpLACAACQJIWViNjNokUf4qbaFggCAAA6kkWXiIjSCxlFlF/MqBQLBAEAAB3JGVYAAACSpLACAACQJIWVPULWYp4sANC1tDQ3t2sbFJk5rOwRqmpq49XLDmmz/VOXPJdDGgCAyqvp0SOmn3bKLtum3TgvpzRQGc6wAgAAkCSFFQAAgCQprEDJ++2WvTdvmfnC5bYXXUfODyo317oj5mCXy9QZc5ncgxl4r5Yyvz/KbYdK8juq+MxhBUreh7fcPXhra2rjiGuOaLP94XMerki2vHXk/KBKzrUulTOic+YyuQcz8F413avj2vPvbLP97CvH5JCGrs7vqOJzhhUAAIAkKawAAAAkSWEFAAAgSYUsrGUXg6nQZP48FzOhuDr7ddqVdcSiRV2V1yMApMECUaUVctGlUgvERJRfJObjynMxE4qrs1+nXVmpxYw6YiGjrsDrFADSYIGo0tp1hnXixInt2gYAAAAdZbdnWJuammLbtm2xYcOG2LRpU2RZFhERb731VjQ2NnZKQAAAALqm3RbW3/zmN3HDDTfEunXrYvz48TsLa69eveK0007rlIB7oqylKapqavOO8ZE1tTRFbYHzp8g+BYpqR1NTdKut/cBteSuXKcWsALxrt4V14sSJMXHixPj1r38dp59+emdl2uOVmm8XUZw5d7U1tXHENUe02f7wOQ/nkGbPYJ8CRVVqzlWK863MDQMopnYtunT66afHU089Fa+99lq0tr67ouS4ceMqFgwAAICurV2F9YILLojVq1fHF77whaiuro6IiKqqKoUVAACAimlXYV2+fHncc889UVVVVek8kJyW5uao6dGj3dvzUpSctGUOc+f5MPMtHVPQsUodO46nrqFI46nXaXraVVgPPPDA+POf/xx1dXWVzgPJKcp9eIuSk7bMYe48H2a+pWMKOlapY8rx1DUUaTz1Ok1Puwrrhg0b4vjjj49DDz00unfvvnP7z3/+84oFAwAAoGtrV2E955xzKp0DAAAAdtGuwvo3f/M3lc4BAAAAu2hXYT3ssMN2Lri0ffv2aGlpiZ49e8ZTTz1V0XAdwWImAAAUWcv21qjpXp13DMhFuwrr008/vfPjLMuioaEhnnnmmYqF6kgWMwEAoMhqulfHteff2Wb72VeOySENdK5uH/YfVFVVxVe/+tX4/e9/X4k8AAAAEBHtPMN633337fx4x44dsXz58qgtcc86AAAA6CjtKqwPPvjgzo+rq6tjwIAB8bOf/axiofJUlDkCRckJAAB0rJbm5qjp0aPd24usXYV1xowZlc6RjFJzBFKcH2AuAwAAdE01PXrE9NNOabN92o3zckhTWe2aw7p27dr43ve+F8OHD4/hw4fHOeecE2vXrq10NgAAALqwdhXWqVOnxsiRI2Pp0qWxdOnSOProo2Pq1KmVzgYAAEAX1q7C+sYbb8TJJ58cNTU1UVNTE+PHj4833nij0tkAAADowtpVWPv06RMLFy6M1tbWaG1tjYULF0afPn0qnQ06Vcv21k55nqylqVOep7PtaGr7c5XaBi3Nze3aRvvZpwB7rs56j5qqdi26dPnll8ePfvSjmDFjRlRVVcVhhx0WV1xxRaWzQafqrIWsqmpq49XLDtll26cuea5DnyMP3WprY/FRI3bZNmLJ4pzSkLJSC0XsiYtEdCb7FGDPVZRFYSulXYX16quvjpkzZ8a+++4bEREbN26MmTNndqnVgwEAAOhc7bok+IUXXthZViPeuUR4xYoVFQsFAAAA7SqsO3bsiE2bNu38fOPGjdHamt611Hvq3MCiK3Xd/fYyc6vMuWqfrjqXoamL/txUVlc9ntg984IB0tCuS4LPPPPM+MY3vhGjR4+OiIh77703/uEf/qGiwT6KPXVuYNGVu+6+q9zsuBK66lyG2u7V8f9d8Ks22//wk2/nkIY9RWfNX6dYzAsGSEO7Cuu4cePi4IMPjkcffTQiIq699tr43Oc+V9FgAAAAdG3tKqwREZ/73OeUVAAAADpNu+awAl1PV5sTbh4jReB12jW4rzVUnvG0ONp9hhXoWkrNCY/Yc+eFm8dIEXiddg3uaw2VZzwtDmdYAQAASJLCCgAAQJIUVgAAAJKksAIUiEUioGM5pgDSZtElgAKxSAR0LMcUQNqcYQUAACBJCisAAABJUljZrazFjcoBAPhg5oRTCeawsltVNbXx6mWH7LLtU5c8l1MaAABSZU44leAMKwAAAElSWAEAAEiSwgoAAECSFFYAAACSpLACAACQJIUVAACAJCmsAAAAJElhBaAi3EAeKq+luflDbQcompq8AwCwZ3IDeai8mh49Yvppp7TZPu3GeTmkAeh4zrACAACQJIUVAACAJCmsQKcz5woAgPao+BzW1tbWOPnkk6N///7xi1/8IlavXh2TJ0+OjRs3xpAhQ2LWrFnRo0ePSscAEmLOFQAA7VHxM6y/+tWvYtCgQTs/nz17dnznO9+J+++/P3r37h3z5nmDCgAAQFsVLaxr166Nhx56KE455Z0zKVmWxaOPPhrHHXdcREScdNJJ0dDQUMkIAAAAFFRFLwm+/PLL44ILLogtW7ZERMSGDRuid+/eUVPzztPW19dHY2PjBz5OU1NTrFixYufngwcPrkzgj+C9uUopStai5IwoTtai5IyobNZSz72757NPO5592vHs04/23J/9zKdjr57/r832t7dtjVdW/ansY9mn5Z/beNq57NOOZ592vD1ln/5FxQrrgw8+GH379o2DDz44HnvssY/1WLW1tUnt3PdKNVcpRclalJwRxcmaZ84P+9z2accrStai5IwoTtYUj/1y89ft045/bvu04xUla1FyRhQna1FyRhQn6/tzliuwFSusTz31VCxatCiWLFkSTU1N8dZbb8X06dPjzTffjJaWlqipqYm1a9dG//79KxUBAACAAqvYHNbzzz8/lixZEosWLYp//dd/jS9/+ctx5ZVXxrBhw+J3v/tdRETccccdMXLkyEpFAAAAoMA6/T6sF1xwQfznf/5nHHvssbFx48aYMGFCZ0cAAACgACp+H9aIiGHDhsWwYcMiImLgwIFuZQMAe7CW7a1R07067xgA7AE6pbACAF1HTffquPb8O9tsP/vKMTmkAaDIOv2SYAAAAGgPhRUAAIAkKaxAxbRsb807AgAABWYOK1Ax5rEBAPBxOMMKAABAkhRWAAAAkqSwAgAAkCSFFQAAgCQprAAAACRJYQUAACBJCisAAABJUlgBABLXsr017wgAuajJOwAAALtX0706rj3/zjbbz75yTA5pADqPM6wAAAAkSWEFAAAgSQorAAAASVJYAQAASJLCCgAAQJIUVgAAAJKksAIAAJAkhRUAAIAkKawAAAAkSWEFAAAgSQorAAAASVJYAQAASJLCCgAAQJIUVgAAAJKksAIAAJAkhRUAAIAkKawAAAAkSWEFAAAgSQorAAAASVJYAQAASJLCCgAAQJIUVgAAAJKksAIAAJAkhRUAAIAkKawAAAAkSWEFAAAgSQorAAAASVJYAQAASJLCCgAAQJIUVgAAAJKksAIAAJAkhRUAAIAkKawAAAAkSWEFAAAgSQorAAAASVJYAQAASJLCCgAAQJIUVgAAAJKksAIAAJAkhRUAAIAkKawAAAAkSWEFAAAgSQorAAAASVJYAQAASJLCCgAAQJIUVgAAAJKksAIAAJAkhRUAAIAkKawAAAAkSWEFAAAgSQorAAAASVJYAQAASJLCCgAAQJIUVgAAAJKksAIAAJAkhRUAAIAkKawAAAAkSWEFAAAgSQorAAAASVJYAQAASJLCCgAAQJIUVgAAAJKksAIAAJAkhRUAAIAk1VTqgV9//fWYMmVKrF+/PqqqquLrX/96TJw4MTZu3BjnnXdevPbaazFgwIC46qqrYt99961UDAAAAAqqYmdYq6ur48ILL4x77rknbr311rj55pvjpZdeijlz5sTw4cPjvvvui+HDh8ecOXMqFQEAAIACq1hhrauriyFDhkRERK9eveKAAw6IxsbGaGhoiHHjxkVExLhx4+KBBx6oVAQAAAAKrFPmsK5ZsyZWrFgRQ4cOjfXr10ddXV1EROy3336xfv36zogAAABAwVRsDutfbNmyJSZNmhQXXXRR9OrVa5evVVVVRVVV1Qc+RlNTU6xYsWLn54MHD+7wnB/Ve3OVUpSsRckZUZysRckZUZysRckZUZysRckZUZysRckZUZysRckZUZysRckZUZysRckZUZysRckZUZysRcn5XhUtrNu3b49JkybFmDFjYtSoURER0a9fv1i3bl3U1dXFunXrom/fvh/4OLW1tUnt3PdKNVcpRclalJwRxclalJwRxclalJwRxclalJwRxclalJwRxclalJwRxclalJwRxclalJwRxclalJwRxcn6/pzlCmzFLgnOsiymTZsWBxxwQJxxxhk7t48cOTIWLFgQERELFiyIY445plIRAAAAKLCKnWH9wx/+EAsXLoyDDjooxo4dGxERkydPjrPOOivOPffcmDdvXuy///5x1VVXVSoCAAAABVaxwvrXf/3X8cILL5T82g033FCppwUAAGAP0SmrBAMAAMCHpbACAACQJIUVAACAJCmsAAAAJElhBQAAIEkKKwAAAElSWAEAAEiSwgoAAECSFFYAAACSpLACAACQJIUVAACAJCmsAAAAJElhBQAAIEkKKwAAAElSWAEAAEiSwgoAAECSFFYAAACSpLACAACQJIUVAACAJCmsAAAAJElhBQAAIEkKKwAAAElSWAEAAEiSwgoAAECSFFYAAACSpLACAACQJIUVAACAJCmsAAAAJElhBQAAIEkKKwAAAElSWAEAAEiSwgoAAECSFFYAAACSpLACAACQJIUVAACAJCmsAAAAJElhBQAAIEkKKwAAAElSWAEAAEiSwgoAAECSFFYAAACSpLACAACQJIUVAACAJCmsAAAAJElhBQAAIEkKKwAAAElSWAEAAEiSwgoAAECSFFYAAACSpLACAACQJIUVAACAJCmsAAAAJElhBQAAIEkKKwAAAElSWAEAAEiSwgoAAECSFFYAAACSpLACAACQJIUVAACAJCmsAAAAJElhBQAAIEkKKwAAAElSWAEAAEiSwgoAAECSFFYAAACSpLACAACQJIUVAACAJCmsAAAAJElhBQAAIEkKKwAAAElSWAEAAEiSwgoAAECSFFYAAACSpLACAACQJIUVAACAJCmsAAAAJElhBQAAIEkKKwAAAEnKpbAuWbIkjjvuuDj22GNjzpw5eUQAAAAgcZ1eWFtbW+Oyyy6L66+/Pu6+++6466674qWXXursGAAAACSu0wvrs88+G5/+9Kdj4MCB0aNHjzj++OOjoaGhs2MAAACQuE4vrI2NjVFfX7/z8/79+0djY2NnxwAAACBxVVmWZZ35hPfee28sXbo0pk+fHhERCxYsiGeffTYuueSSsv/mmWeeidra2s6KCAAAQCdqamqKL37xi22213R2kP79+8fatWt3ft7Y2Bj9+/ff7b8pFRwAAIA9W6dfEnzIIYfEqlWrYvXq1dHc3Bx33313jBw5srNjAAAAkLhOP8NaU1MTl1xySfz93/99tLa2xsknnxwHHnhgZ8cAAAAgcZ0+hxUAAADao9MvCQYAAID2UFgBAABIUqfPYc3b1KlT46GHHop+/frFXXfdlXecspqamuJb3/pWNDc3R2traxx33HExadKkvGOVNXLkyNh7772jW7duUV1dHfPnz887Uklvvvlm/OAHP4gXX3wxqqqq4vLLL4/DDjss71htvPzyy3Heeeft/Hz16tUxadKk+M53vpNfqDL+67/+K2677baoqqqKgw46KGbMmJHMbahKHe+//e1v49prr40//vGPcdttt8UhhxySc8rdj0u//OUvY+bMmbFs2bLo27dvTgnfVSrrNddcE3Pnzt2Zb/LkyTFixIg8Y5bdp7/+9a/jpptuiurq6hgxYkRMmTIlx5TvKJX13HPPjVdeeSUiIjZv3hz77LNPLFy4MM+YJXOuXLkyLr300ti6dWsMGDAgZs+eHb169co1Z0TE66+/HlOmTIn169dHVVVVfP3rX4+JEycmd/yXyzlz5sx48MEHo3v37vGpT30qZsyYEb17904y61VXXRUNDQ3RrVu36NevX8yYMeMD7/6QR84Ux6lyWSPSGqvK5UxxnCqXdcWKFXHppZdGU1NTVFdXxw9/+MM49NBDk8uZ4pharpOsXr06Jk+eHBs3bowhQ4bErFmzokePHpUJkXUxjz/+eLZ8+fLs+OOPzzvKbu3YsSN76623sizLsubm5uyUU07Jnn766ZxTlXf00Udn69evzzvGB5oyZUo2d+7cLMuyrKmpKdu0aVPOiT5YS0tLdvjhh2dr1qzJO0oba9euzY4++uhs27ZtWZZl2aRJk7Lbb78951TvKnW8v/TSS9kf//jH7LTTTsueffbZHNO9q9y49L//+7/ZmWeemf3t3/5tMsdXqaxXX311dv311+eYqq1SOZctW5ZNnDgxa2pqyrIsy/7v//4vr3i7+KDfSzNmzMiuueaaTk7VVqmc48ePzx577LEsy7Lstttuy37605/mFW8XjY2N2fLly7Msy7LNmzdno0aNyv7nf/4nueO/XM6lS5dm27dvz7Isy2bNmpXNmjUrz5hZlpXPunnz5p3fc8MNN2QXX3xxXhGzLCufM8VxqlzW1MaqcjnfK5VxqlzWM844I3vooYeyLMuyhx56KDvttNPyjFk2Z4pjarlOMmnSpOyuu+7KsizLLr744uymm26qWIYud0nwl770pdh3333zjvGBqqqqYu+9946IiJaWlmhpaYmqqqqcUxXb5s2b44knnohTTjklIiJ69OiR+1+s22PZsmUxcODAGDBgQN5RSmptbY233347Wlpa4u233466urq8I+1U6ngfNGhQHHDAATklKq3cuDRjxoy44IILkjr2izKGlsp5yy23xFlnnbXzL8D9+vXLI1obu9unWZbFb3/72zjhhBM6OVVbpXKuWrUqvvSlL0VExBFHHBH33XdfHtHaqKuriyFDhkRERK9eveKAAw6IxsbG5I7/cjmPPPLIqKl55yK4L37xi7vcvz4v5bK+9+zPtm3bch+vyuVMUbmsqY1VH7RPUxqnymWtqqqKLVu2RMQ77wfzfq9SLmeKY2q5TvLoo4/GcccdFxERJ510UjQ0NFQsQ5crrEXS2toaY8eOjcMPPzwOP/zwGDp0aN6Rduu73/1ujB8/Pm699da8o5S0Zs2a6Nu3b0ydOjXGjRsX06ZNi61bt+Yd6wPdfffdSfwSKKV///5x5plnxtFHHx1HHnlk9OrVK4488si8Y+0RHnjggairq4svfOELeUdpl5tuuinGjBkTU6dOjU2bNuUdp6RVq1bFk08+GRMmTIjTTjstnn322bwjfaAnn3wy+vXrF5/5zGfyjlLSgQceuPNNyr333huvv/56zonaWrNmTaxYsSL536Hlct5+++1x1FFH5ZSqtPdn/elPfxojRoyIO++8M/75n/8553Tven/OlMep92ZNeawq9TpNdZx6b9aLLrooZs2aFSNGjIiZM2fG5MmT846303tzpjqmvr+TDBw4MHr37r3zD2v19fUV/cOQwpqw6urqWLhwYSxevDieffbZePHFF/OOVNYtt9wSd9xxR/z7v/973HTTTfHEE0/kHamNlpaWeP755+PUU0+NBQsWRM+ePWPOnDl5x9qt5ubmWLRoUYwePTrvKCVt2rQpGhoaoqGhIZYuXRrbtm3Lff7KnmDbtm3xi1/8Iqk3frtz6qmnxv333x8LFy6Murq6uOKKK/KOVFJra2ts2rQp5s6dG1OmTIlzzz03ssTv7HbXXXcl+weriIjp06fHzTffHOPHj48tW7ZUbv7SR7Rly5aYNGlSXHTRRbnPA9udcjmvu+66qK6ujhNPPDHHdLsqlfW8886LxYsXx5gxY+LGG2/MOeE73p8z5XHq/VlTHavKvU5THKfen/WWW26JqVOnxuLFi2Pq1Kkxbdq0vCNGRNucqY6p7+8kL7/8cqc+v8JaAL17945hw4bF0qVL845S1l8WWOjXr18ce+yxSf018C/q6+ujvr5+518FR48eHc8//3zOqXZvyZIlMWTIkPjkJz+Zd5SSHnnkkfirv/qr6Nu3b3Tv3j1GjRoVTz/9dN6xCu/VV1+NNWvWxNixY2PkyJGxdu3aGD9+fPz5z3/OO1pJn/zkJ6O6ujq6desWEyZMiOeeey7vSCX1798/jj322KiqqopDDz00unXrFhs2bMg7VlktLS1x//33x9/93d/lHaWsQYMGxS9/+cuYP39+HH/88TFw4MC8I+20ffv2mDRpUowZMyZGjRqVd5yyyuWcP39+PPTQQzF79uzcL7P9iw/ap2PGjEniEsZSOVMdp0plTXGsKvd/n+I4VSrrHXfcsfPjr33ta0m8Ty2VM+UxNeLdTvLMM8/Em2++GS0tLRERsXbt2ooutqawJuqNN96IN998MyIi3n777XjkkUeSmnfzXlu3bo233npr58cPP/xwHHjggTmnamu//faL+vr6nX8VWrZsWQwaNCjnVLt39913x/HHH593jLL233//+O///u/Ytm1bZFlWiH1aBJ///Odj2bJlsWjRoli0aFHU19fH/PnzY7/99ss7Wknr1q3b+fEDDzyQ5PEfEfHVr341HnvssYiIeOWVV2L79u3xiU98IudU5f1l3K+vr887Slnr16+PiIgdO3bEddddF9/85jdzTvSOLMti2rRpccABB8QZZ5yRd5yyyuVcsmRJXH/99XHddddFz549c0z4rnJZV61atfPjhoaG3N+rlMuZ4jhVLmtqY9XujqfUxqlyWevq6uLxxx+PiIhHH30098uXy+VMcUwt1UkGDRoUw4YNi9/97ncR8c4fBEaOHFmxDFVZCtcYdKLJkyfH448/Hhs2bIh+/frFOeecExMmTMg7VhsrV66MCy+8MFpbWyPLshg9enScffbZeccqafXq1fG9730vIt655O6EE06If/zHf8w5VWkrVqyIadOmxfbt22PgwIExY8aMZBeQ2bp1axx99NHxwAMPxD777JN3nLKuvvrquOeee6KmpiYGDx4c06dPT+YSllLHe58+feJHP/pRvPHGG9G7d+8YPHhw/Md//EdyOd87Lo0cOTLmzZuXxG1tSmV9/PHHY+XKlRERMWAkKT+AAAAEe0lEQVTAgLjssstyX9CiVM6xY8fGRRddFCtXrozu3bvHlClTYvjw4bnmLJd1woQJceGFF8bQoUPj1FNPzTtiRJTOuXXr1rj55psjIuLYY4+N888/P4mzgU8++WR861vfioMOOii6dXvnb/OTJ0+O5ubmpI7/cjl//OMfR3Nzc/Tp0yciIoYOHRqXXXZZbjkjymedN29evPLKK1FVVRUDBgyIf/mXf8n1tjblct51113JjVPlsg4fPjypsapczhEjRiQ3TpXLuvfee8fll18eLS0tUVtbG5deemkcfPDByeVctWpVcmNquU6yevXqOO+882LTpk0xePDgmD17dsXe/3W5wgoAAEAxuCQYAACAJCmsAAAAJElhBQAAIEkKKwAAAElSWAEAAEiSwgoAObnmmmtK3lalsbExJk2a9JEec/78+dHY2PhxowFAEhRWAEhM//794+qrr/5I//aOO+6IdevWdXAiAMiHwgoAHWjr1q1x1llnxYknnhgnnHBC3HPPPTFy5Mh44403IiLiueeei9NPP33n969cuTK+8Y1vxKhRo2Lu3LkREbFmzZo44YQTIiKitbU1Zs6cGSeffHKMGTMmfvOb3+z8t3PmzIkxY8bEiSeeGLNnz4577703li9fHt///vdj7Nix8fbbb3fiTw4AHa8m7wAAsCdZunRp1NXVxZw5cyIiYvPmzTF79uyy3//CCy/E3LlzY+vWrXHSSSfFiBEjdvn6vHnzYp999onbb789mpub45vf/GYcccQR8fLLL8eiRYti7ty50bNnz9i4cWP06dMnbrrpppgyZUoccsghFf05AaAzOMMKAB3ooIMOikceeSR+8pOfxJNPPhn77LPPbr//mGOOib322iv69u0bw4YNi+eee26Xrz/88MOxcOHCGDt2bEyYMCE2btwYf/rTn2LZsmUxfvz46NmzZ0RE9OnTp2I/EwDkxRlWAOhAn/3sZ2P+/PmxePHiuOqqq+LLX/5yVFdXR5ZlERHR1NS0y/dXVVXt9vGyLIsf/OAH8ZWvfGWX7b///e87NjgAJMgZVgDoQI2NjdGzZ88YO3ZsfPe7343nn38+BgwYEMuXL4+IiPvuu2+X729oaIimpqbYsGFDPP74420u5T3yyCPjlltuie3bt0dExCuvvBJbt26Nww8/PObPnx/btm2LiIiNGzdGRMTee+8dW7ZsqfSPCQCdwhlWAOhAL774YsyaNSu6desWNTU18cMf/jCamppi2rRp8W//9m8xbNiwXb7/85//fHz729+ODRs2xD/90z9F//79Y82aNTvPvE6YMCFee+21GD9+fGRZFp/4xCfiZz/7WRx11FGxcuXKOPnkk6N79+4xYsSImDx5cpx00klx6aWXxl577RW33npr7LXXXnnsBgDoEFXZX65RAgCSsHz58rjiiivixhtvzDsKAOTKJcEAkJDnnnsuzj///Pj2t7+ddxQAyJ0zrAAAACTJGVYAAACSpLACAACQJIUVAACAJCmsAAAAJElhBQAAIEkKKwAAAEn6/wFBX3U7dLvtDwAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1152x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16,8))\n",
    "plt.title('Data provided by each user', fontsize=20)\n",
    "sns.countplot(x='subject',hue='ActivityName', data = train)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### $~~~~~~~~~~~~~~~~~~~~~~~~~~$ We have got almost same number of reading from all the subjects\n",
    "$~~~~~~~~~~~$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.title('No of Datapoints per Activity', fontsize=15)\n",
    "sns.countplot(train.ActivityName)\n",
    "plt.xticks(rotation=90)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### $~~~~~~~~~~~~~~~~~~~~~~~~~$Our data is well balanced (almost)\n",
    "$~~~~~~~~~~~$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4. Changing feature names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['tBodyAccmeanX', 'tBodyAccmeanY', 'tBodyAccmeanZ', 'tBodyAccstdX',\n",
       "       'tBodyAccstdY', 'tBodyAccstdZ', 'tBodyAccmadX', 'tBodyAccmadY',\n",
       "       'tBodyAccmadZ', 'tBodyAccmaxX',\n",
       "       ...\n",
       "       'angletBodyAccMeangravity', 'angletBodyAccJerkMeangravityMean',\n",
       "       'angletBodyGyroMeangravityMean', 'angletBodyGyroJerkMeangravityMean',\n",
       "       'angleXgravityMean', 'angleYgravityMean', 'angleZgravityMean',\n",
       "       'subject', 'Activity', 'ActivityName'],\n",
       "      dtype='object', length=564)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "columns = train.columns\n",
    "\n",
    "# Removing '()' from column names\n",
    "columns = columns.str.replace('[()]','')\n",
    "columns = columns.str.replace('[-]', '')\n",
    "columns = columns.str.replace('[,]','')\n",
    "\n",
    "train.columns = columns\n",
    "test.columns = columns\n",
    "\n",
    "test.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5. Save this dataframe in a csv files"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "train.to_csv('data/train.csv', index=False)\n",
    "test.to_csv('data/test.csv', index=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
