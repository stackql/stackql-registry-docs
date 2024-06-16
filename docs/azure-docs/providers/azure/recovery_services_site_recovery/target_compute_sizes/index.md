---
title: target_compute_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - target_compute_sizes
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
<tr><td><b>Name</b></td><td><code>target_compute_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.target_compute_sizes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Id. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | Represents applicable recovery vm sizes properties. |
| <CopyableCode code="type" /> | `string` | The Type of the object. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_replication_protected_items" /> | `SELECT` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> |
