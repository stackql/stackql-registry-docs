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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>generate_benefit_utilization_summaries_report</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cost_management.generate_benefit_utilization_summaries_report</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `generate_by_billing_account` | `EXEC` | `billingAccountId, data__endDate, data__grain, data__startDate` | Triggers generation of a benefit utilization summaries report for the provided billing account. This API supports only enrollment accounts. |
| `generate_by_billing_profile` | `EXEC` | `billingAccountId, billingProfileId, data__endDate, data__grain, data__startDate` | Triggers generation of a benefit utilization summaries report for the provided billing account and billing profile. |
| `generate_by_reservation_id` | `EXEC` | `reservationId, reservationOrderId, data__endDate, data__grain, data__startDate` | Triggers generation of a benefit utilization summaries report for the provided reservation. |
| `generate_by_reservation_order_id` | `EXEC` | `reservationOrderId, data__endDate, data__grain, data__startDate` | Triggers generation of a benefit utilization summaries report for the provided reservation order. |
| `generate_by_savings_plan_id` | `EXEC` | `savingsPlanId, savingsPlanOrderId, data__endDate, data__grain, data__startDate` | Triggers generation of a benefit utilization summaries report for the provided savings plan. |
| `generate_by_savings_plan_order_id` | `EXEC` | `savingsPlanOrderId, data__endDate, data__grain, data__startDate` | Triggers generation of a benefit utilization summaries report for the provided savings plan order. |
