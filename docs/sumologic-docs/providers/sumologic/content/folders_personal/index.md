---
title: folders_personal
hide_title: false
hide_table_of_contents: false
keywords:
  - folders_personal
  - content
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
<tr><td><b>Name</b></td><td><code>folders_personal</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.content.folders_personal</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the content item. |
| `name` | `string` | The name of the content item. |
| `description` | `string` | The description of the folder. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `permissions` | `array` | List of permissions the user has on the content item. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `parentId` | `string` | Identifier of the parent content item. |
| `itemType` | `string` | Type of the content item. Supported values are:<br />  1. Folder<br />  2. Search<br />  3. Report (for old dashboards)<br />  4. Dashboard (for new dashboards)<br />  5. Lookups |
| `children` | `array` | A list of the content items. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getPersonalFolder` | `SELECT` | `region` |
