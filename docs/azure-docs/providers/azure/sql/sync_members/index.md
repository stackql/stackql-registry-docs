---
title: sync_members
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_members
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
<tr><td><b>Name</b></td><td><code>sync_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.sync_members" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName" /> | Gets a sync member. |
| <CopyableCode code="list_by_sync_group" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Lists sync members in the given sync group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName" /> | Creates or updates a sync member. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName" /> | Deletes a sync member. |
| <CopyableCode code="refresh_member_schema" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName" /> | Refreshes a sync member database schema. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName" /> | Updates an existing sync member. |
