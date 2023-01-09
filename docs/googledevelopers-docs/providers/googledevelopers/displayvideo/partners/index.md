---
title: partners
hide_title: false
hide_table_of_contents: false
keywords:
  - partners
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
<tr><td><b>Name</b></td><td><code>partners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.partners</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the partner. |
| `adServerConfig` | `object` | Ad server related settings of a partner. |
| `dataAccessConfig` | `object` | Settings that control how partner related data may be accessed. |
| `partnerId` | `string` | Output only. The unique ID of the partner. Assigned by the system. |
| `updateTime` | `string` | Output only. The timestamp when the partner was last updated. Assigned by the system. |
| `entityStatus` | `string` | Output only. The status of the partner. |
| `displayName` | `string` | The display name of the partner. Must be UTF-8 encoded with a maximum size of 240 bytes. |
| `exchangeConfig` | `object` | Settings that control which exchanges are enabled for a partner. |
| `generalConfig` | `object` | General settings of a partner. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `partnersId` | Gets a partner. |
| `list` | `SELECT` |  | Lists partners that are accessible to the current user. The order is defined by the order_by parameter. |
| `editAssignedTargetingOptions` | `EXEC` | `partnersId` | Edits targeting options under a single partner. The operation will delete the assigned targeting options provided in BulkEditPartnerAssignedTargetingOptionsRequest.deleteRequests and then create the assigned targeting options provided in BulkEditPartnerAssignedTargetingOptionsRequest.createRequests . |
