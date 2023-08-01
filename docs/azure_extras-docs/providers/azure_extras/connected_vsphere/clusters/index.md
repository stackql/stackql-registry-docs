---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - connected_vsphere
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.connected_vsphere.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id. |
| `name` | `string` | Gets or sets the name. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Gets or sets the Resource tags. |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| `location` | `string` | Gets or sets the location. |
| `extendedLocation` | `object` | The extended location. |
| `properties` | `object` | Defines the resource properties. |
| `type` | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Clusters_Get` | `SELECT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Implements cluster GET method. |
| `Clusters_List` | `SELECT` | `api-version, subscriptionId` | List of clusters in a subscription. |
| `Clusters_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List of clusters in a resource group. |
| `Clusters_Create` | `INSERT` | `api-version, clusterName, resourceGroupName, subscriptionId, data__location, data__properties` | Create Or Update cluster. |
| `Clusters_Delete` | `DELETE` | `api-version, clusterName, resourceGroupName, subscriptionId` | Implements cluster DELETE method. |
| `Clusters_Update` | `EXEC` | `api-version, clusterName, resourceGroupName, subscriptionId` | API to update certain properties of the cluster resource. |
