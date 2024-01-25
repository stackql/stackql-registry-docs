---
title: network_service_design_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_service_design_versions
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>network_service_design_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.network_service_design_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | network service design version properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkServiceDesignGroupName, networkServiceDesignVersionName, publisherName, resourceGroupName, subscriptionId` | Gets information about a network service design version. |
| `list_by_network_service_design_group` | `SELECT` | `networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId` | Gets information about a list of network service design versions under a network service design group. |
| `create_or_update` | `INSERT` | `networkServiceDesignGroupName, networkServiceDesignVersionName, publisherName, resourceGroupName, subscriptionId` | Creates or updates a network service design version. |
| `delete` | `DELETE` | `networkServiceDesignGroupName, networkServiceDesignVersionName, publisherName, resourceGroupName, subscriptionId` | Deletes the specified network service design version. |
| `_list_by_network_service_design_group` | `EXEC` | `networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId` | Gets information about a list of network service design versions under a network service design group. |
| `update` | `EXEC` | `networkServiceDesignGroupName, networkServiceDesignVersionName, publisherName, resourceGroupName, subscriptionId` | Updates a network service design version resource. |
