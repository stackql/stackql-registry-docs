---
title: location_capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - location_capabilities
  - container_instances
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
<tr><td><b>Name</b></td><td><code>location_capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_instances.location_capabilities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `capabilities` | `object` | The supported capabilities. |
| `gpu` | `string` | The GPU sku that this capability describes. |
| `ipAddressType` | `string` | The ip address type that this capability describes. |
| `location` | `string` | The resource location. |
| `osType` | `string` | The OS type that this capability describes. |
| `resourceType` | `string` | The resource type that this capability describes. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `location, subscriptionId` |
| `_list` | `EXEC` | `location, subscriptionId` |
