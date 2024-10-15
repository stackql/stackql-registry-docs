---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - signalr
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.signalr.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ARM resource id |
| <CopyableCode code="name" /> | `object` | Localizable String object containing the name and a localized value. |
| <CopyableCode code="currentValue" /> | `integer` | Current value for the usage quota. |
| <CopyableCode code="limit" /> | `integer` | The maximum permitted value for the usage quota. If there is no limit, this value will be -1. |
| <CopyableCode code="unit" /> | `string` | Representing the units of the usage quota. Possible values are: Count, Bytes, Seconds, Percent, CountPerSecond, BytesPerSecond. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List resource usage quotas by location. |

## `SELECT` examples

List resource usage quotas by location.


```sql
SELECT
id,
name,
currentValue,
limit,
unit
FROM azure.signalr.usages
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```