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
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `zones` | `array` | The availability zones. |
| `etag` | `string` | The ETag for the resource |
| `identity` | `object` | Identity for the cluster. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Clusters_Get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets the specified cluster. |
| `Clusters_List` | `SELECT` | `subscriptionId` | Lists all the HDInsight clusters under the subscription. |
| `Clusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the HDInsight clusters in a resource group. |
| `Clusters_Create` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Creates a new HDInsight cluster with the specified parameters. |
| `Clusters_Delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes the specified HDInsight cluster. |
| `Clusters_ExecuteScriptActions` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, data__persistOnSuccess` | Executes script actions on the specified HDInsight cluster. |
| `Clusters_GetAzureAsyncOperationStatus` | `EXEC` | `clusterName, operationId, resourceGroupName, subscriptionId` | The the async operation status. |
| `Clusters_GetGatewaySettings` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Gets the gateway settings for the specified cluster. |
| `Clusters_Resize` | `EXEC` | `clusterName, resourceGroupName, roleName, subscriptionId` | Resizes the specified HDInsight cluster to the specified size. |
| `Clusters_RotateDiskEncryptionKey` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Rotate disk encryption key of the specified HDInsight cluster. |
| `Clusters_Update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Patch HDInsight cluster with the specified parameters. |
| `Clusters_UpdateAutoScaleConfiguration` | `EXEC` | `clusterName, resourceGroupName, roleName, subscriptionId` | Updates the Autoscale Configuration for HDInsight cluster. |
| `Clusters_UpdateGatewaySettings` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Configures the gateway settings on the specified cluster. |
| `Clusters_UpdateIdentityCertificate` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Updates the cluster identity certificate. |
