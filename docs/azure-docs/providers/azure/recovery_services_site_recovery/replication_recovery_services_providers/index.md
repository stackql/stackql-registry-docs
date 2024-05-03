---
title: replication_recovery_services_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_recovery_services_providers
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_recovery_services_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_recovery_services_providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Recovery services provider properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of registered recovery services provider. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Lists the registered recovery services providers in the vault. |
| <CopyableCode code="list_by_replication_fabrics" /> | `SELECT` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> | Lists the registered recovery services providers for the specified fabric. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to add a recovery services provider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to removes/delete(unregister) a recovery services provider from the vault. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Lists the registered recovery services providers in the vault. |
| <CopyableCode code="_list_by_replication_fabrics" /> | `EXEC` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> | Lists the registered recovery services providers for the specified fabric. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to purge(force delete) a recovery services provider from the vault. |
| <CopyableCode code="refresh_provider" /> | `EXEC` | <CopyableCode code="api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to refresh the information from the recovery services provider. |
