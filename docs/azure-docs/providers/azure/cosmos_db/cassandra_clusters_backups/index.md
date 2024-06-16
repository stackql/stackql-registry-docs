---
title: cassandra_clusters_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_clusters_backups
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
<tr><td><b>Name</b></td><td><code>cassandra_clusters_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.cassandra_clusters_backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="backupExpiryTimestamp" /> | `string` | The time at which the backup will expire. |
| <CopyableCode code="backupId" /> | `string` | The unique identifier of backup. |
| <CopyableCode code="backupStartTimestamp" /> | `string` | The time at which the backup process begins. |
| <CopyableCode code="backupState" /> | `string` | The current state of the backup. |
| <CopyableCode code="backupStopTimestamp" /> | `string` | The time at which the backup process ends. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupId, clusterName, resourceGroupName, subscriptionId" /> | Get the properties of an individual backup of this cluster that is available to restore. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List the backups of this cluster that are available to restore. |
