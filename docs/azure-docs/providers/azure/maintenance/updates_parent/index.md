---
title: updates_parent
hide_title: false
hide_table_of_contents: false
keywords:
  - updates_parent
  - maintenance
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
<tr><td><b>Name</b></td><td><code>updates_parent</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maintenance.updates_parent" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="impactDurationInSec" /> | `integer` | Duration of impact in seconds |
| <CopyableCode code="impactType" /> | `string` | The impact type |
| <CopyableCode code="maintenanceScope" /> | `string` | The impact area |
| <CopyableCode code="notBefore" /> | `string` | Time when Azure will start force updates if not self-updated by customer before this time |
| <CopyableCode code="properties" /> | `object` | Properties for update |
| <CopyableCode code="status" /> | `string` | The status |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId" /> |
