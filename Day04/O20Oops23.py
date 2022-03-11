
# Duck typing
class Manager:
    def doJob(self):
        print("Manager's Job.....")

class Developer:
    def doJob(self):
        print("Developer's Job......")

manoj = Manager()
dev = Developer()

def BankfunJobs(emps):
    print("Started".center(40, "-"))
    for emp in emps:
        emp.doJob()
    print("Completed".center(40, "-"))
    print("-" * 40)


BankfunJobs([manoj, dev])
