---
title: location
hide_title: false
hide_table_of_contents: false
keywords:
  - location
  - batch
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
<tr><td><b>Name</b></td><td><code>location</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.batch.location</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Location_CheckNameAvailability` | `EXEC` | `locationName, subscriptionId, data__name, data__type` | Checks whether the Batch account name is available in the specified region. |
| `Location_GetQuotas` | `EXEC` | `locationName, subscriptionId` | Gets the Batch service quotas for the specified subscription at the given location. |
| `Location_ListSupportedCloudServiceSkus` | `EXEC` | `locationName, subscriptionId` | Gets the list of Batch supported Cloud Service VM sizes available at the given location. |
| `Location_ListSupportedVirtualMachineSkus` | `EXEC` | `locationName, subscriptionId` | Gets the list of Batch supported Virtual Machine VM sizes available at the given location. |
