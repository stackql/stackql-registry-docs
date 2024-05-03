---
title: pending_deployments_for_run
hide_title: false
hide_table_of_contents: false
keywords:
  - pending_deployments_for_run
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pending_deployments_for_run</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.actions.pending_deployments_for_run" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="current_user_can_approve" /> | `boolean` | Whether the currently authenticated user can approve the deployment |
| <CopyableCode code="environment" /> | `object` |  |
| <CopyableCode code="reviewers" /> | `array` | The people or teams that may approve jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed. |
| <CopyableCode code="wait_timer" /> | `integer` | The set duration of the wait timer |
| <CopyableCode code="wait_timer_started_at" /> | `string` | The time that the wait timer began. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_pending_deployments_for_run" /> | `SELECT` | <CopyableCode code="owner, repo, run_id" /> | Get all deployment environments for a workflow run that are waiting for protection rules to pass.<br /><br />Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| <CopyableCode code="review_pending_deployments_for_run" /> | `EXEC` | <CopyableCode code="owner, repo, run_id, data__comment, data__environment_ids, data__state" /> | Approve or reject pending deployments that are waiting on approval by a required reviewer.<br /><br />Required reviewers with read access to the repository contents and deployments can use this endpoint. Required reviewers must authenticate using an access token with the `repo` scope to use this endpoint. |
