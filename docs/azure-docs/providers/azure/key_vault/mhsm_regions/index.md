---
title: mhsm_regions
hide_title: false
hide_table_of_contents: false
keywords:
  - mhsm_regions
  - key_vault
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
<tr><td><b>Name</b></td><td><code>mhsm_regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.mhsm_regions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the geo replicated region. |
| <CopyableCode code="isPrimary" /> | `boolean` | A boolean value that indicates whether the region is the primary region or a secondary region. |
| <CopyableCode code="provisioningState" /> | `string` | The current provisioning state. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_resource" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list_by_resource" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> |
