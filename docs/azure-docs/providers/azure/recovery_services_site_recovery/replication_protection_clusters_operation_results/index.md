---
title: replication_protection_clusters_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_clusters_operation_results
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
<tr><td><b>Name</b></td><td><code>replication_protection_clusters_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protection_clusters_operation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The protection cluster Id. |
| <CopyableCode code="name" /> | `string` | The name of the protection cluster. |
| <CopyableCode code="properties" /> | `object` | Replication protection cluster custom data details. |
| <CopyableCode code="type" /> | `string` | The Type of the object. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, fabricName, jobId, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> |
