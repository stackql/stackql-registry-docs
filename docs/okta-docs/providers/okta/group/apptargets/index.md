---
title: apptargets
hide_title: false
hide_table_of_contents: false
keywords:
  - apptargets
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
<tr><td><b>Name</b></td><td><code>apptargets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.apptargets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `lastUpdated` | `string` |
| `signOnModes` | `array` |
| `verificationStatus` | `string` |
| `displayName` | `string` |
| `category` | `string` |
| `status` | `string` |
| `_links` | `object` |
| `website` | `string` |
| `features` | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `groupId, roleId` | Lists all App targets for an `APP_ADMIN` Role assigned to a Group. This methods return list may include full Applications or Instances. The response for an instance will have an `ID` value, while Application will not have an ID. |
| `insert` | `INSERT` | `appName, groupId, roleId` | Success |
| `delete` | `DELETE` | `appName, groupId, roleId` | Success |
