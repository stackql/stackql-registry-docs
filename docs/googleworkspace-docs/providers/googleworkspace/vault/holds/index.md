---
title: holds
hide_title: false
hide_table_of_contents: false
keywords:
  - holds
  - vault
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>holds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.vault.holds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the hold. |
| `orgUnit` | `object` | The organizational unit covered by a hold. This structure is immutable. |
| `query` | `object` | Service-specific options for holds. |
| `updateTime` | `string` | The last time this hold was modified. |
| `accounts` | `array` | If set, the hold applies to the specified accounts and **orgUnit** must be empty. |
| `corpus` | `string` | The service to be searched. |
| `holdId` | `string` | The unique immutable ID of the hold. Assigned during creation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `matters_holds_get` | `SELECT` | `holdId, matterId` | Gets the specified hold. |
| `matters_holds_list` | `SELECT` | `matterId` | Lists the holds in a matter. |
| `matters_holds_create` | `INSERT` | `matterId` | Creates a hold in the specified matter. |
| `matters_holds_delete` | `DELETE` | `holdId, matterId` | Removes the specified hold and releases the accounts or organizational unit covered by the hold. If the data is not preserved by another hold or retention rule, it might be purged. |
| `matters_holds_update` | `EXEC` | `holdId, matterId` | Updates the scope (organizational unit or accounts) and query parameters of a hold. You cannot add accounts to a hold that covers an organizational unit, nor can you add organizational units to a hold that covers individual accounts. If you try, the unsupported values are ignored. |
