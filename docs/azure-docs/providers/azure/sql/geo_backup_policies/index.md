---
title: geo_backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - geo_backup_policies
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
<tr><td><b>Name</b></td><td><code>geo_backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.geo_backup_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of geo backup policy.  This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `string` | Backup policy location. |
| <CopyableCode code="properties" /> | `object` | The properties of the geo backup policy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, geoBackupPolicyName, resourceGroupName, serverName, subscriptionId" /> | Gets a geo backup policy. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Returns a list of geo backup policies. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, geoBackupPolicyName, resourceGroupName, serverName, subscriptionId, data__properties" /> | Updates a database geo backup policy. |
