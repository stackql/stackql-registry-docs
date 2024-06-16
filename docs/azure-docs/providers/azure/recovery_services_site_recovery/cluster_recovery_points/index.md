---
title: cluster_recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_recovery_points
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
<tr><td><b>Name</b></td><td><code>cluster_recovery_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.cluster_recovery_points" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The recovery point Id. |
| <CopyableCode code="name" /> | `string` | The name of the recovery point. |
| <CopyableCode code="properties" /> | `object` | Cluster recovery point properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_replication_protection_cluster" /> | `SELECT` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> |
