---
title: gpg_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - gpg_keys
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
<tr><td><b>Name</b></td><td><code>gpg_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.gpg_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `subkeys` | `array` |
| `emails` | `array` |
| `key_id` | `string` |
| `created_at` | `string` |
| `can_sign` | `boolean` |
| `can_certify` | `boolean` |
| `primary_key_id` | `integer` |
| `raw_key` | `string` |
| `expires_at` | `string` |
| `public_key` | `string` |
| `revoked` | `boolean` |
| `can_encrypt_storage` | `boolean` |
| `can_encrypt_comms` | `boolean` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_gpg_keys_for_user` | `SELECT` | `username` |
