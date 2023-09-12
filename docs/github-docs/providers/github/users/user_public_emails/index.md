---
title: user_public_emails
hide_title: false
hide_table_of_contents: false
keywords:
  - user_public_emails
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
<tr><td><b>Name</b></td><td><code>user_public_emails</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.user_public_emails</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `email` | `string` |
| `primary` | `boolean` |
| `verified` | `boolean` |
| `visibility` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public_emails_for_authenticated_user` | `SELECT` |  |
