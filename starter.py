import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

# Find number of rows in the table
def find_rows(list):
    return len(list)

# Find number of unique students in table
def find_unique(list):
	keys = set()
	for i in list:
		keys.add(i['account_key'])
	return keys

enrollment_num_rows = find_rows(enrollments)
enrollment_unique = find_unique(enrollments)
enrollment_num_unique_students = len(enrollment_unique)

engagement_num_rows = find_rows(daily_engagement)
for d in daily_engagement:
	d['account_key'] = d['acct']
	del d['acct']
engagement_unique = find_unique(daily_engagement)
engagement_num_unique_students = len(engagement_unique)

submission_num_rows = find_rows(project_submissions)
submission_unique = find_unique(project_submissions)
submission_num_unique_students = len(submission_unique)

# Students in enrollment but not in engagement
missing = enrollment_unique.difference(engagement_unique)
missing_key = missing.pop()
for e in enrollments:
	if e['account_key'] == missing_key:
		#print e
		break

# Number of problem students
num_problem_students = 0
for e in enrollments:
	key = e['account_key']
	if key not in engagement_unique and e['join_date'] != e['cancel_date']:
		num_problem_students += 1
#print num_problem_students

# Remove Udacity accounts
udacity_keys = []
for e in enrollments:
	if e['is_udacity'] == 'True':
		udacity_keys.append(e['account_key'])

def remove_udacity(list):
	non_udacity_data = []
	for i in list:
		if i['account_key'] not in udacity_keys:
			non_udacity_data.append(i)
	return non_udacity_data

non_udacity_enrollment = remove_udacity(enrollments)
non_udacity_engagement = remove_udacity(daily_engagement)
non_udacity_submission = remove_udacity(project_submissions)

#print len(non_udacity_enrollment)
#print len(non_udacity_engagement)
#print len(non_udacity_submission)

# Getting started with cleaning up data
# Refining the Question

paid_students = {}
for e in non_udacity_enrollment:
	if e['is_canceled'] == 'False' or e['days_to_cancel'] > '7':
		account_key = e['account_key']
		enrollment_date = e['join_date']
		paid_students[account_key] = enrollment_date
#print len(paid_students)