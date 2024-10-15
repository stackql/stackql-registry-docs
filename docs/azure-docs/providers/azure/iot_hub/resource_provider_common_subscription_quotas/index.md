---
title: resource_provider_common_subscription_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_provider_common_subscription_quotas
  - iot_hub
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>resource_provider_common_subscription_quotas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_provider_common_subscription_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.resource_provider_common_subscription_quotas" /></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the number of free and paid iot hubs in the subscription |

## `SELECT` examples

Get the number of free and paid iot hubs in the subscription


```sql
SELECT
id,
name,
currentValue,
limit,
type,
unit
FROM azure.iot_hub.resource_provider_common_subscription_quotas
WHERE subscriptionId = '{{ subscriptionId }}';
```