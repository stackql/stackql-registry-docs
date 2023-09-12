---
title: repos_permissions_access
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_permissions_access
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repos_permissions_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.repos_permissions_access</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_workflow_access_to_repository` | `SELECT` | `owner, repo` | Gets the level of access that workflows outside of the repository have to actions and reusable workflows in the repository.<br />This endpoint only applies to private repositories.<br />For more information, see "[Allowing access to components in a private repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#allowing-access-to-components-in-a-private-repository)."<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the<br />repository `administration` permission to use this endpoint. |
| `set_workflow_access_to_repository` | `EXEC` | `owner, repo, data__access_level` | Sets the level of access that workflows outside of the repository have to actions and reusable workflows in the repository.<br />This endpoint only applies to private repositories.<br />For more information, see "[Allowing access to components in a private repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#allowing-access-to-components-in-a-private-repository)".<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the<br />repository `administration` permission to use this endpoint. |
