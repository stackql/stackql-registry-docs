---
title: database_migrations_sql_mi
hide_title: false
hide_table_of_contents: false
keywords:
  - database_migrations_sql_mi
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
<tr><td><b>Name</b></td><td><code>database_migrations_sql_mi</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.database_migrations_sql_mi" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Database Migration Resource properties for SQL Managed Instance. |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId, targetDbName" /> | Retrieve the specified database migration for a given SQL Managed Instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId, targetDbName" /> | Create a new database migration to a given SQL Managed Instance. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId, targetDbName" /> | Stop in-progress database migration to SQL Managed Instance. |
| <CopyableCode code="cutover" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId, targetDbName" /> | Initiate cutover for in-progress online database migration to SQL Managed Instance. |
