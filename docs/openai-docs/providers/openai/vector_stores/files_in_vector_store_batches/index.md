---
title: files_in_vector_store_batches
hide_title: false
hide_table_of_contents: false
keywords:
  - files_in_vector_store_batches
  - vector_stores
  - openai
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage openai resources using SQL
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>files_in_vector_store_batches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>files_in_vector_store_batches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.vector_stores.files_in_vector_store_batches" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_files_in_vector_store_batch" /> | `SELECT` | <CopyableCode code="batch_id, vector_store_id" /> |  |

## `SELECT` examples




```sql
SELECT
column_anon
FROM openai.vector_stores.files_in_vector_store_batches
WHERE batch_id = '{{ batch_id }}'
AND vector_store_id = '{{ vector_store_id }}';
```