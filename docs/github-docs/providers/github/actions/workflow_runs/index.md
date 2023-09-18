---
title: workflow_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_runs
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
<tr><td><b>Name</b></td><td><code>workflow_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.workflow_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the workflow run. |
| `name` | `string` | The name of the workflow run. |
| `head_sha` | `string` | The SHA of the head commit that points to the version of the workflow being run. |
| `event` | `string` |  |
| `triggering_actor` | `object` | A GitHub user. |
| `rerun_url` | `string` | The URL to rerun the workflow run. |
| `check_suite_id` | `integer` | The ID of the associated check suite. |
| `artifacts_url` | `string` | The URL to the artifacts for the workflow run. |
| `check_suite_url` | `string` | The URL to the associated check suite. |
| `updated_at` | `string` |  |
| `run_number` | `integer` | The auto incrementing run number for the workflow run. |
| `run_started_at` | `string` | The start time of the latest run. Resets on re-run. |
| `head_repository` | `object` | Minimal Repository |
| `jobs_url` | `string` | The URL to the jobs for the workflow run. |
| `head_branch` | `string` |  |
| `head_repository_id` | `integer` |  |
| `status` | `string` |  |
| `logs_url` | `string` | The URL to download the logs for the workflow run. |
| `referenced_workflows` | `array` |  |
| `previous_attempt_url` | `string` | The URL to the previous attempted run of this workflow, if one exists. |
| `created_at` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `pull_requests` | `array` | Pull requests that are open with a `head_sha` or `head_branch` that matches the workflow run. The returned pull requests do not necessarily indicate pull requests that triggered the run. |
| `check_suite_node_id` | `string` | The node ID of the associated check suite. |
| `cancel_url` | `string` | The URL to cancel the workflow run. |
| `head_commit` | `object` | A commit. |
| `url` | `string` | The URL to the workflow run. |
| `workflow_url` | `string` | The URL to the workflow. |
| `workflow_id` | `integer` | The ID of the parent workflow. |
| `html_url` | `string` |  |
| `display_title` | `string` | The event-specific title associated with the run or the run-name if set, or the value of `run-name` if it is set in the workflow. |
| `run_attempt` | `integer` | Attempt number of the run, 1 for first attempt and higher if the workflow was re-run. |
| `node_id` | `string` |  |
| `actor` | `object` | A GitHub user. |
| `conclusion` | `string` |  |
| `path` | `string` | The full path of the workflow |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_workflow_run` | `SELECT` | `owner, repo, run_id` | Gets a specific workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `get_workflow_run_attempt` | `SELECT` | `attempt_number, owner, repo, run_id` | Gets a specific workflow run attempt. Anyone with read access to the repository<br />can use this endpoint. If the repository is private you must use an access token<br />with the `repo` scope. GitHub Apps must have the `actions:read` permission to<br />use this endpoint. |
| `list_workflow_runs` | `SELECT` | `owner, repo, workflow_id` | List all workflow runs for a workflow. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters).<br /><br />Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. |
| `list_workflow_runs_for_repo` | `SELECT` | `owner, repo` | Lists all workflow runs for a repository. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters).<br /><br />Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `delete_workflow_run` | `DELETE` | `owner, repo, run_id` | Delete a specific workflow run. Anyone with write access to the repository can use this endpoint. If the repository is<br />private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:write` permission to use<br />this endpoint. |
| `approve_workflow_run` | `EXEC` | `owner, repo, run_id` | Approves a workflow run for a pull request from a public fork of a first time contributor. For more information, see ["Approving workflow runs from public forks](https://docs.github.com/actions/managing-workflow-runs/approving-workflow-runs-from-public-forks)."<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint. |
| `cancel_workflow_run` | `EXEC` | `owner, repo, run_id` | Cancels a workflow run using its `id`.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions:write` permission to use this endpoint. |
| `re_run_job_for_workflow_run` | `EXEC` | `job_id, owner, repo` | Re-run a job and its dependent jobs in a workflow run.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions:write` permission to use this endpoint. |
| `re_run_workflow` | `EXEC` | `owner, repo, run_id` | Re-runs your workflow run using its `id`. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint. |
| `re_run_workflow_failed_jobs` | `EXEC` | `owner, repo, run_id` | Re-run all of the failed jobs and their dependent jobs in a workflow run using the `id` of the workflow run. You must authenticate using an access token with the `repo` scope to use this endpoint. |
| `review_custom_gates_for_run` | `EXEC` | `owner, repo, run_id, data__comment, data__environment_name` | Approve or reject custom deployment protection rules provided by a GitHub App for a workflow run. For more information, see "[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment)."<br /><br />**Note:** GitHub Apps can only review their own custom deployment protection rules.<br />To approve or reject pending deployments that are waiting for review from a specific person or team, see [`POST /repos/&#123;owner&#125;/&#123;repo&#125;/actions/runs/&#123;run_id&#125;/pending_deployments`](/rest/actions/workflow-runs#review-pending-deployments-for-a-workflow-run).<br /><br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have read and write permission for **Deployments** to use this endpoint. |
