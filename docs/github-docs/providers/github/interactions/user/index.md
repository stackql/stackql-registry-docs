---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - interactions
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
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.interactions.user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `expires_at` | `string` |  |
| `limit` | `string` | The type of GitHub user that can comment, open issues, or create pull requests while the interaction limit is in effect. |
| `origin` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_restrictions_for_authenticated_user` | `SELECT` |  | Shows which type of GitHub user can interact with your public repositories and when the restriction expires. |
| `remove_restrictions_for_authenticated_user` | `DELETE` |  | Removes any interaction restrictions from your public repositories. |
| `set_restrictions_for_authenticated_user` | `EXEC` | `data__limit` | Temporarily restricts which type of GitHub user can interact with your public repositories. Setting the interaction limit at the user level will overwrite any interaction limits that are set for individual repositories owned by the user. |
