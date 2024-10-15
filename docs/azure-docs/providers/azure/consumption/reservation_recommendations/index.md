---
title: reservation_recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_recommendations
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

Creates, updates, deletes, gets or lists a <code>reservation_recommendations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservation_recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.reservation_recommendations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The full qualified ARM ID of an event. |
| <CopyableCode code="name" /> | `string` | The ID that uniquely identifies an event.  |
| <CopyableCode code="etag" /> | `string` | The etag for the resource. |
| <CopyableCode code="kind" /> | `string` | Specifies the kind of reservation recommendation. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="sku" /> | `string` | Resource sku |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceScope" /> | List of recommendations for purchasing reserved instances. |

## `SELECT` examples

List of recommendations for purchasing reserved instances.


```sql
SELECT
id,
name,
etag,
kind,
location,
sku,
tags,
type
FROM azure.consumption.reservation_recommendations
WHERE resourceScope = '{{ resourceScope }}';
```