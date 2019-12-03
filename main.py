#this is a sample object which will be returned by the LDA library.  This will be deleted.
sampleLDAObject = [([(0.016457407, 'blinddata'),
   (0.013355694, 'challenge'),
   (0.01012295, 'company'),
   (0.009961982, 'role'),
   (0.009931401, 'help'),
   (0.009904657, 'location'),
   (0.009899793, 'talent'),
   (0.009886243, 'test'),
   (0.009852432, 'engineer'),
   (0.007913896, 'software')],
  -0.46815505190093104),
 ([(0.01682621, 'cornell'),
   (0.01441851, 'university'),
   (0.011264864, 'application'),
   (0.009779172, 'arxiv'),
   (0.008449792, 'cornell_university'),
   (0.007058739, 'position'),
   (0.0070001795, 'team'),
   (0.0057919268, 'online'),
   (0.005688391, 'backend'),
   (0.0056264284, 'applicant')],
  -0.5274462715617378),
 ([(0.012407964, 'development'),
   (0.012156849, 'you'),
   (0.011766175, 'application'),
   (0.011180819, 'software'),
   (0.010896422, 'design'),
   (0.010592988, 'team'),
   (0.009780526, 'web'),
   (0.00955148, 'product'),
   (0.009547641, 'strong'),
   (0.009385446, 'technology')],
  -0.5760017043470895),
 ([(0.020723922, 'data'),
   (0.015039341, 'team'),
   (0.011454791, 'we'),
   (0.010297295, 'software'),
   (0.010018243, 'business'),
   (0.0098209325, 'development'),
   (0.009566773, 'review'),
   (0.009513931, 'technology'),
   (0.008589802, 'skill'),
   (0.0071811522, 'client')],
  -0.600801966360079),
 ([(0.022867246, 'job'),
   (0.017583847, 'preferred'),
   (0.017122434, 'time'),
   (0.017031534, 'java'),
   (0.01682841, 'contract'),
   (0.0162554, 'location'),
   (0.015922008, 'required'),
   (0.015180564, 'skill'),
   (0.012153905, 'type'),
   (0.012007199, 'full')],
  -0.7241788992287569),
 ([(0.019700693, 'data'),
   (0.0179627, 'development'),
   (0.014946458, 'design'),
   (0.014530582, 'business'),
   (0.01406248, 'dashboard'),
   (0.010323161, 'required'),
   (0.010086188, 'candidate'),
   (0.009979595, 'user'),
   (0.009936221, 'plus'),
   (0.0097470675, 'skill')],
  -0.8352557697999314),
 ([(0.023212798, 'contract'),
   (0.021415073, 'required'),
   (0.021376101, 'framework'),
   (0.021189125, 'year_required'),
   (0.018495489, 'month'),
   (0.014944796, 'hour'),
   (0.014882797, 'oriented'),
   (0.014774962, 'location'),
   (0.014730365, 'this'),
   (0.01464435, 'focused')],
  -0.8679391969273703),
 ([(0.03605076, 'seen'),
   (0.027079739, 'you'),
   (0.025867406, 'company'),
   (0.025381353, 'get'),
   (0.020662623, 'job'),
   (0.0204971, 'role'),
   (0.02039554, 'tech'),
   (0.016097797, 'indeed'),
   (0.015394535, 'skill'),
   (0.015244444, 'ready')],
  -0.8902348660974885),
 ([(0.018508, 'insurance'),
   (0.017105794, 'engineer'),
   (0.016486999, 'system'),
   (0.011871413, 'senior'),
   (0.011837192, 'health'),
   (0.011593329, 'research'),
   (0.011473599, 'time'),
   (0.011324313, 'required'),
   (0.011321694, 'implement'),
   (0.011068108, 'inc')],
  -0.9634888832392112),
 ([(0.03216682, 'data'),
   (0.017860714, 'code'),
   (0.017611505, 'build'),
   (0.015358127, 'hadoop'),
   (0.015220426, 'business'),
   (0.014785984, 'rule'),
   (0.012926369, 'minimum'),
   (0.0123172505, 'application'),
   (0.012057946, 'pyspark'),
   (0.01193623, 'spark')],
  -1.1233787114499412)]

#import flask library
from flask import Flask, escape, url_for, render_template

#initialize flask app
app = Flask(__name__)

#Path to render the html to display the search page
@app.route('/')
def displaySearch():
    return render_template('landingpage.html')

#path to render the results page.  the searchQuery parameter is passed from the landing page.
@app.route('/result/<searchQuery>')
def diplayresult(searchQuery):

        labelsList = [] # list of labels for each topic
        dataList = [] #list of data points for each topic
        dataList_tot = []
        numTopics = len(sampleLDAObject) #num of topics

        #format data into a list of data points and labels
        for topicDist in sampleLDAObject:
            topicLabelList = []
            topicDataList = []
            topicDist = topicDist[0]  # remove average which is topic[1]
            for topic in topicDist:
                topicDataList.append(topic[0])
                topicLabelList.append(topic[1])
            labelsList.append(topicLabelList)
            dataList.append(topicDataList)
            # fake dataset cotaining probability of word
            dataList_tot.append([x*2 for x in topicDataList])

        return render_template('results.html', searchQuery=searchQuery, labels =labelsList, values=dataList, values_tot=dataList_tot,numTopics=numTopics )

#run flask app
if __name__ == '__main__':
    app.run()