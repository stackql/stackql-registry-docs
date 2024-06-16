---
title: replication_fabrics
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_fabrics
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
<tr><td><b>Name</b></td><td><code>replication_fabrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_fabrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Fabric properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of an Azure Site Recovery fabric. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Gets a list of the Azure Site Recovery fabrics in the vault. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> | The operation to create an Azure Site Recovery fabric (for e.g. Hyper-V site). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> | The operation to delete or remove an Azure Site Recovery fabric. |
| <CopyableCode code="check_consistency" /> | `EXEC` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> | The operation to perform a consistency check on the fabric. |
| <CopyableCode code="migrate_to_aad" /> | `EXEC` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> | The operation to migrate an Azure Site Recovery fabric to AAD. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> | The operation to purge(force delete) an Azure Site Recovery fabric. |
| <CopyableCode code="reassociate_gateway" /> | `EXEC` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> | The operation to move replications from a process server to another process server. |
| <CopyableCode code="remove_infra" /> | `EXEC` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="renew_certificate" /> | `EXEC` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> | Renews the connection certificate for the ASR replication fabric. |
