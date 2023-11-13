# Postmortem: Web Stack Outage Incident
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/pQ9YzVY.gif)

## Issue Summary:
- **Duration:** 
  - Start Time: November 12, 2023, 15:30 UTC
  - End Time: November 12, 2023, 18:45 UTC
- **Impact:**
  - Affecting 30% of our user base
  - Sluggish performance and intermittent service disruptions on the e-commerce platform
- **Root Cause:**
  - Database connection pool exhaustion due to a misconfiguration in the connection pool settings.

## Timeline:
![](https://www.google.com/url?sa=i&url=https%3A%2F%2Fmedium.com%2Fganttpro-blog%2Ftimeline-examples-and-tips-on-how-to-use-them-a1ec2aab9f9a&psig=AOvVaw2K1VsMFc7h_9HAJigkCSp&ust=1699929046437000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCODIp7z3v4IDFQAAAAAdAAAAABAE)
- **15:30 UTC: Issue Detected**
  - Monitoring alerts triggered due to an increase in response times.
- **15:35 UTC: Issue Identification**
  The engineering team started investigating the elevated response times.
- **16:00 UTC: Initial Assumptions**
  - Assumed increased traffic due to ongoing promotion causing server overload.
  - Investigated server logs and application code for potential bottlenecks.
- **16:45 UTC: Misleading Paths**
  - A temporary fix was attempted by scaling up server instances, but there was no significant improvement.
  - Investigated network infrastructure assuming potential issues with the CDN.
- **17:15 UTC: Escalation**
  - The incident escalated to the Database Operations team as anomalies in database performance surfaced.
- **17:45 UTC: Root Cause Identification**
  - Database connection pool misconfiguration was identified as the root cause.
  - Misconfigured pool settings causing a rapid increase in open connections, leading to exhaustion.
- **18:00 UTC: Resolution**
  - Adjusted database connection pool settings to accommodate the increased load.
  - Conducted rolling restart of affected servers to apply the configuration changes.
- **18:45 UTC: Issue Resolved**
  - Monitoring tools indicated a significant drop in response times, confirming the resolution.

## Root Cause and Resolution:
- **Root Cause:**
  - The misconfiguration in the database connection pool settings led to a rapid increase in open connections, exhausting available resources.
- **Resolution:**
  - Adjusted connection pool settings to increase the allowed connections and implemented a rolling restart to apply the changes without service downtime.

## Corrective and Preventative Measures:
- **Improvements/Fixes:**
  - Enhanced monitoring for connection pool metrics to detect anomalies early.
  - Implement automated scaling policies to handle sudden spikes in traffic.
  - Conduct regular reviews of system configurations to identify potential misconfigurations.
- **Tasks:**
  - Implement automated alerting for abnormal connection pool behavior.
  - Conduct a comprehensive audit of system configurations for potential misconfigurations.
  - Develop and document a protocol for handling misconfigurations in critical system components.
  - Evaluate the feasibility of implementing auto-scaling solutions to dynamically adjust resources based on demand.

## Conclusion:
In conclusion, the web stack outage was a result of a misconfigured database connection pool, causing service disruptions and sluggish performance. The incident was resolved by adjusting the connection pool settings and conducting a rolling restart. Moving forward, the team will implement measures to enhance monitoring, automate scaling, and conduct regular configuration audits to prevent similar incidents in the future.
