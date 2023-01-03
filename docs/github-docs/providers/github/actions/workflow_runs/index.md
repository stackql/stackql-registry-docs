---
title: workflow_runs
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
<tr><td><b>Name</b></td><td><code>workflow_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.workflow_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the workflow run. |
| `name` | `string` | The name of the workflow run. |
| `logs_url` | `string` | The URL to download the logs for the workflow run. |
| `rerun_url` | `string` | The URL to rerun the workflow run. |
| `url` | `string` | The URL to the workflow run. |
| `head_repository` | `object` | Minimal Repository |
| `head_repository_id` | `integer` |  |
| `run_started_at` | `string` | The start time of the latest run. Resets on re-run. |
| `event` | `string` |  |
| `run_number` | `integer` | The auto incrementing run number for the workflow run. |
| `repository` | `object` | Minimal Repository |
| `html_url` | `string` |  |
| `updated_at` | `string` |  |
| `pull_requests` | `array` |  |
| `status` | `string` |  |
| `check_suite_url` | `string` | The URL to the associated check suite. |
| `workflow_url` | `string` | The URL to the workflow. |
| `jobs_url` | `string` | The URL to the jobs for the workflow run. |
| `node_id` | `string` |  |
| `created_at` | `string` |  |
| `conclusion` | `string` |  |
| `workflow_id` | `integer` | The ID of the parent workflow. |
| `artifacts_url` | `string` | The URL to the artifacts for the workflow run. |
| `check_suite_node_id` | `string` | The node ID of the associated check suite. |
| `run_attempt` | `integer` | Attempt number of the run, 1 for first attempt and higher if the workflow was re-run. |
| `head_branch` | `string` |  |
| `previous_attempt_url` | `string` | The URL to the previous attempted run of this workflow, if one exists. |
| `check_suite_id` | `integer` | The ID of the associated check suite. |
| `head_sha` | `string` | The SHA of the head commit that points to the version of the worflow being run. |
| `head_commit` | `object` | Simple Commit |
| `cancel_url` | `string` | The URL to cancel the workflow run. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_workflow_run` | `SELECT` | `owner, repo, run_id` | Gets a specific workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `get_workflow_run_attempt` | `SELECT` | `attempt_number, owner, repo, run_id` | Gets a specific workflow run attempt. Anyone with read access to the repository<br />can use this endpoint. If the repository is private you must use an access token<br />with the `repo` scope. GitHub Apps must have the `actions:read` permission to<br />use this endpoint. |
| `list_workflow_runs` | `SELECT` | `owner, repo, workflow_id` | List all workflow runs for a workflow. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters).<br /><br />Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. |
| `list_workflow_runs_for_repo` | `SELECT` | `owner, repo` | Lists all workflow runs for a repository. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters).<br /><br />Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `delete_workflow_run` | `DELETE` | `owner, repo, run_id` | Delete a specific workflow run. Anyone with write access to the repository can use this endpoint. If the repository is<br />private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:write` permission to use<br />this endpoint. |
| `cancel_workflow_run` | `EXEC` | `owner, repo, run_id` | Cancels a workflow run using its `id`. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint. |
| `delete_workflow_run_logs` | `EXEC` | `owner, repo, run_id` | Deletes all logs for a workflow run. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint. |
| `download_workflow_run_attempt_logs` | `EXEC` | `attempt_number, owner, repo, run_id` | Gets a redirect URL to download an archive of log files for a specific workflow run attempt. This link expires after<br />1 minute. Look for `Location:` in the response header to find the URL for the download. Anyone with read access to<br />the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `download_workflow_run_logs` | `EXEC` | `owner, repo, run_id` | Gets a redirect URL to download an archive of log files for a workflow run. This link expires after 1 minute. Look for<br />`Location:` in the response header to find the URL for the download. Anyone with read access to the repository can use<br />this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have<br />the `actions:read` permission to use this endpoint. |
| `re_run_workflow` | `EXEC` | `owner, repo, run_id` | Re-runs your workflow run using its `id`. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint. |
