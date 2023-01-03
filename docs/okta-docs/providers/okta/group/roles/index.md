---
title: roles
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
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `description` | `string` |
| `label` | `string` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `assignmentType` | `string` |
| `_embedded` | `object` |
| `type` | `string` |
| `_links` | `object` |
| `created` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `groupId, roleId` | Success |
| `list` | `SELECT` | `groupId` | Success |
| `insert` | `INSERT` | `groupId` | Assigns a Role to a Group |
| `delete` | `DELETE` | `groupId, roleId` | Unassigns a Role from a Group |
