---
title: iot_dps_resource_operation_result
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_dps_resource_operation_result
  - iot_hub_device_provisioning
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
<tr><td><b>Name</b></td><td><code>iot_dps_resource_operation_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub_device_provisioning.iot_dps_resource_operation_result</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `error` | `object` | Error response containing message and code. |
| `status` | `string` | current status of a long running operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version, asyncinfo, operationId, provisioningServiceName, resourceGroupName, subscriptionId` |
