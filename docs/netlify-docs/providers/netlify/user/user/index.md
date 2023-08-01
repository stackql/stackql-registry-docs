---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - user
  - netlify    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.user.user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `affiliate_id` | `string` |
| `avatar_url` | `string` |
| `uid` | `string` |
| `created_at` | `string` |
| `onboarding_progress` | `object` |
| `email` | `string` |
| `site_count` | `integer` |
| `login_providers` | `array` |
| `full_name` | `string` |
| `last_login` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getCurrentUser` | `SELECT` |  |
