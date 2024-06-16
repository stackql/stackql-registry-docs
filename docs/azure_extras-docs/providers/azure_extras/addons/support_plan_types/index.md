---
title: support_plan_types
hide_title: false
hide_table_of_contents: false
keywords:
  - support_plan_types
  - addons
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>support_plan_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.addons.support_plan_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The id of the ARM resource, e.g. "/subscriptions/&#123;id&#125;/providers/Microsoft.Addons/supportProvider/&#123;supportProviderName&#125;/supportPlanTypes/&#123;planTypeName&#125;". |
| <CopyableCode code="name" /> | `string` | The name of the Canonical support plan, i.e. "essential", "standard" or "advanced". |
| <CopyableCode code="properties" /> | `object` | The properties of the Canonical support plan. |
| <CopyableCode code="type" /> | `string` | Microsoft.Addons/supportProvider |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="planTypeName, providerName, subscriptionId" /> | Returns whether or not the canonical support plan of type &#123;type&#125; is enabled for the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="planTypeName, providerName, subscriptionId" /> | Creates or updates the Canonical support plan of type &#123;type&#125; for the subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="planTypeName, providerName, subscriptionId" /> | Cancels the Canonical support plan of type &#123;type&#125; for the subscription. |
