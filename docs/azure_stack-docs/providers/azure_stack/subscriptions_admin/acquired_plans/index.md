---
title: acquired_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - acquired_plans
  - subscriptions_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>acquired_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.acquired_plans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Identifier in the tenant subscription context. |
| <CopyableCode code="acquisitionId" /> | `string` | Acquisition identifier. |
| <CopyableCode code="acquisitionTime" /> | `string` | Acquisition time. |
| <CopyableCode code="externalReferenceId" /> | `string` | External reference identifier. |
| <CopyableCode code="planId" /> | `string` | Plan identifier in the tenant subscription context. |
| <CopyableCode code="provisioningState" /> | `string` | Provisioning state for subscriptions service resources, for example, resource provider registration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="planAcquisitionId, subscriptionId, targetSubscriptionId" /> | Gets the specified plan acquired by a subscription consuming the offer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId, targetSubscriptionId" /> | Get a collection of all acquired plans that subscription has access to. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="planAcquisitionId, subscriptionId, targetSubscriptionId" /> | Creates an acquired plan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="planAcquisitionId, subscriptionId, targetSubscriptionId" /> | Deletes an acquired plan. |
