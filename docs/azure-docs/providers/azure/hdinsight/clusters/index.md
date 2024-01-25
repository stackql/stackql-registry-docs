---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - hdinsight
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
<tr><td><b>Id</b></td><td><code>azure.hdinsight.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | The ETag for the resource |
| `identity` | `object` | Identity for the cluster. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of cluster. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `zones` | `array` | The availability zones. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets the specified cluster. |
| `list` | `SELECT` | `subscriptionId` | Lists all the HDInsight clusters under the subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the HDInsight clusters in a resource group. |
| `create` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Creates a new HDInsight cluster with the specified parameters. |
| `delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes the specified HDInsight cluster. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the HDInsight clusters under the subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists the HDInsight clusters in a resource group. |
| `execute_script_actions` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, data__persistOnSuccess` | Executes script actions on the specified HDInsight cluster. |
| `resize` | `EXEC` | `clusterName, resourceGroupName, roleName, subscriptionId` | Resizes the specified HDInsight cluster to the specified size. |
| `rotate_disk_encryption_key` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Rotate disk encryption key of the specified HDInsight cluster. |
| `update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Patch HDInsight cluster with the specified parameters. |
