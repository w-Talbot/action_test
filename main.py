
def check_diff( ga, gb ):
    # Needs to loop through each piece of several files, check them as groups
    for i in range(3):
        for i in instruments_group_a:
            print("push to git no errors")


instruments_group_a = ["first_name", "last_name", "dob", "sex", "weight"]
instruments_group_b = ["first_name", "last_name", "dob", "sex", "weight"]

survey_queue_a = {"contact_details":1 , "screening_log":2 , "consent":3, "randomisation":4, "randomisation_outcome":5}
survey_queue_b = {"contact_details":1 , "screening_log":2 , "consent":3, "randomisation":4, "randomisation_outcome":5}

crfs_a = ["contact_details", "screening_log", "consent",  "randomisation", "randomisation_outcome" ]
crfs_b = ["contact_details", "screening_log", "consent",  "randomisation", "randomisation_outcome" ]

group_a = [instruments_group_a, survey_queue_a, crfs_a]
group_b = [instruments_group_b, survey_queue_b, crfs_b]

check_diff(group_a, group_a)