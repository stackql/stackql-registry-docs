---
title: location_capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - location_capabilities
  - container_instances
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
<tr><td><b>Name</b></td><td><code>location_capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_instances.location_capabilities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capabilities" /> | `object` | The supported capabilities. |
| <CopyableCode code="gpu" /> | `string` | The GPU sku that this capability describes. |
| <CopyableCode code="ipAddressType" /> | `string` | The ip address type that this capability describes. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="osType" /> | `string` | The OS type that this capability describes. |
| <CopyableCode code="resourceType" /> | `string` | The resource type that this capability describes. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> |
