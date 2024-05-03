---
title: disk_pool_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_pool_zones
  - storage_pool
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
<tr><td><b>Name</b></td><td><code>disk_pool_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_pool.disk_pool_zones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="additionalCapabilities" /> | `array` | List of additional capabilities for Disk Pool. |
| <CopyableCode code="availabilityZones" /> | `array` | Logical zone for Disk Pool resource; example: ["1"]. |
| <CopyableCode code="sku" /> | `object` | Sku for ARM resource |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> |
