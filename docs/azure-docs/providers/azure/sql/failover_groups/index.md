---
title: failover_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - failover_groups
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
<tr><td><b>Name</b></td><td><code>failover_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.failover_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of a failover group. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Gets a failover group. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Lists the failover groups in a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a failover group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Deletes a failover group. |
| <CopyableCode code="_list_by_server" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Lists the failover groups in a server. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Fails over from the current primary server to this server. |
| <CopyableCode code="force_failover_allow_data_loss" /> | `EXEC` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Fails over from the current primary server to this server. This operation might result in data loss. |
| <CopyableCode code="try_planned_before_forced_failover" /> | `EXEC` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Fails over from the current primary server to this server. This operation tries planned before forced failover but might still result in data loss. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Updates a failover group. |
