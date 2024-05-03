---
title: org_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - org_permissions
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
<tr><td><b>Name</b></td><td><code>org_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.actions.org_permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allowed_actions" /> | `string` | The permissions policy that controls the actions and reusable workflows that are allowed to run. |
| <CopyableCode code="enabled_repositories" /> | `string` | The policy that controls the repositories in the organization that are allowed to run GitHub Actions. |
| <CopyableCode code="selected_actions_url" /> | `string` | The API URL to use to get or set the actions and reusable workflows that are allowed to run, when `allowed_actions` is set to `selected`. |
| <CopyableCode code="selected_repositories_url" /> | `string` | The API URL to use to get or set the selected repositories that are allowed to run GitHub Actions, when `enabled_repositories` is set to `selected`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_github_actions_permissions_organization" /> | `SELECT` | <CopyableCode code="org" /> | Gets the GitHub Actions permissions policy for repositories and allowed actions and reusable workflows in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| <CopyableCode code="set_github_actions_permissions_organization" /> | `EXEC` | <CopyableCode code="org, data__enabled_repositories" /> | Sets the GitHub Actions permissions policy for repositories and allowed actions and reusable workflows in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
