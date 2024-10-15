---
title: cdn_peering_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - cdn_peering_prefixes
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

Creates, updates, deletes, gets or lists a <code>cdn_peering_prefixes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cdn_peering_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.cdn_peering_prefixes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties that define a CDN peering prefix |
| <CopyableCode code="type" /> | `string` | The type of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="peeringLocation, subscriptionId" /> | Lists all of the advertised prefixes for the specified peering location |

## `SELECT` examples

Lists all of the advertised prefixes for the specified peering location


```sql
SELECT
id,
name,
properties,
type
FROM azure.peering.cdn_peering_prefixes
WHERE peeringLocation = '{{ peeringLocation }}'
AND subscriptionId = '{{ subscriptionId }}';
```