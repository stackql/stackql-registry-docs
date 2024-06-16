---
title: capacities_details
hide_title: false
hide_table_of_contents: false
keywords:
  - capacities_details
  - powerbi_dedicated
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
<tr><td><b>Name</b></td><td><code>capacities_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_dedicated.capacities_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the PowerBI Dedicated resource. |
| <CopyableCode code="name" /> | `string` | The name of the PowerBI Dedicated resource. |
| <CopyableCode code="location" /> | `string` | Location of the PowerBI Dedicated resource. |
| <CopyableCode code="properties" /> | `object` | Properties of Dedicated Capacity resource. |
| <CopyableCode code="sku" /> | `object` | Represents the SKU name and Azure pricing tier for PowerBI Dedicated capacity resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Key-value pairs of additional resource provisioning properties. |
| <CopyableCode code="type" /> | `string` | The type of the PowerBI Dedicated resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dedicatedCapacityName, resourceGroupName, subscriptionId" /> |
