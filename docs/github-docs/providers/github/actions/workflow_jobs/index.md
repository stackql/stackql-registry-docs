---
title: workflow_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - actions
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.workflow_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `total_count` | `integer` |
| `jobs` | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_job_for_workflow_run` | `SELECT` | `job_id, owner, repo` | Gets a specific job in a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `list_jobs_for_workflow_run` | `SELECT` | `owner, repo, run_id` | Lists jobs for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters). |
| `list_jobs_for_workflow_run_attempt` | `SELECT` | `attempt_number, owner, repo, run_id` | Lists jobs for a specific workflow run attempt. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters). |
| `download_job_logs_for_workflow_run` | `EXEC` | `job_id, owner, repo` | Gets a redirect URL to download a plain text file of logs for a workflow job. This link expires after 1 minute. Look<br />for `Location:` in the response header to find the URL for the download. Anyone with read access to the repository can<br />use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must<br />have the `actions:read` permission to use this endpoint. |
