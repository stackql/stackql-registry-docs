---
title: branch_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - branch_policies
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
<tr><td><b>Name</b></td><td><code>branch_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.branch_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The unique identifier of the branch policy. |
| <CopyableCode code="name" /> | `string` | The name pattern that branches must match in order to deploy to the environment. |
| <CopyableCode code="node_id" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_deployment_branch_policy" /> | `SELECT` | <CopyableCode code="branch_policy_id, environment_name, owner, repo" /> | Gets a deployment branch policy for an environment.<br /><br />Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| <CopyableCode code="list_deployment_branch_policies" /> | `SELECT` | <CopyableCode code="environment_name, owner, repo" /> | Lists the deployment branch policies for an environment.<br /><br />Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| <CopyableCode code="create_deployment_branch_policy" /> | `INSERT` | <CopyableCode code="environment_name, owner, repo, data__name" /> | Creates a deployment branch policy for an environment.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration:write` permission for the repository to use this endpoint. |
| <CopyableCode code="delete_deployment_branch_policy" /> | `DELETE` | <CopyableCode code="branch_policy_id, environment_name, owner, repo" /> | Deletes a deployment branch policy for an environment.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration:write` permission for the repository to use this endpoint. |
| <CopyableCode code="update_deployment_branch_policy" /> | `EXEC` | <CopyableCode code="branch_policy_id, environment_name, owner, repo, data__name" /> | Updates a deployment branch policy for an environment.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration:write` permission for the repository to use this endpoint. |
