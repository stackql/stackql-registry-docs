---
title: applinks
hide_title: false
hide_table_of_contents: false
keywords:
  - applinks
  - user
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
<tr><td><b>Name</b></td><td><code>applinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.applinks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `hidden` | `boolean` |
| `sortOrder` | `integer` |
| `appAssignmentId` | `string` |
| `label` | `string` |
| `credentialsSetup` | `boolean` |
| `logoUrl` | `string` |
| `appName` | `string` |
| `linkUrl` | `string` |
| `appInstanceId` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `userId` |
