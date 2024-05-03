---
title: database_migrations_sql_db
hide_title: false
hide_table_of_contents: false
keywords:
  - database_migrations_sql_db
  - data_migration
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
<tr><td><b>Name</b></td><td><code>database_migrations_sql_db</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.database_migrations_sql_db" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Database Migration Resource properties for SQL database. |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlDbInstanceName, subscriptionId, targetDbName" /> | Retrieve the Database Migration resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlDbInstanceName, subscriptionId, targetDbName" /> | Create or Update Database Migration resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlDbInstanceName, subscriptionId, targetDbName" /> | Delete Database Migration resource. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlDbInstanceName, subscriptionId, targetDbName" /> | Stop on going migration for the database. |
