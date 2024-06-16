---
title: hybrid_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_connections
  - relay
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
<tr><td><b>Name</b></td><td><code>hybrid_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.relay.hybrid_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `` | Properties of the HybridConnection. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hybridConnectionName, namespaceName, resourceGroupName, subscriptionId" /> | Returns the description for the specified hybrid connection. |
| <CopyableCode code="list_by_namespace" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Lists the hybrid connection within the namespace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hybridConnectionName, namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates a service hybrid connection. This operation is idempotent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hybridConnectionName, namespaceName, resourceGroupName, subscriptionId" /> | Deletes a hybrid connection. |
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="authorizationRuleName, hybridConnectionName, namespaceName, resourceGroupName, subscriptionId, data__keyType" /> | Regenerates the primary or secondary connection strings to the hybrid connection. |
