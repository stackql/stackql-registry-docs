---
title: requests
hide_title: false
hide_table_of_contents: false
keywords:
  - requests
  - customer_lockbox
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_lockbox.requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The Arm resource id of the Lockbox request. |
| `name` | `string` | The name of the Lockbox request. |
| `properties` | `object` | The properties that are associated with a lockbox request. |
| `type` | `string` | The type of the Lockbox request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Requests_Get` | `SELECT` | `requestId, subscriptionId` | Get Customer Lockbox request |
| `Requests_List` | `SELECT` | `subscriptionId` | Lists all of the Lockbox requests in the given subscription. |
| `Requests_UpdateStatus` | `EXEC` | `requestId, subscriptionId` | Update Customer Lockbox request approval status API |
