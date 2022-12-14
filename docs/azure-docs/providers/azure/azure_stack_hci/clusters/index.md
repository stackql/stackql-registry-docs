---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - azure_stack_hci
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_stack_hci.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Cluster properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Clusters_Get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Get HCI cluster. |
| `Clusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all HCI clusters in a resource group. |
| `Clusters_ListBySubscription` | `SELECT` | `subscriptionId` | List all HCI clusters in a subscription. |
| `Clusters_Create` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Create an HCI cluster. |
| `Clusters_Delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Delete an HCI cluster. |
| `Clusters_CreateIdentity` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Create cluster identity. |
| `Clusters_ExtendSoftwareAssuranceBenefit` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Extends Software Assurance Benefit to a cluster |
| `Clusters_Update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Update an HCI cluster. |
| `Clusters_UploadCertificate` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Upload certificate. |
