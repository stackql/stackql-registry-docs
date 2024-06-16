---
title: replication_links
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_links
  - sql
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
<tr><td><b>Name</b></td><td><code>replication_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.replication_links" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, linkId, resourceGroupName, serverName, subscriptionId" /> | Gets a replication link. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of replication links on database. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of replication links. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, linkId, resourceGroupName, serverName, subscriptionId" /> | Updates the replication link type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, linkId, resourceGroupName, serverName, subscriptionId" /> | Deletes the replication link. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="databaseName, linkId, resourceGroupName, serverName, subscriptionId" /> | Fails over from the current primary server to this server. |
| <CopyableCode code="failover_allow_data_loss" /> | `EXEC` | <CopyableCode code="databaseName, linkId, resourceGroupName, serverName, subscriptionId" /> | Fails over from the current primary server to this server allowing data loss. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="databaseName, linkId, resourceGroupName, serverName, subscriptionId" /> | Updates the replication link type. |
