---
title: sql_pool_geo_backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_geo_backup_policies
  - synapse
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
<tr><td><b>Name</b></td><td><code>sql_pool_geo_backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_geo_backup_policies" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="geoBackupPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get the specified SQL pool geo backup policy |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get list of SQL pool geo backup policies |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="geoBackupPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName, data__properties" /> | Updates a SQL Pool geo backup policy. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get list of SQL pool geo backup policies |
