---
title: custom_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_lists
  - displayvideo
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.custom_lists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the custom list. |
| `customListId` | `string` | Output only. The unique ID of the custom list. Assigned by the system. |
| `displayName` | `string` | Output only. The display name of the custom list. . |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customLists_get` | `SELECT` | `customListsId` | Gets a custom list. |
| `customLists_list` | `SELECT` |  | Lists custom lists. The order is defined by the order_by parameter. |
