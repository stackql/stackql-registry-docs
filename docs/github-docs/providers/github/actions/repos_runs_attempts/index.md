---
title: repos_runs_attempts
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_runs_attempts
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
<tr><td><b>Name</b></td><td><code>repos_runs_attempts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.repos_runs_attempts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the workflow run. |
| `name` | `string` | The name of the workflow run. |
| `rerun_url` | `string` | The URL to rerun the workflow run. |
| `cancel_url` | `string` | The URL to cancel the workflow run. |
| `previous_attempt_url` | `string` | The URL to the previous attempted run of this workflow, if one exists. |
| `head_repository_id` | `integer` |  |
| `event` | `string` |  |
| `referenced_workflows` | `array` |  |
| `artifacts_url` | `string` | The URL to the artifacts for the workflow run. |
| `logs_url` | `string` | The URL to download the logs for the workflow run. |
| `check_suite_id` | `integer` | The ID of the associated check suite. |
| `head_sha` | `string` | The SHA of the head commit that points to the version of the workflow being run. |
| `head_branch` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `actor` | `object` | A GitHub user. |
| `display_title` | `string` | The event-specific title associated with the run or the run-name if set, or the value of `run-name` if it is set in the workflow. |
| `pull_requests` | `array` | Pull requests that are open with a `head_sha` or `head_branch` that matches the workflow run. The returned pull requests do not necessarily indicate pull requests that triggered the run. |
| `triggering_actor` | `object` | A GitHub user. |
| `url` | `string` | The URL to the workflow run. |
| `check_suite_url` | `string` | The URL to the associated check suite. |
| `html_url` | `string` |  |
| `head_repository` | `object` | Minimal Repository |
| `run_started_at` | `string` | The start time of the latest run. Resets on re-run. |
| `status` | `string` |  |
| `created_at` | `string` |  |
| `workflow_url` | `string` | The URL to the workflow. |
| `jobs_url` | `string` | The URL to the jobs for the workflow run. |
| `workflow_id` | `integer` | The ID of the parent workflow. |
| `path` | `string` | The full path of the workflow |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `run_attempt` | `integer` | Attempt number of the run, 1 for first attempt and higher if the workflow was re-run. |
| `conclusion` | `string` |  |
| `head_commit` | `object` | A commit. |
| `run_number` | `integer` | The auto incrementing run number for the workflow run. |
| `check_suite_node_id` | `string` | The node ID of the associated check suite. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_workflow_run_attempt` | `SELECT` | `attempt_number, owner, repo, run_id` | Gets a specific workflow run attempt. Anyone with read access to the repository<br />can use this endpoint. If the repository is private you must use an access token<br />with the `repo` scope. GitHub Apps must have the `actions:read` permission to<br />use this endpoint. |
| `download_workflow_run_attempt_logs` | `EXEC` | `attempt_number, owner, repo, run_id` | Gets a redirect URL to download an archive of log files for a specific workflow run attempt. This link expires after<br />1 minute. Look for `Location:` in the response header to find the URL for the download. Anyone with read access to<br />the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions:read` permission to use this endpoint. |
