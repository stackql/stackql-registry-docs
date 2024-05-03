---
title: inference_groups_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_groups_skus
  - ml_services
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
<tr><td><b>Name</b></td><td><code>inference_groups_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.inference_groups_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `object` | SKU capacity information |
| <CopyableCode code="resourceType" /> | `string` | The resource type name. |
| <CopyableCode code="sku" /> | `object` | SkuSetting fulfills the need for stripped down SKU info in ARM contract. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupName, poolName, resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="groupName, poolName, resourceGroupName, subscriptionId, workspaceName" /> |
