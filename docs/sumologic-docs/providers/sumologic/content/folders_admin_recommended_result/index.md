---
title: folders_admin_recommended_result
hide_title: false
hide_table_of_contents: false
keywords:
  - folders_admin_recommended_result
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
<tr><td><b>Name</b></td><td><code>folders_admin_recommended_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.content.folders_admin_recommended_result</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the content item. |
| `name` | `string` | The name of the content item. |
| `description` | `string` | The description of the folder. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `permissions` | `array` | List of permissions the user has on the content item. |
| `children` | `array` | A list of the content items. |
| `parentId` | `string` | Identifier of the parent content item. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `itemType` | `string` | Type of the content item. Supported values are:<br />  1. Folder<br />  2. Search<br />  3. Report (for old dashboards)<br />  4. Dashboard (for new dashboards)<br />  5. Lookups |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getAdminRecommendedFolderAsyncResult` | `SELECT` | `jobId, region` |
