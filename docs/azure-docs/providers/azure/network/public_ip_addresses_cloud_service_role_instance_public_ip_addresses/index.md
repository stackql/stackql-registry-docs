---
title: public_ip_addresses_cloud_service_role_instance_public_ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - public_ip_addresses_cloud_service_role_instance_public_ip_addresses
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
<tr><td><b>Name</b></td><td><code>public_ip_addresses_cloud_service_role_instance_public_ip_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.public_ip_addresses_cloud_service_role_instance_public_ip_addresses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Public IP address properties. |
| `sku` | `object` | SKU of a public IP address. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `zones` | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `api-version, cloudServiceName, ipConfigurationName, networkInterfaceName, resourceGroupName, roleInstanceName, subscriptionId` |
| `_list` | `EXEC` | `api-version, cloudServiceName, ipConfigurationName, networkInterfaceName, resourceGroupName, roleInstanceName, subscriptionId` |