---
title: folders_global_result
hide_title: false
hide_table_of_contents: false
keywords:
  - folders_global_result
  - content
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>folders_global_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.content.folders_global_result</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the content item. |
| `name` | `string` | The name of the content item. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `permissions` | `array` | List of permissions the user has on the content item. |
| `itemType` | `string` | Type of the content item. Supported values are:<br />  1. Folder<br />  2. Search<br />  3. Report (for old dashboards)<br />  4. Dashboard (for new dashboards)<br />  5. Lookups |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `parentId` | `string` | Identifier of the parent content item. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getGlobalFolderAsyncResult` | `SELECT` | `jobId` |
