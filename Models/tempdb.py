class Tempdb:

    def __init__(self, tempid=0, rmbavailable=0, rmbavailable2=0, submission="", usersubmissionid=0, alreadysubmitted=0):
        self.tempid = tempid
        self.rmbavailable = rmbavailable
        self.rmbavailable2 = rmbavailable2
        self.submission = submission
        self.usersubmissionid = usersubmissionid
        self.alreadysubmitted = alreadysubmitted

    def __repr__(self):
        return str({
            "tempId": self.tempid,
            "rmbAvailable": self.rmbavailable,
            "rmbAvailable2": self.rmbavailable2,
            "submission": self.submission,
            "userSubmission": self.usersubmissionid,
            "alreadySubmitted": self.alreadysubmitted
        })

    def json(self):
        return {
            "tempId": self.tempid,
            "rmbAvailable": self.rmbavailable,
            "rmbAvailable2": self.rmbavailable2,
            "submission": self.submission,
            "userSubmission": self.usersubmissionid,
            "alreadySubmitted": self.alreadysubmitted
        }