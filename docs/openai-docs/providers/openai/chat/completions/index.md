---
title: completions
hide_title: false
hide_table_of_contents: false
keywords:
  - completions
  - chat
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

Creates, updates, deletes, gets or lists a <code>completions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>completions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.chat.completions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique identifier for the chat completion. |
| <CopyableCode code="choices" /> | `array` | A list of chat completion choices. Can be more than one if `n` is greater than 1. |
| <CopyableCode code="created" /> | `integer` | The Unix timestamp (in seconds) of when the chat completion was created. |
| <CopyableCode code="model" /> | `string` | The model used for the chat completion. |
| <CopyableCode code="object" /> | `string` | The object type, which is always `chat.completion`. |
| <CopyableCode code="service_tier" /> | `string` | The service tier used for processing the request. This field is only included if the `service_tier` parameter is specified in the request. |
| <CopyableCode code="system_fingerprint" /> | `string` | This fingerprint represents the backend configuration that the model runs with. Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism. |
| <CopyableCode code="usage" /> | `object` | Usage statistics for the completion request. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_chat_completion" /> | `SELECT` | <CopyableCode code="data__messages, data__model" /> |  |

## `SELECT` examples




```sql
SELECT
id,
choices,
created,
model,
object,
service_tier,
system_fingerprint,
usage
FROM openai.chat.completions
WHERE data__messages = '{{ data__messages }}'
AND data__model = '{{ data__model }}';
```