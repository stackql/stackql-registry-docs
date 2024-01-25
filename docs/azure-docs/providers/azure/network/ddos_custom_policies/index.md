---
title: ddos_custom_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - ddos_custom_policies
  - network
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
<tr><td><b>Name</b></td><td><code>ddos_custom_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.ddos_custom_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | DDoS custom policy properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `ddosCustomPolicyName, resourceGroupName, subscriptionId` | Gets information about the specified DDoS custom policy. |
| `create_or_update` | `INSERT` | `ddosCustomPolicyName, resourceGroupName, subscriptionId` | Creates or updates a DDoS custom policy. |
| `delete` | `DELETE` | `ddosCustomPolicyName, resourceGroupName, subscriptionId` | Deletes the specified DDoS custom policy. |
