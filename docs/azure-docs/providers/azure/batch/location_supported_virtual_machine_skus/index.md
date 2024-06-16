---
title: location_supported_virtual_machine_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - location_supported_virtual_machine_skus
  - batch
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
<tr><td><b>Name</b></td><td><code>location_supported_virtual_machine_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.location_supported_virtual_machine_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the SKU. |
| <CopyableCode code="batchSupportEndOfLife" /> | `string` | The time when Azure Batch service will retire this SKU. |
| <CopyableCode code="capabilities" /> | `array` | A collection of capabilities which this SKU supports. |
| <CopyableCode code="familyName" /> | `string` | The family name of the SKU. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> |
