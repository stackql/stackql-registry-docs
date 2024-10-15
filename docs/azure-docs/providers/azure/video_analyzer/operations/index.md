---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - video_analyzer
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

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.video_analyzer.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The operation name. |
| <CopyableCode code="actionType" /> | `string` | Indicates the action type. |
| <CopyableCode code="display" /> | `object` | Operation details. |
| <CopyableCode code="isDataAction" /> | `boolean` | Whether the operation applies to data-plane. |
| <CopyableCode code="origin" /> | `string` | Origin of the operation. |
| <CopyableCode code="properties" /> | `object` | Metric properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all the Media operations. |

## `SELECT` examples

Lists all the Media operations.


```sql
SELECT
name,
actionType,
display,
isDataAction,
origin,
properties
FROM azure.video_analyzer.operations
;
```