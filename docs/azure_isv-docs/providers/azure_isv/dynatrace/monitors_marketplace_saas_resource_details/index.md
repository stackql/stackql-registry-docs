---
title: monitors_marketplace_saas_resource_details
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_marketplace_saas_resource_details
  - dynatrace
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>monitors_marketplace_saas_resource_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.dynatrace.monitors_marketplace_saas_resource_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="marketplaceSaaSResourceId" /> | `string` | Id of the Marketplace SaaS Resource |
| <CopyableCode code="marketplaceSubscriptionStatus" /> | `string` | Flag specifying the Marketplace Subscription Status of the resource. If payment is not made in time, the resource will go in Suspended state. |
| <CopyableCode code="planId" /> | `string` | Id of the plan |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId, data__tenantId" /> |
