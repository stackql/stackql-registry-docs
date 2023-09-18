---
title: user_public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - user_public_keys
  - codespaces
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
<tr><td><b>Name</b></td><td><code>user_public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.user_public_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `key` | `string` | The Base64 encoded public key. |
| `key_id` | `string` | The identifier for the key. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_public_key_for_authenticated_user` | `SELECT` |  |
