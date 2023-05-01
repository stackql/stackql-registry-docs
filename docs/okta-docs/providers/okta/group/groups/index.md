---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - group
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `lastUpdated` | `string` |
| `_embedded` | `object` |
| `type` | `string` |
| `profile` | `object` |
| `_links` | `object` |
| `lastMembershipUpdated` | `string` |
| `objectClass` | `array` |
| `created` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `groupId` | Fetches a group from your organization. |
| `list` | `SELECT` |  | Enumerates groups in your organization with pagination. A subset of groups can be returned that match a supported filter expression or query. |
| `insert` | `INSERT` |  | Adds a new group with `OKTA_GROUP` type to your organization. |
| `delete` | `DELETE` | `groupId` | Removes a group with `OKTA_GROUP` type from your organization. |
| `update` | `EXEC` | `groupId` | Updates the profile for a group with `OKTA_GROUP` type from your organization. |
