---
title: exports_execution_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - exports_execution_histories
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>exports_execution_histories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>exports_execution_histories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.exports_execution_histories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="eTag" /> | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| <CopyableCode code="properties" /> | `object` | The properties of the export run. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="exportName, scope" /> | The operation to get the run history of an export for the defined scope and export name. |

## `SELECT` examples

The operation to get the run history of an export for the defined scope and export name.


```sql
SELECT
id,
name,
eTag,
properties,
type
FROM azure.cost_management.exports_execution_histories
WHERE exportName = '{{ exportName }}'
AND scope = '{{ scope }}';
```