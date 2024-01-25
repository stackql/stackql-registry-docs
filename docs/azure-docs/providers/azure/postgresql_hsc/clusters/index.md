---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - postgresql_hsc
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
<tr><td><b>Id</b></td><td><code>azure.postgresql_hsc.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the cluster. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets information about a cluster such as compute and storage configuration and cluster lifecycle metadata such as cluster creation date and time. |
| `list` | `SELECT` | `subscriptionId` | Lists all clusters in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all clusters in a resource group. |
| `create` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Creates a new cluster with servers. |
| `delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes a cluster together with servers in it. |
| `_list` | `EXEC` | `subscriptionId` | Lists all clusters in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all clusters in a resource group. |
| `check_name_availability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks availability of a cluster name. Cluster names should be globally unique; at least 3 characters and at most 40 characters long; they must only contain lowercase letters, numbers, and hyphens; and must not start or end with a hyphen. |
| `promote_read_replica` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Promotes read replica cluster to an independent read-write cluster. |
| `restart` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Restarts all nodes in the cluster. |
| `start` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Starts stopped compute on all cluster nodes. |
| `stop` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Stops compute on all cluster nodes. |
| `update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Updates an existing cluster. The request body can contain one or several properties from the cluster definition. |
