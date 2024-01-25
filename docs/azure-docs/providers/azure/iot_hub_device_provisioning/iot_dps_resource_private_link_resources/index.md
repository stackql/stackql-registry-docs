---
title: iot_dps_resource_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_dps_resource_private_link_resources
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
<tr><td><b>Name</b></td><td><code>iot_dps_resource_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub_device_provisioning.iot_dps_resource_private_link_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | The properties for a group information object |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, groupId, resourceGroupName, resourceName, subscriptionId` | Get the specified private link resource for the given provisioning service |
| `list` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | List private link resources for the given provisioning service |
| `_list` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | List private link resources for the given provisioning service |
