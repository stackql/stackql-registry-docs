---
title: claims
hide_title: false
hide_table_of_contents: false
keywords:
  - okta
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>claims</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.claims</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `status` | `string` |
| `value` | `string` |
| `_links` | `object` |
| `alwaysIncludeInToken` | `boolean` |
| `conditions` | `object` |
| `system` | `boolean` |
| `valueType` | `string` |
| `claimType` | `string` |
| `group_filter_type` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `authServerId, claimId` |
| `list` | `SELECT` | `authServerId` |
| `insert` | `INSERT` | `authServerId` |
| `delete` | `DELETE` | `authServerId, claimId` |
| `update` | `EXEC` | `authServerId, claimId` |
