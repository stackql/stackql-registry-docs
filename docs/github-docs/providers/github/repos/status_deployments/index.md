---
title: status_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - status_deployments
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
<tr><td><b>Name</b></td><td><code>status_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.status_deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="description" /> | `string` | A short description of the status. |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="creator" /> | `object` | A GitHub user. |
| <CopyableCode code="deployment_url" /> | `string` |  |
| <CopyableCode code="environment" /> | `string` | The environment of the deployment that the status is for. |
| <CopyableCode code="environment_url" /> | `string` | The URL for accessing your environment. |
| <CopyableCode code="log_url" /> | `string` | The URL to associate with this status. |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="performed_via_github_app" /> | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| <CopyableCode code="repository_url" /> | `string` |  |
| <CopyableCode code="state" /> | `string` | The state of the status. |
| <CopyableCode code="target_url" /> | `string` | Deprecated: the URL to associate with this status. |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_deployment_status" /> | `SELECT` | <CopyableCode code="deployment_id, owner, repo, status_id" /> | Users with pull access can view a deployment status for a deployment: |
| <CopyableCode code="list_deployment_statuses" /> | `SELECT` | <CopyableCode code="deployment_id, owner, repo" /> | Users with pull access can view deployment statuses for a deployment: |
| <CopyableCode code="create_deployment_status" /> | `INSERT` | <CopyableCode code="deployment_id, owner, repo, data__state" /> | Users with `push` access can create deployment statuses for a given deployment.<br /><br />GitHub Apps require `read & write` access to "Deployments" and `read-only` access to "Repo contents" (for private repos). OAuth apps require the `repo_deployment` scope. |
