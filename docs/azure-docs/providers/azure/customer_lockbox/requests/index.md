---
title: requests
hide_title: false
hide_table_of_contents: false
keywords:
  - requests
  - customer_lockbox
  - azure    
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
<tr><td><b>Id</b></td><td><code>azure.customer_lockbox.requests</code></td></tr>
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
| `get` | `SELECT` | `requestId, subscriptionId` | Get Customer Lockbox request |
| `list` | `SELECT` | `subscriptionId` | Lists all of the Lockbox requests in the given subscription. |
| `_list` | `EXEC` | `subscriptionId` | Lists all of the Lockbox requests in the given subscription. |
