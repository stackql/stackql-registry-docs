---
title: workspace_managed_sql_server_extended_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_extended_blob_auditing_policies
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
<tr><td><b>Name</b></td><td><code>workspace_managed_sql_server_extended_blob_auditing_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.workspace_managed_sql_server_extended_blob_auditing_policies" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="blobAuditingPolicyName, resourceGroupName, subscriptionId, workspaceName" /> | Get a workspace SQL server's extended blob auditing policy. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List workspace managed sql server's extended blob auditing policies. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="blobAuditingPolicyName, resourceGroupName, subscriptionId, workspaceName" /> | Create or Update a workspace managed sql server's extended blob auditing policy. |
| <CopyableCode code="_list_by_workspace" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List workspace managed sql server's extended blob auditing policies. |
