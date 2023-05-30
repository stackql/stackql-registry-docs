---
title: root
hide_title: false
hide_table_of_contents: false
keywords:
  - root
  - monitors
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>root</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.monitors.root</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the monitor or folder. |
| `name` | `string` | Identifier of the monitor or folder. |
| `description` | `string` | Description of the monitor or folder. |
| `version` | `integer` | Version of the monitor or folder. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `children` | `array` | Children of the folder. NOTE: Permissions field will not be filled (empty list) for children. |
| `contentType` | `string` | Type of the content. Valid values:<br />  1) Monitor<br />  2) Folder |
| `parentId` | `string` | Identifier of the parent folder. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `permissions` | `array` | Aggregated permission summary for the calling user. If detailed permission statements are required, please call list permissions endpoint. |
| `_permissions` | `array` | Aggregated permission summary for the calling user. If detailed permission statements are required, please call list permissions endpoint. |
| `isSystem` | `boolean` | System objects are objects provided by Sumo Logic. System objects can only be localized. Non-local fields can't be updated. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `type` | `string` | Type of the object model. |
| `isMutable` | `boolean` | Immutable objects are "READ-ONLY". |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getMonitorsLibraryRoot` | `SELECT` | `region` |
