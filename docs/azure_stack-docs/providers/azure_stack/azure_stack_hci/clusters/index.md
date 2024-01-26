---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - azure_stack_hci
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack_hci.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Cluster properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Get HCI cluster. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all HCI clusters in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all HCI clusters in a subscription. |
| `create` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Create an HCI cluster. |
| `delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Delete an HCI cluster. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all HCI clusters in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all HCI clusters in a subscription. |
| `extend_software_assurance_benefit` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Extends Software Assurance Benefit to a cluster |
| `update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Update an HCI cluster. |
| `upload_certificate` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Upload certificate. |
