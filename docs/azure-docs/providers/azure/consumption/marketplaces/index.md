---
title: marketplaces
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplaces
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

Creates, updates, deletes, gets or lists a <code>marketplaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>marketplaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.marketplaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The full qualified ARM ID of an event. |
| <CopyableCode code="name" /> | `string` | The ID that uniquely identifies an event. |
| <CopyableCode code="etag" /> | `string` | The etag for the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of the marketplace usage detail. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Lists the marketplaces for a scope at the defined scope. Marketplaces are available via this API only for May 1, 2014 or later. |

## `SELECT` examples

Lists the marketplaces for a scope at the defined scope. Marketplaces are available via this API only for May 1, 2014 or later.


```sql
SELECT
id,
name,
etag,
properties,
tags,
type
FROM azure.consumption.marketplaces
WHERE scope = '{{ scope }}';
```