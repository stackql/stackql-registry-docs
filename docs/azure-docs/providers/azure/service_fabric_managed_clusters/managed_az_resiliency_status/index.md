---
title: managed_az_resiliency_status
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_az_resiliency_status
  - service_fabric_managed_clusters
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
<tr><td><b>Name</b></td><td><code>managed_az_resiliency_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_managed_clusters.managed_az_resiliency_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `isClusterZoneResilient` | `boolean` | URL to get the next set of Managed VM Sizes if there are any. |
| `baseResourceStatus` | `array` | List of Managed VM Sizes for Service Fabric Managed Clusters. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `managedAzResiliencyStatus_get` | `SELECT` | `api-version, clusterName, resourceGroupName, subscriptionId` |
