---
title: protection_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_rules
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
<tr><td><b>Name</b></td><td><code>protection_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.protection_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The unique identifier for the deployment protection rule. |
| <CopyableCode code="app" /> | `object` | A GitHub App that is providing a custom deployment protection rule. |
| <CopyableCode code="enabled" /> | `boolean` | Whether the deployment protection rule is enabled for the environment. |
| <CopyableCode code="node_id" /> | `string` | The node ID for the deployment protection rule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_all_deployment_protection_rules" /> | `SELECT` | <CopyableCode code="environment_name, owner, repo" /> | Gets all custom deployment protection rules that are enabled for an environment. Anyone with read access to the repository can use this endpoint. If the repository is private and you want to use a personal access token (classic), you must use an access token with the `repo` scope. GitHub Apps and fine-grained personal access tokens must have the `actions:read` permission to use this endpoint. For more information about environments, see "[Using environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)."<br /><br />For more information about the app that is providing this custom deployment rule, see the [documentation for the `GET /apps/&#123;app_slug&#125;` endpoint](https://docs.github.com/rest/apps/apps#get-an-app). |
| <CopyableCode code="get_custom_deployment_protection_rule" /> | `SELECT` | <CopyableCode code="environment_name, owner, protection_rule_id, repo" /> | Gets an enabled custom deployment protection rule for an environment. Anyone with read access to the repository can use this endpoint. If the repository is private and you want to use a personal access token (classic), you must use an access token with the `repo` scope. GitHub Apps and fine-grained personal access tokens must have the `actions:read` permission to use this endpoint. For more information about environments, see "[Using environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)."<br /><br />For more information about the app that is providing this custom deployment rule, see [`GET /apps/&#123;app_slug&#125;`](https://docs.github.com/rest/apps/apps#get-an-app). |
| <CopyableCode code="create_deployment_protection_rule" /> | `INSERT` | <CopyableCode code="environment_name, owner, repo" /> | Enable a custom deployment protection rule for an environment.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. Enabling a custom protection rule requires admin or owner permissions to the repository. GitHub Apps must have the `actions:write` permission to use this endpoint.<br /><br />For more information about the app that is providing this custom deployment rule, see the [documentation for the `GET /apps/&#123;app_slug&#125;` endpoint](https://docs.github.com/rest/apps/apps#get-an-app). |
| <CopyableCode code="disable_deployment_protection_rule" /> | `EXEC` | <CopyableCode code="environment_name, owner, protection_rule_id, repo" /> | Disables a custom deployment protection rule for an environment.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. Removing a custom protection rule requires admin or owner permissions to the repository. GitHub Apps must have the `actions:write` permission to use this endpoint. For more information, see "[Get an app](https://docs.github.com/rest/apps/apps#get-an-app)". |
