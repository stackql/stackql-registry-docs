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
| `get` | `SELECT` | `applicationName, clusterName, resourceGroupName, subscriptionId` | Gets properties of the specified application. |
| `list_by_cluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Lists all of the applications for the HDInsight cluster. |
| `create` | `INSERT` | `applicationName, clusterName, resourceGroupName, subscriptionId` | Creates applications for the HDInsight cluster. |
| `delete` | `DELETE` | `applicationName, clusterName, resourceGroupName, subscriptionId` | Deletes the specified application on the HDInsight cluster. |
| `_list_by_cluster` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Lists all of the applications for the HDInsight cluster. |
