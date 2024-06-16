---
title: generate_benefit_utilization_summaries_report
hide_title: false
hide_table_of_contents: false
keywords:
  - generate_benefit_utilization_summaries_report
  - cost_management
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
<tr><td><b>Name</b></td><td><code>generate_benefit_utilization_summaries_report</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.generate_benefit_utilization_summaries_report" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="generate_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountId, data__endDate, data__grain, data__startDate" /> | Triggers generation of a benefit utilization summaries report for the provided billing account. This API supports only enrollment accounts. |
| <CopyableCode code="generate_by_billing_profile" /> | `EXEC` | <CopyableCode code="billingAccountId, billingProfileId, data__endDate, data__grain, data__startDate" /> | Triggers generation of a benefit utilization summaries report for the provided billing account and billing profile. |
| <CopyableCode code="generate_by_reservation_id" /> | `EXEC` | <CopyableCode code="reservationId, reservationOrderId, data__endDate, data__grain, data__startDate" /> | Triggers generation of a benefit utilization summaries report for the provided reservation. |
| <CopyableCode code="generate_by_reservation_order_id" /> | `EXEC` | <CopyableCode code="reservationOrderId, data__endDate, data__grain, data__startDate" /> | Triggers generation of a benefit utilization summaries report for the provided reservation order. |
| <CopyableCode code="generate_by_savings_plan_id" /> | `EXEC` | <CopyableCode code="savingsPlanId, savingsPlanOrderId, data__endDate, data__grain, data__startDate" /> | Triggers generation of a benefit utilization summaries report for the provided savings plan. |
| <CopyableCode code="generate_by_savings_plan_order_id" /> | `EXEC` | <CopyableCode code="savingsPlanOrderId, data__endDate, data__grain, data__startDate" /> | Triggers generation of a benefit utilization summaries report for the provided savings plan order. |
