---
title: legacy_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - legacy_peerings
  - peering
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

Creates, updates, deletes, gets or lists a <code>legacy_peerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>legacy_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.legacy_peerings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="kind" /> | `string` | The kind of the peering. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties that define connectivity to the Microsoft Cloud Edge. |
| <CopyableCode code="sku" /> | `object` | The SKU that defines the tier and kind of the peering. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="kind, peeringLocation, subscriptionId" /> | Lists all of the legacy peerings under the given subscription matching the specified kind and location. |

## `SELECT` examples

Lists all of the legacy peerings under the given subscription matching the specified kind and location.


```sql
SELECT
id,
name,
kind,
location,
properties,
sku,
tags,
type
FROM azure.peering.legacy_peerings
WHERE kind = '{{ kind }}'
AND peeringLocation = '{{ peeringLocation }}'
AND subscriptionId = '{{ subscriptionId }}';
```