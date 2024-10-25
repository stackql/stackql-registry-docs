---
title: threads
hide_title: false
hide_table_of_contents: false
keywords:
  - threads
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
<tr><td><b>Name</b></td><td><code>threads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.assistants.threads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints. |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) for when the thread was created. |
| <CopyableCode code="metadata" /> | `object` | Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long.<br /> |
| <CopyableCode code="object" /> | `string` | The object type, which is always `thread`. |
| <CopyableCode code="tool_resources" /> | `object` | A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_thread" /> | `SELECT` | <CopyableCode code="thread_id" /> |
| <CopyableCode code="create_thread" /> | `INSERT` |  |
| <CopyableCode code="delete_thread" /> | `DELETE` | <CopyableCode code="thread_id" /> |
| <CopyableCode code="modify_thread" /> | `UPDATE` | <CopyableCode code="thread_id" /> |
| <CopyableCode code="create_thread_and_run" /> | `EXEC` | <CopyableCode code="data__assistant_id" /> |
