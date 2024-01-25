---
title: cassandra_clusters_command
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_clusters_command
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>cassandra_clusters_command</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.cassandra_clusters_command</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `arguments` | `object` | The arguments for the command to be run |
| `cassandraStopStart` | `boolean` | If true, stops cassandra before executing the command and then start it again |
| `command` | `string` | The command which should be run |
| `commandId` | `string` | The unique id of command |
| `host` | `string` | IP address of the cassandra host to run the command on |
| `isAdmin` | `boolean` | Whether command has admin privileges |
| `outputFile` | `string` | The name of the file where the result is written. |
| `readWrite` | `boolean` | If true, allows the command to *write* to the cassandra directory, otherwise read-only. |
| `result` | `string` | Result output of the command. |
| `status` | `string` | Status of the command. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` |
