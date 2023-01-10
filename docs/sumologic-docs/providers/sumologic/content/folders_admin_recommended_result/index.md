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
| `description` | `string` | The description of the folder. |
| `children` | `array` | A list of the content items. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getAdminRecommendedFolderAsyncResult` | `SELECT` | `jobId` |
