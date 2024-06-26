---
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - runs
  - checks
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.checks.runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The id of the check. |
| <CopyableCode code="name" /> | `string` | The name of the check. |
| <CopyableCode code="app" /> | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| <CopyableCode code="check_suite" /> | `object` |  |
| <CopyableCode code="completed_at" /> | `string` |  |
| <CopyableCode code="conclusion" /> | `string` |  |
| <CopyableCode code="deployment" /> | `object` | A deployment created as the result of an Actions check run from a workflow that references an environment |
| <CopyableCode code="details_url" /> | `string` |  |
| <CopyableCode code="external_id" /> | `string` |  |
| <CopyableCode code="head_sha" /> | `string` | The SHA of the commit that is being checked. |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="output" /> | `object` |  |
| <CopyableCode code="pull_requests" /> | `array` | Pull requests that are open with a `head_sha` or `head_branch` that matches the check. The returned pull requests do not necessarily indicate pull requests that triggered the check. |
| <CopyableCode code="started_at" /> | `string` |  |
| <CopyableCode code="status" /> | `string` | The phase of the lifecycle that the check is currently in. |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="check_run_id, owner, repo" /> | **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.<br /><br />Gets a single check run using its `id`. GitHub Apps must have the `checks:read` permission on a private repository or pull access to a public repository to get check runs. OAuth apps and authenticated users must have the `repo` scope to get check runs in a private repository. |
| <CopyableCode code="list_for_ref" /> | `SELECT` | <CopyableCode code="owner, ref, repo" /> | **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.<br /><br />Lists check runs for a commit ref. The `ref` can be a SHA, branch name, or a tag name. GitHub Apps must have the `checks:read` permission on a private repository or pull access to a public repository to get check runs. OAuth apps and authenticated users must have the `repo` scope to get check runs in a private repository. |
| <CopyableCode code="list_for_suite" /> | `SELECT` | <CopyableCode code="check_suite_id, owner, repo" /> | **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.<br /><br />Lists check runs for a check suite using its `id`. GitHub Apps must have the `checks:read` permission on a private repository or pull access to a public repository to get check runs. OAuth apps and authenticated users must have the `repo` scope to get check runs in a private repository. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="owner, repo, data__head_sha, data__name" /> | **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.<br /><br />Creates a new check run for a specific commit in a repository. Your GitHub App must have the `checks:write` permission to create check runs.<br /><br />In a check suite, GitHub limits the number of check runs with the same name to 1000. Once these check runs exceed 1000, GitHub will start to automatically delete older check runs. |
| <CopyableCode code="rerequest_run" /> | `EXEC` | <CopyableCode code="check_run_id, owner, repo" /> | Triggers GitHub to rerequest an existing check run, without pushing new code to a repository. This endpoint will trigger the [`check_run` webhook](https://docs.github.com/webhooks/event-payloads/#check_run) event with the action `rerequested`. When a check run is `rerequested`, its `status` is reset to `queued` and the `conclusion` is cleared.<br /><br />To rerequest a check run, your GitHub App must have the `checks:read` permission on a private repository or pull access to a public repository.<br /><br />For more information about how to re-run GitHub Actions jobs, see "[Re-run a job from a workflow run](https://docs.github.com/rest/actions/workflow-runs#re-run-a-job-from-a-workflow-run)". |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="check_run_id, owner, repo" /> | **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.<br /><br />Updates a check run for a specific commit in a repository. Your GitHub App must have the `checks:write` permission to edit check runs. |
