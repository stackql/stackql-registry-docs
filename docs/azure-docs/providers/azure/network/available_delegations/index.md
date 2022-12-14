---
title: available_delegations
hide_title: false
hide_table_of_contents: false
keywords:
  - available_delegations
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
<tr><td><b>Name</b></td><td><code>available_delegations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.available_delegations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A unique identifier of the AvailableDelegation resource. |
| `name` | `string` | The name of the AvailableDelegation resource. |
| `type` | `string` | Resource type. |
| `actions` | `array` | The actions permitted to the service upon delegation. |
| `serviceName` | `string` | The name of the service and resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AvailableDelegations_List` | `SELECT` | `location, subscriptionId` |
