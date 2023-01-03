---
title: feeds
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feeds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.feeds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `current_user_actor_url` | `string` |
| `current_user_organization_url` | `string` |
| `user_url` | `string` |
| `_links` | `object` |
| `current_user_url` | `string` |
| `security_advisories_url` | `string` |
| `current_user_public_url` | `string` |
| `timeline_url` | `string` |
| `current_user_organization_urls` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_feeds` | `SELECT` |  |
