---
title: reservation_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_revisions
  - reservations
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
<tr><td><b>Name</b></td><td><code>reservation_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.reservations.reservation_revisions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `integer` |  |
| <CopyableCode code="kind" /> | `string` | Resource Provider type to be reserved. |
| <CopyableCode code="location" /> | `string` | The Azure region where the reserved resource lives. |
| <CopyableCode code="properties" /> | `object` | The properties of the reservations |
| <CopyableCode code="sku" /> | `object` | The name of sku |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="reservationId, reservationOrderId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="reservationId, reservationOrderId" /> |
