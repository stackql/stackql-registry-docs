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
| `avatar_url` | `string` |
| `login_providers` | `array` |
| `last_login` | `string` |
| `onboarding_progress` | `object` |
| `affiliate_id` | `string` |
| `site_count` | `integer` |
| `uid` | `string` |
| `created_at` | `string` |
| `email` | `string` |
| `full_name` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getCurrentUser` | `SELECT` |  |
