---
title: usage_aggregates
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_aggregates
  - commerce
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

Creates, updates, deletes, gets or lists a <code>usage_aggregates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_aggregates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.commerce.usage_aggregates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique Id for the usage aggregate. |
| <CopyableCode code="name" /> | `string` | Name of the usage aggregate. |
| <CopyableCode code="properties" /> | `object` | Describes a sample of the usageAggregation. |
| <CopyableCode code="type" /> | `string` | Type of the resource being returned. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="reportedEndTime, reportedStartTime, subscriptionId" /> | Query aggregated Azure subscription consumption data for a date range. |

## `SELECT` examples

Query aggregated Azure subscription consumption data for a date range.


```sql
SELECT
id,
name,
properties,
type
FROM azure_extras.commerce.usage_aggregates
WHERE reportedEndTime = '{{ reportedEndTime }}'
AND reportedStartTime = '{{ reportedStartTime }}'
AND subscriptionId = '{{ subscriptionId }}';
```