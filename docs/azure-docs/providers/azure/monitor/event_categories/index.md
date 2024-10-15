---
title: event_categories
hide_title: false
hide_table_of_contents: false
keywords:
  - event_categories
  - monitor
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

Creates, updates, deletes, gets or lists a <code>event_categories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_categories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.event_categories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="localizedValue" /> | `string` | The display name. |
| <CopyableCode code="value" /> | `string` | The invariant value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Get the list of available event categories supported in the Activity Logs Service.<br>The current list includes the following: Administrative, Security, ServiceHealth, Alert, Recommendation, Policy. |

## `SELECT` examples

Get the list of available event categories supported in the Activity Logs Service.<br>The current list includes the following: Administrative, Security, ServiceHealth, Alert, Recommendation, Policy.


```sql
SELECT
localizedValue,
value
FROM azure.monitor.event_categories
;
```