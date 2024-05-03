---
title: reservations_details
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations_details
  - consumption
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
<tr><td><b>Name</b></td><td><code>reservations_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.reservations_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The properties of the reservation detail. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceScope" /> |
| <CopyableCode code="list_by_reservation_order" /> | `SELECT` | <CopyableCode code="$filter, reservationOrderId" /> |
| <CopyableCode code="list_by_reservation_order_and_reservation" /> | `SELECT` | <CopyableCode code="$filter, reservationId, reservationOrderId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceScope" /> |
| <CopyableCode code="_list_by_reservation_order" /> | `EXEC` | <CopyableCode code="$filter, reservationOrderId" /> |
| <CopyableCode code="_list_by_reservation_order_and_reservation" /> | `EXEC` | <CopyableCode code="$filter, reservationId, reservationOrderId" /> |
