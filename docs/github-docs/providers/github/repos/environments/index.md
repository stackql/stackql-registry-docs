---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The id of the environment. |
| <CopyableCode code="name" /> | `string` | The name of the environment. |
| <CopyableCode code="created_at" /> | `string` | The time that the environment was created, in ISO 8601 format. |
| <CopyableCode code="deployment_branch_policy" /> | `object` | The type of deployment branch policy for this environment. To allow all branches to deploy, set to `null`. |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="protection_rules" /> | `array` | Built-in deployment protection rules for the environment. |
| <CopyableCode code="updated_at" /> | `string` | The time that the environment was last updated, in ISO 8601 format. |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_all_environments" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists the environments for a repository.<br /><br />Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| <CopyableCode code="get_environment" /> | `SELECT` | <CopyableCode code="environment_name, owner, repo" /> | **Note:** To get information about name patterns that branches must match in order to deploy to this environment, see "[Get a deployment branch policy](/rest/deployments/branch-policies#get-a-deployment-branch-policy)."<br /><br />Anyone with read access to the repository can use this endpoint. If the<br />repository is private, you must use an access token with the `repo` scope. GitHub<br />Apps must have the `actions:read` permission to use this endpoint. |
| <CopyableCode code="create_or_update_environment" /> | `INSERT` | <CopyableCode code="environment_name, owner, repo" /> | Create or update an environment with protection rules, such as required reviewers. For more information about environment protection rules, see "[Environments](/actions/reference/environments#environment-protection-rules)."<br /><br />**Note:** To create or update name patterns that branches must match in order to deploy to this environment, see "[Deployment branch policies](/rest/deployments/branch-policies)."<br /><br />**Note:** To create or update secrets for an environment, see "[GitHub Actions secrets](/rest/actions/secrets)."<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration:write` permission for the repository to use this endpoint. |
| <CopyableCode code="delete_an_environment" /> | `DELETE` | <CopyableCode code="environment_name, owner, repo" /> | You must authenticate using an access token with the repo scope to use this endpoint. |
