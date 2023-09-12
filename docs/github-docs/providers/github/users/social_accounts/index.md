---
title: social_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - social_accounts
  - users
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
<tr><td><b>Name</b></td><td><code>social_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.social_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `url` | `string` |
| `provider` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_social_accounts_for_user` | `SELECT` | `username` |
