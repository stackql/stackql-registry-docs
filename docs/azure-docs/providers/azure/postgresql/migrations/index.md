---
title: migrations
hide_title: false
hide_table_of_contents: false
keywords:
  - migrations
  - postgresql
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
<tr><td><b>Name</b></td><td><code>migrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql.migrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Migration resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetDbServerName" /> | Gets details of a migration. |
| <CopyableCode code="list_by_target_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, targetDbServerName" /> | List all the migrations on a given target server. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetDbServerName" /> | Creates a new migration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetDbServerName" /> | Deletes a migration. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetDbServerName" /> | Updates an existing migration. The request body can contain one to many of the mutable properties present in the migration definition. Certain property updates initiate migration state transitions. |
