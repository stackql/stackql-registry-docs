---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hdinsight.applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | The ETag for the application |
| `properties` | `object` | The HDInsight cluster application GET response. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | The tags for the application. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Applications_Get` | `SELECT` | `applicationName, clusterName, resourceGroupName, subscriptionId` | Gets properties of the specified application. |
| `Applications_ListByCluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Lists all of the applications for the HDInsight cluster. |
| `Applications_Create` | `INSERT` | `applicationName, clusterName, resourceGroupName, subscriptionId` | Creates applications for the HDInsight cluster. |
| `Applications_Delete` | `DELETE` | `applicationName, clusterName, resourceGroupName, subscriptionId` | Deletes the specified application on the HDInsight cluster. |
| `Applications_GetAzureAsyncOperationStatus` | `EXEC` | `applicationName, clusterName, operationId, resourceGroupName, subscriptionId` | Gets the async operation status. |
