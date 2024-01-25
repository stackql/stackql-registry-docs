---
title: extensions_monitoring_status
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions_monitoring_status
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
<tr><td><b>Name</b></td><td><code>extensions_monitoring_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hdinsight.extensions_monitoring_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `clusterMonitoringEnabled` | `boolean` | The status of the monitor on the HDInsight cluster. |
| `workspaceId` | `string` | The workspace ID of the monitor on the HDInsight cluster. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` |
