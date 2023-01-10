---
title: export_result
hide_title: false
hide_table_of_contents: false
keywords:
  - export_result
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
<tr><td><b>Name</b></td><td><code>export_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.content.export_result</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the item. |
| `type` | `string` | The content item type.<br />**Note:**<br /> - `MewboardSyncDefinition` _is depreciated, and will soon be removed. Please use_ `DashboardV2SyncDefinition`<br />   _instead_.<br /> - Dashboard links are not supported for dashboards. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getAsyncExportResult` | `SELECT` | `contentId, jobId` |
