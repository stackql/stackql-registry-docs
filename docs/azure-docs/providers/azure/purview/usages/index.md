---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - purview
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource Id |
| <CopyableCode code="name" /> | `object` | Quota name |
| <CopyableCode code="currentValue" /> | `integer` | Current usage quota value |
| <CopyableCode code="limit" /> | `integer` | Usage quota limit |
| <CopyableCode code="unit" /> | `string` | Quota usage unit. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Get the usage quota configuration |

## `SELECT` examples

Get the usage quota configuration


```sql
SELECT
id,
name,
currentValue,
limit,
unit
FROM azure.purview.usages
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```