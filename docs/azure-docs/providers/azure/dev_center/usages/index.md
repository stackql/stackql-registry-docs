---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - dev_center
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified arm resource id. |
| <CopyableCode code="name" /> | `object` | The Usage Names. |
| <CopyableCode code="currentValue" /> | `integer` | The current usage. |
| <CopyableCode code="limit" /> | `integer` | The limit integer. |
| <CopyableCode code="unit" /> | `string` | The unit details. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Lists the current usages and limits in this location for the provided subscription. |

## `SELECT` examples

Lists the current usages and limits in this location for the provided subscription.


```sql
SELECT
id,
name,
currentValue,
limit,
unit
FROM azure.dev_center.usages
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```