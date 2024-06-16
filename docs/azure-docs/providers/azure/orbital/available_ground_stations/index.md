---
title: available_ground_stations
hide_title: false
hide_table_of_contents: false
keywords:
  - available_ground_stations
  - orbital
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
<tr><td><b>Name</b></td><td><code>available_ground_stations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.orbital.available_ground_stations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of groundStation. |
| <CopyableCode code="name" /> | `string` | Name of the ground station. |
| <CopyableCode code="location" /> | `string` | Azure region. |
| <CopyableCode code="properties" /> | `object` | The properties bag for this resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_capability" /> | `SELECT` | <CopyableCode code="capability, subscriptionId" /> |
