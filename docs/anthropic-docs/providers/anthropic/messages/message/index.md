---
title: message
hide_title: false
hide_table_of_contents: false
keywords:
  - message
  - messages
  - anthropic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Anthropic resources using SQL.
custom_edit_url: null
image: /img/providers/anthropic/stackql-anthropic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>message</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="anthropic.messages.message" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique object identifier. |
| <CopyableCode code="content" /> | `array` | The generated content blocks by the model. |
| <CopyableCode code="model" /> | `string` | The model that handled the request. |
| <CopyableCode code="role" /> | `string` | The conversational role of the generated message. |
| <CopyableCode code="stop_reason" /> | `string` | The reason the model stopped generating. |
| <CopyableCode code="stop_sequence" /> | `string` | The stop sequence that caused the model to stop, if applicable. |
| <CopyableCode code="type" /> | `string` | Object type, which is always "message" for Messages API. |
| <CopyableCode code="usage" /> | `object` | Information about token usage and rate limits. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="create_message" /> | `SELECT` | <CopyableCode code="anthropic-version, data__max_tokens, data__messages, data__model" /> |
