---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
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
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.actions.permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allowed_actions" /> | `string` | The permissions policy that controls the actions and reusable workflows that are allowed to run. |
| <CopyableCode code="enabled" /> | `boolean` | Whether GitHub Actions is enabled on the repository. |
| <CopyableCode code="selected_actions_url" /> | `string` | The API URL to use to get or set the actions and reusable workflows that are allowed to run, when `allowed_actions` is set to `selected`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_github_actions_permissions_repository" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Gets the GitHub Actions permissions policy for a repository, including whether GitHub Actions is enabled and the actions and reusable workflows allowed to run in the repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration` repository permission to use this API. |
| <CopyableCode code="set_github_actions_permissions_repository" /> | `EXEC` | <CopyableCode code="owner, repo, data__enabled" /> | Sets the GitHub Actions permissions policy for enabling GitHub Actions and allowed actions and reusable workflows in the repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration` repository permission to use this API. |
