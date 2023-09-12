---
title: repos_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_jobs
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
<tr><td><b>Name</b></td><td><code>repos_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.repos_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The id of the job. |
| `name` | `string` | The name of the job. |
| `runner_group_id` | `integer` | The ID of the runner group to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.) |
| `labels` | `array` | Labels for the workflow job. Specified by the "runs_on" attribute in the action's workflow file. |
| `url` | `string` |  |
| `head_sha` | `string` | The SHA of the commit that is being run. |
| `runner_name` | `string` | The name of the runner to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.) |
| `runner_group_name` | `string` | The name of the runner group to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.) |
| `run_url` | `string` |  |
| `status` | `string` | The phase of the lifecycle that the job is currently in. |
| `html_url` | `string` |  |
| `run_id` | `integer` | The id of the associated workflow run. |
| `head_branch` | `string` | The name of the current branch. |
| `created_at` | `string` | The time that the job created, in ISO 8601 format. |
| `node_id` | `string` |  |
| `workflow_name` | `string` | The name of the workflow. |
| `completed_at` | `string` | The time that the job finished, in ISO 8601 format. |
| `check_run_url` | `string` |  |
| `conclusion` | `string` | The outcome of the job. |
| `steps` | `array` | Steps in this job. |
| `run_attempt` | `integer` | Attempt number of the associated workflow run, 1 for first attempt and higher if the workflow was re-run. |
| `started_at` | `string` | The time that the job started, in ISO 8601 format. |
| `runner_id` | `integer` | The ID of the runner to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_job_for_workflow_run` | `SELECT` | `job_id, owner, repo` | Gets a specific job in a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `download_job_logs_for_workflow_run` | `EXEC` | `job_id, owner, repo` | Gets a redirect URL to download a plain text file of logs for a workflow job. This link expires after 1 minute. Look<br />for `Location:` in the response header to find the URL for the download. Anyone with read access to the repository can<br />use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must<br />have the `actions:read` permission to use this endpoint. |
| `re_run_job_for_workflow_run` | `EXEC` | `job_id, owner, repo` | Re-run a job and its dependent jobs in a workflow run.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions:write` permission to use this endpoint. |
