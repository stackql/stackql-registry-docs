---
title: sync_members_member_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_members_member_schemas
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
<tr><td><b>Name</b></td><td><code>sync_members_member_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.sync_members_member_schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="lastUpdateTime" /> | `string` | Last update time of the database schema. |
| <CopyableCode code="tables" /> | `array` | List of tables in the database full schema. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName" /> |
