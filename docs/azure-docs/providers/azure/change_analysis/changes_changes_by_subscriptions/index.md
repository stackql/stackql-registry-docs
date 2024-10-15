---
title: changes_changes_by_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - changes_changes_by_subscriptions
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

Creates, updates, deletes, gets or lists a <code>changes_changes_by_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>changes_changes_by_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.change_analysis.changes_changes_by_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a change. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$endTime, $startTime, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
properties
FROM azure.change_analysis.changes_changes_by_subscriptions
WHERE $endTime = '{{ $endTime }}'
AND $startTime = '{{ $startTime }}'
AND subscriptionId = '{{ subscriptionId }}';
```