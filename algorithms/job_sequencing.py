def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    n = len(jobs)
    result = [-1]*n
    slot = [False]*n
    for i in range(n):
        for j in range(min(n-1, jobs[i][1]-1), -1, -1):
            if not slot[j]:
                result[j] = jobs[i][0]
                slot[j] = True
                break
    return [job for job in result if job != -1]
