---
title: cassandra_clusters_command_async
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_clusters_command_async
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cassandra_clusters_command_async</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.cassandra_clusters_command_async" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="arguments" /> | `object` | The arguments for the command to be run |
| <CopyableCode code="cassandraStopStart" /> | `boolean` | If true, stops cassandra before executing the command and then start it again |
| <CopyableCode code="command" /> | `string` | The command which should be run |
| <CopyableCode code="commandId" /> | `string` | The unique id of command |
| <CopyableCode code="host" /> | `string` | IP address of the cassandra host to run the command on |
| <CopyableCode code="isAdmin" /> | `boolean` | Whether command has admin privileges |
| <CopyableCode code="outputFile" /> | `string` | The name of the file where the result is written. |
| <CopyableCode code="readWrite" /> | `boolean` | If true, allows the command to *write* to the cassandra directory, otherwise read-only. |
| <CopyableCode code="result" /> | `string` | Result output of the command. |
| <CopyableCode code="status" /> | `string` | Status of the command. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, commandId, resourceGroupName, subscriptionId" /> |
