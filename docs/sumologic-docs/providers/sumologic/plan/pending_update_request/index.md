---
title: pending_update_request
hide_title: false
hide_table_of_contents: false
keywords:
  - pending_update_request
  - plan
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
<tr><td><b>Name</b></td><td><code>pending_update_request</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.plan.pending_update_request</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `plan` | `object` | Current plan of the account. |
| `createdOn` | `string` | The date on which the update request was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getPendingUpdateRequest` | `SELECT` | `region` | Get the pending plan update request which will be applicable from next billing cycle. |
| `deletePendingUpdateRequest` | `DELETE` | `region` | Delete the pending plan update request which would be applicable from next billing cycle. |
