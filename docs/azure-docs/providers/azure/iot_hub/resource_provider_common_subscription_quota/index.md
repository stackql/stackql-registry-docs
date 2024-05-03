---
title: resource_provider_common_subscription_quota
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_provider_common_subscription_quota
  - iot_hub
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
<tr><td><b>Name</b></td><td><code>resource_provider_common_subscription_quota</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.resource_provider_common_subscription_quota" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | IotHub type id |
| <CopyableCode code="name" /> | `object` | Name of Iot Hub type |
| <CopyableCode code="currentValue" /> | `integer` | Current number of IotHub type |
| <CopyableCode code="limit" /> | `integer` | Numerical limit on IotHub type |
| <CopyableCode code="type" /> | `string` | Response type |
| <CopyableCode code="unit" /> | `string` | Unit of IotHub type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> |
| <CopyableCode code="_get" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> |
