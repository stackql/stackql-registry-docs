---
title: suites
hide_title: false
hide_table_of_contents: false
keywords:
  - suites
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
<tr><td><b>Name</b></td><td><code>suites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.checks.suites" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="after" /> | `string` |  |
| <CopyableCode code="app" /> | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| <CopyableCode code="before" /> | `string` |  |
| <CopyableCode code="check_runs_url" /> | `string` |  |
| <CopyableCode code="conclusion" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="head_branch" /> | `string` |  |
| <CopyableCode code="head_commit" /> | `object` | A commit. |
| <CopyableCode code="head_sha" /> | `string` | The SHA of the head commit that is being checked. |
| <CopyableCode code="latest_check_runs_count" /> | `integer` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="pull_requests" /> | `array` |  |
| <CopyableCode code="repository" /> | `object` | Minimal Repository |
| <CopyableCode code="rerequestable" /> | `boolean` |  |
| <CopyableCode code="runs_rerequestable" /> | `boolean` |  |
| <CopyableCode code="status" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_suite" /> | `SELECT` | <CopyableCode code="check_suite_id, owner, repo" /> | **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array and a `null` value for `head_branch`.<br /><br />Gets a single check suite using its `id`. GitHub Apps must have the `checks:read` permission on a private repository or pull access to a public repository to get check suites. OAuth apps and authenticated users must have the `repo` scope to get check suites in a private repository. |
| <CopyableCode code="list_suites_for_ref" /> | `SELECT` | <CopyableCode code="owner, ref, repo" /> | **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array and a `null` value for `head_branch`.<br /><br />Lists check suites for a commit `ref`. The `ref` can be a SHA, branch name, or a tag name. GitHub Apps must have the `checks:read` permission on a private repository or pull access to a public repository to list check suites. OAuth apps and authenticated users must have the `repo` scope to get check suites in a private repository. |
| <CopyableCode code="create_suite" /> | `INSERT` | <CopyableCode code="owner, repo, data__head_sha" /> | **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array and a `null` value for `head_branch`.<br /><br />By default, check suites are automatically created when you create a [check run](https://docs.github.com/rest/checks/runs). You only need to use this endpoint for manually creating check suites when you've disabled automatic creation using "[Update repository preferences for check suites](https://docs.github.com/rest/checks/suites#update-repository-preferences-for-check-suites)". Your GitHub App must have the `checks:write` permission to create check suites. |
| <CopyableCode code="rerequest_suite" /> | `EXEC` | <CopyableCode code="check_suite_id, owner, repo" /> | Triggers GitHub to rerequest an existing check suite, without pushing new code to a repository. This endpoint will trigger the [`check_suite` webhook](https://docs.github.com/webhooks/event-payloads/#check_suite) event with the action `rerequested`. When a check suite is `rerequested`, its `status` is reset to `queued` and the `conclusion` is cleared.<br /><br />To rerequest a check suite, your GitHub App must have the `checks:write` permission on a private repository or pull access to a public repository. |
| <CopyableCode code="set_suites_preferences" /> | `EXEC` | <CopyableCode code="owner, repo" /> | Changes the default automatic flow when creating check suites. By default, a check suite is automatically created each time code is pushed to a repository. When you disable the automatic creation of check suites, you can manually [Create a check suite](https://docs.github.com/rest/checks/suites#create-a-check-suite). You must have admin permissions in the repository to set preferences for check suites. |
