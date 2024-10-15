---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - purview
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Operation name for display purposes |
| <CopyableCode code="display" /> | `object` | The response model for get operation properties |
| <CopyableCode code="isDataAction" /> | `boolean` | Whether operation is a data action |
| <CopyableCode code="origin" /> | `string` | origin of the operation |
| <CopyableCode code="properties" /> | `object` | properties on meta info |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | List of available operations |

## `SELECT` examples

List of available operations


```sql
SELECT
name,
display,
isDataAction,
origin,
properties
FROM azure.purview.operations
;
```