---
title: reservation_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_revisions
  - reservations
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

Creates, updates, deletes, gets or lists a <code>reservation_revisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservation_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.reservations.reservation_revisions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `integer` |  |
| <CopyableCode code="kind" /> | `string` | Resource Provider type to be reserved. |
| <CopyableCode code="location" /> | `string` | The Azure region where the reserved resource lives. |
| <CopyableCode code="properties" /> | `object` | The properties of the reservations |
| <CopyableCode code="sku" /> | `object` | The name of sku |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="reservationId, reservationOrderId" /> | List of all the revisions for the `Reservation`. |

## `SELECT` examples

List of all the revisions for the `Reservation`.


```sql
SELECT
etag,
kind,
location,
properties,
sku
FROM azure.reservations.reservation_revisions
WHERE reservationId = '{{ reservationId }}'
AND reservationOrderId = '{{ reservationOrderId }}';
```