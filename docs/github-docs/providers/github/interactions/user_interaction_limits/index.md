---
title: user_interaction_limits
hide_title: false
hide_table_of_contents: false
keywords:
  - user_interaction_limits
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
<tr><td><b>Name</b></td><td><code>user_interaction_limits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.interactions.user_interaction_limits</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `remove_restrictions_for_authenticated_user` | `DELETE` |  | Removes any interaction restrictions from your public repositories. |
| `get_restrictions_for_authenticated_user` | `EXEC` |  | Shows which type of GitHub user can interact with your public repositories and when the restriction expires. |
| `set_restrictions_for_authenticated_user` | `EXEC` | `data__limit` | Temporarily restricts which type of GitHub user can interact with your public repositories. Setting the interaction limit at the user level will overwrite any interaction limits that are set for individual repositories owned by the user. |
