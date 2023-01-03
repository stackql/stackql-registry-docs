---
title: policies
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `system` | `boolean` |
| `_embedded` | `object` |
| `status` | `string` |
| `_links` | `object` |
| `priority` | `integer` |
| `created` | `string` |
| `lastUpdated` | `string` |
| `type` | `string` |
| `conditions` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `authServerId, policyId` | Success |
| `list` | `SELECT` | `authServerId` | Success |
| `insert` | `INSERT` | `authServerId` | Success |
| `delete` | `DELETE` | `authServerId, policyId` | Success |
| `activate` | `EXEC` | `authServerId, policyId` | Activate Authorization Server Policy |
| `deactivate` | `EXEC` | `authServerId, policyId` | Deactivate Authorization Server Policy |
| `update` | `EXEC` | `authServerId, policyId` | Success |
