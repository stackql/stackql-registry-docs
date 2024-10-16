---
title: reservations_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations_summaries
  - consumption
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

Creates, updates, deletes, gets or lists a <code>reservations_summaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservations_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.reservations_summaries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The full qualified ARM ID of an event. |
| <CopyableCode code="name" /> | `string` | The ID that uniquely identifies an event. |
| <CopyableCode code="etag" /> | `string` | The etag for the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of the reservation summary. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="grain, resourceScope" /> | Lists the reservations summaries for the defined scope daily or monthly grain. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges. |
| <CopyableCode code="list_by_reservation_order" /> | `SELECT` | <CopyableCode code="grain, reservationOrderId" /> | Lists the reservations summaries for daily or monthly grain. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges. |
| <CopyableCode code="list_by_reservation_order_and_reservation" /> | `SELECT` | <CopyableCode code="grain, reservationId, reservationOrderId" /> | Lists the reservations summaries for daily or monthly grain. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges. |

## `SELECT` examples

Lists the reservations summaries for the defined scope daily or monthly grain. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges.


```sql
SELECT
id,
name,
etag,
properties,
tags,
type
FROM azure.consumption.reservations_summaries
WHERE grain = '{{ grain }}'
AND resourceScope = '{{ resourceScope }}';
```