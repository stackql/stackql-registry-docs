---
title: status_commits
hide_title: false
hide_table_of_contents: false
keywords:
  - status_commits
  - repos
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
<tr><td><b>Name</b></td><td><code>status_commits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.status_commits" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="avatar_url" /> | `string` |  |
| <CopyableCode code="context" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="creator" /> | `object` | A GitHub user. |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="state" /> | `string` |  |
| <CopyableCode code="target_url" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_commit_statuses_for_ref" /> | `SELECT` | <CopyableCode code="owner, ref, repo" /> | Users with pull access in a repository can view commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name. Statuses are returned in reverse chronological order. The first status in the list will be the latest one.<br /><br />This resource is also available via a legacy route: `GET /repos/:owner/:repo/statuses/:ref`. |
| <CopyableCode code="create_commit_status" /> | `INSERT` | <CopyableCode code="owner, repo, sha, data__state" /> | Users with push access in a repository can create commit statuses for a given SHA.<br /><br />Note: there is a limit of 1000 statuses per `sha` and `context` within a repository. Attempts to create more than 1000 statuses will result in a validation error. |
