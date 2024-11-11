---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
  - models
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

Creates, updates, deletes, gets or lists a <code>models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.models.models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` | Describes an OpenAI model offering that can be used with the API. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_models" /> | `SELECT` | <CopyableCode code="" /> |  |
| <CopyableCode code="retrieve_model" /> | `SELECT` | <CopyableCode code="model" /> |  |
| <CopyableCode code="delete_model" /> | `DELETE` | <CopyableCode code="model" /> |  |

## `SELECT` examples




```sql
SELECT
column_anon
FROM openai.models.models
;
```
## `DELETE` example

Deletes the specified <code>models</code> resource.

```sql
/*+ delete */
DELETE FROM openai.models.models
WHERE model = '{{ model }}';
```
