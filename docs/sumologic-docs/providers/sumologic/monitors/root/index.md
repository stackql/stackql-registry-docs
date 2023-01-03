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
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `isSystem` | `boolean` | System objects are objects provided by Sumo Logic. System objects can only be localized. Non-local fields can't be updated. |
| `contentType` | `string` | Type of the content. Valid values:<br />  1) Monitor<br />  2) Folder |
| `version` | `integer` | Version of the monitor or folder. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `type` | `string` | Type of the object model. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `permissions` | `array` | Aggregated permission summary for the calling user. If detailed permission statements are required, please call list permissions endpoint. |
| `children` | `array` | Children of the folder. NOTE: Permissions field will not be filled (empty list) for children. |
| `parentId` | `string` | Identifier of the parent folder. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `_permissions` | `array` | Aggregated permission summary for the calling user. If detailed permission statements are required, please call list permissions endpoint. |
| `isMutable` | `boolean` | Immutable objects are "READ-ONLY". |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getMonitorsLibraryRoot` | `SELECT` |  |
