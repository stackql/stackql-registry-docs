---
title: folders_global_status
hide_title: false
hide_table_of_contents: false
keywords:
  - folders_global_status
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
<tr><td><b>Name</b></td><td><code>folders_global_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.content.folders_global_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `status` | `string` | Whether or not the request is in progress (`InProgress`), has completed successfully (`Success`), or has completed with an error (`Failed`). |
| `statusMessage` | `string` | Additional status message generated if the status is not `Failed`. |
| `error` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getGlobalFolderAsyncStatus` | `SELECT` | `jobId, region` |
