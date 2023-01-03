---
title: appadmintargets
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
<tr><td><b>Name</b></td><td><code>appadmintargets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.appadmintargets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `verificationStatus` | `string` |
| `displayName` | `string` |
| `features` | `array` |
| `lastUpdated` | `string` |
| `website` | `string` |
| `_links` | `object` |
| `category` | `string` |
| `status` | `string` |
| `signOnModes` | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `roleId, userId` | Lists all App targets for an `APP_ADMIN` Role assigned to a User. This methods return list may include full Applications or Instances. The response for an instance will have an `ID` value, while Application will not have an ID. |
| `insert` | `INSERT` | `appName, applicationId, roleId, userId` | Add App Instance Target to App Administrator Role given to a User |
| `delete` | `DELETE` | `appName, applicationId, roleId, userId` | Remove App Instance Target to App Administrator Role given to a User |
