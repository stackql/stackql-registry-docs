---
title: replication_protection_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_clusters
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
<tr><td><b>Name</b></td><td><code>replication_protection_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protection_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The protection cluster Id. |
| <CopyableCode code="name" /> | `string` | The name of the protection cluster. |
| <CopyableCode code="properties" /> | `object` | Replication protection cluster custom data details. |
| <CopyableCode code="type" /> | `string` | The Type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of an ASR replication protection cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR replication protected clusters in the vault. |
| <CopyableCode code="list_by_replication_protection_containers" /> | `SELECT` | <CopyableCode code="api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR replication protected clusters in the protection container. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> | The operation to create an ASR replication protection cluster item. |
| <CopyableCode code="apply_recovery_point" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to apply a new cluster recovery point on the Protection cluster. |
| <CopyableCode code="failover_commit" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> | Operation to initiate commit failover of the replication protection cluster. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> | The operation to purge the replication protection cluster. This operation will force delete the replication protection cluster. Use the remove operation on replication protection cluster to perform a clean disable replication protection cluster. |
| <CopyableCode code="repair_replication" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> | The operation to repair replication protection cluster. |
| <CopyableCode code="test_failover" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to initiate a failover of the replication protection cluster. |
| <CopyableCode code="test_failover_cleanup" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to clean up the test failover of a replication protected cluster. |
| <CopyableCode code="unplanned_failover" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to initiate a failover of the replication protection cluster. |
