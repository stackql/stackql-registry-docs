---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
  - data_box
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
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_box.service</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Service_ListAvailableSkusByResourceGroup` | `EXEC` | `location, resourceGroupName, subscriptionId, data__country, data__location, data__transferType` | This method provides the list of available skus for the given subscription, resource group and location. |
| `Service_RegionConfiguration` | `EXEC` | `location, subscriptionId` | This API provides configuration details specific to given region/location at Subscription level. |
| `Service_RegionConfigurationByResourceGroup` | `EXEC` | `location, resourceGroupName, subscriptionId` | This API provides configuration details specific to given region/location at Resource group level. |
| `Service_ValidateAddress` | `EXEC` | `location, subscriptionId, data__deviceType, data__shippingAddress, data__validationType` | [DEPRECATED NOTICE: This operation will soon be removed]. This method validates the customer shipping address and provide alternate addresses if any. |
| `Service_ValidateInputs` | `EXEC` | `location, subscriptionId, data__individualRequestDetails, data__validationCategory` | This method does all necessary pre-job creation validation under subscription. |
| `Service_ValidateInputsByResourceGroup` | `EXEC` | `location, resourceGroupName, subscriptionId, data__individualRequestDetails, data__validationCategory` | This method does all necessary pre-job creation validation under resource group. |
