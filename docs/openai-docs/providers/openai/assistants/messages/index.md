---
title: messages
hide_title: false
hide_table_of_contents: false
keywords:
  - messages
  - assistants
  - openai    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage OpenAI and ChatGPT resources using SQL.
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.assistants.messages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints. |
| <CopyableCode code="assistant_id" /> | `string` | If applicable, the ID of the [assistant](/docs/api-reference/assistants) that authored this message. |
| <CopyableCode code="attachments" /> | `array` | A list of files attached to the message, and the tools they were added to. |
| <CopyableCode code="completed_at" /> | `integer` | The Unix timestamp (in seconds) for when the message was completed. |
| <CopyableCode code="content" /> | `array` | The content of the message in array of text and/or images. |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) for when the message was created. |
| <CopyableCode code="incomplete_at" /> | `integer` | The Unix timestamp (in seconds) for when the message was marked as incomplete. |
| <CopyableCode code="incomplete_details" /> | `object` | On an incomplete message, details about why the message is incomplete. |
| <CopyableCode code="metadata" /> | `object` | Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long.<br /> |
| <CopyableCode code="object" /> | `string` | The object type, which is always `thread.message`. |
| <CopyableCode code="role" /> | `string` | The entity that produced the message. One of `user` or `assistant`. |
| <CopyableCode code="run_id" /> | `string` | The ID of the [run](/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints. |
| <CopyableCode code="status" /> | `string` | The status of the message, which can be either `in_progress`, `incomplete`, or `completed`. |
| <CopyableCode code="thread_id" /> | `string` | The [thread](/docs/api-reference/threads) ID that this message belongs to. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_message" /> | `SELECT` | <CopyableCode code="message_id, thread_id" /> |
| <CopyableCode code="list_messages" /> | `SELECT` | <CopyableCode code="thread_id" /> |
| <CopyableCode code="create_message" /> | `INSERT` | <CopyableCode code="thread_id, data__content, data__role" /> |
| <CopyableCode code="delete_message" /> | `DELETE` | <CopyableCode code="message_id, thread_id" /> |
| <CopyableCode code="modify_message" /> | `UPDATE` | <CopyableCode code="message_id, thread_id" /> |