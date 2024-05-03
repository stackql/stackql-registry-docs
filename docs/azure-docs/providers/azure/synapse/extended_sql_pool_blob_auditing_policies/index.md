---
title: extended_sql_pool_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - extended_sql_pool_blob_auditing_policies
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
<tr><td><b>Name</b></td><td><code>extended_sql_pool_blob_auditing_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.extended_sql_pool_blob_auditing_policies" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="blobAuditingPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Gets an extended Sql pool's blob auditing policy. |
| <CopyableCode code="list_by_sql_pool" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Lists extended auditing settings of a Sql pool. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="blobAuditingPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Creates or updates an extended Sql pool's blob auditing policy. |
| <CopyableCode code="_list_by_sql_pool" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Lists extended auditing settings of a Sql pool. |
