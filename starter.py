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
#missing = enrollment_unique.difference(engagement_unique)
#missing_key = missing.pop()
#for e in enrollments:
#	if e['account_key'] == missing_key:
#		print e
#		break