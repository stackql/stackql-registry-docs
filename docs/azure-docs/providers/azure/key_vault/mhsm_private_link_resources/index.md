---
title: mhsm_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - mhsm_private_link_resources
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
<tr><td><b>Name</b></td><td><code>mhsm_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.mhsm_private_link_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Azure Resource Manager resource ID for the managed HSM Pool. |
| <CopyableCode code="name" /> | `string` | The name of the managed HSM Pool. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The supported Azure location where the managed HSM Pool should be created. |
| <CopyableCode code="properties" /> | `object` | Properties of a private link resource. |
| <CopyableCode code="sku" /> | `object` | SKU details |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the key vault resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | The resource type of the managed HSM Pool. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_mhsm_resource" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> |
