---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
  - data_box
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
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_box.service</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `region_configuration` | `EXEC` | `location, subscriptionId` | This API provides configuration details specific to given region/location at Subscription level. |
| `region_configuration_by_resource_group` | `EXEC` | `location, resourceGroupName, subscriptionId` | This API provides configuration details specific to given region/location at Resource group level. |
| `validate_address` | `EXEC` | `location, subscriptionId, data__deviceType, data__shippingAddress, data__validationType` | [DEPRECATED NOTICE: This operation will soon be removed]. This method validates the customer shipping address and provide alternate addresses if any. |
| `validate_inputs` | `EXEC` | `location, subscriptionId, data__individualRequestDetails, data__validationCategory` | This method does all necessary pre-job creation validation under subscription. |
| `validate_inputs_by_resource_group` | `EXEC` | `location, resourceGroupName, subscriptionId, data__individualRequestDetails, data__validationCategory` | This method does all necessary pre-job creation validation under resource group. |
