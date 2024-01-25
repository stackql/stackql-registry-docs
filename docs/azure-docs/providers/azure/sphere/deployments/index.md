---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - sphere
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
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sphere.deployments</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `catalogName, deploymentName, deviceGroupName, productName, resourceGroupName, subscriptionId` | Get a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| `list_by_device_group` | `SELECT` | `catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId` | List Deployment resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| `create_or_update` | `INSERT` | `catalogName, deploymentName, deviceGroupName, productName, resourceGroupName, subscriptionId` | Create a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| `delete` | `DELETE` | `catalogName, deploymentName, deviceGroupName, productName, resourceGroupName, subscriptionId` | Delete a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| `_list_by_device_group` | `EXEC` | `catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId` | List Deployment resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
