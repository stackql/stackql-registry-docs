---
title: exposure_control
hide_title: false
hide_table_of_contents: false
keywords:
  - exposure_control
  - data_factory
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
<tr><td><b>Name</b></td><td><code>exposure_control</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.exposure_control</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExposureControl_GetFeatureValue` | `EXEC` | `api-version, locationId, subscriptionId` | Get exposure control feature for specific location. |
| `ExposureControl_GetFeatureValueByFactory` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Get exposure control feature for specific factory. |
| `ExposureControl_QueryFeatureValuesByFactory` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, data__exposureControlRequests` | Get list of exposure control features for specific factory. |
