---
title: workflow_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_jobs
  - actions
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.workflow_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The id of the job. |
| `name` | `string` | The name of the job. |
| `steps` | `array` | Steps in this job. |
| `status` | `string` | The phase of the lifecycle that the job is currently in. |
| `run_id` | `integer` | The id of the associated workflow run. |
| `runner_name` | `string` | The name of the runner to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.) |
| `run_url` | `string` |  |
| `runner_group_name` | `string` | The name of the runner group to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.) |
| `conclusion` | `string` | The outcome of the job. |
| `head_sha` | `string` | The SHA of the commit that is being run. |
| `node_id` | `string` |  |
| `labels` | `array` | Labels for the workflow job. Specified by the "runs_on" attribute in the action's workflow file. |
| `url` | `string` |  |
| `completed_at` | `string` | The time that the job finished, in ISO 8601 format. |
| `runner_id` | `integer` | The ID of the runner to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.) |
| `run_attempt` | `integer` | Attempt number of the associated workflow run, 1 for first attempt and higher if the workflow was re-run. |
| `started_at` | `string` | The time that the job started, in ISO 8601 format. |
| `html_url` | `string` |  |
| `check_run_url` | `string` |  |
| `runner_group_id` | `integer` | The ID of the runner group to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_job_for_workflow_run` | `SELECT` | `job_id, owner, repo` | Gets a specific job in a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `list_jobs_for_workflow_run` | `SELECT` | `owner, repo, run_id` | Lists jobs for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters). |
| `list_jobs_for_workflow_run_attempt` | `SELECT` | `attempt_number, owner, repo, run_id` | Lists jobs for a specific workflow run attempt. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters). |
| `download_job_logs_for_workflow_run` | `EXEC` | `job_id, owner, repo` | Gets a redirect URL to download a plain text file of logs for a workflow job. This link expires after 1 minute. Look<br />for `Location:` in the response header to find the URL for the download. Anyone with read access to the repository can<br />use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must<br />have the `actions:read` permission to use this endpoint. |
