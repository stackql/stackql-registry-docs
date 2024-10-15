---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - network
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

Creates, updates, deletes, gets or lists a <code>usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource identifier. |
| <CopyableCode code="name" /> | `object` | The usage names. |
| <CopyableCode code="currentValue" /> | `integer` | The current value of the usage. |
| <CopyableCode code="limit" /> | `integer` | The limit of usage. |
| <CopyableCode code="unit" /> | `string` | An enum describing the unit of measurement. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List network usages for a subscription. |

## `SELECT` examples

List network usages for a subscription.


```sql
SELECT
id,
name,
currentValue,
limit,
unit
FROM azure.network.usages
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```