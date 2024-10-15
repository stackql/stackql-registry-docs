---
title: resource_changes
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_changes
  - change_analysis
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

Creates, updates, deletes, gets or lists a <code>resource_changes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_changes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.change_analysis.resource_changes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a change. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$endTime, $startTime, resourceId" /> |  |

## `SELECT` examples




```sql
SELECT
properties
FROM azure.change_analysis.resource_changes
WHERE $endTime = '{{ $endTime }}'
AND $startTime = '{{ $startTime }}'
AND resourceId = '{{ resourceId }}';
```