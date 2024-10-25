---
title: vector_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - vector_stores
  - vector_stores
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
<tr><td><b>Name</b></td><td><code>vector_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.vector_stores.vector_stores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints. |
| <CopyableCode code="name" /> | `string` | The name of the vector store. |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) for when the vector store was created. |
| <CopyableCode code="expires_after" /> | `object` | The expiration policy for a vector store. |
| <CopyableCode code="expires_at" /> | `integer` | The Unix timestamp (in seconds) for when the vector store will expire. |
| <CopyableCode code="file_counts" /> | `object` |  |
| <CopyableCode code="last_active_at" /> | `integer` | The Unix timestamp (in seconds) for when the vector store was last active. |
| <CopyableCode code="metadata" /> | `object` | Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long.<br /> |
| <CopyableCode code="object" /> | `string` | The object type, which is always `vector_store`. |
| <CopyableCode code="status" /> | `string` | The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use. |
| <CopyableCode code="usage_bytes" /> | `integer` | The total number of bytes used by the files in the vector store. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_vector_store" /> | `SELECT` | <CopyableCode code="vector_store_id" /> |
| <CopyableCode code="list_vector_stores" /> | `SELECT` |  |
| <CopyableCode code="create_vector_store" /> | `INSERT` |  |
| <CopyableCode code="delete_vector_store" /> | `DELETE` | <CopyableCode code="vector_store_id" /> |
| <CopyableCode code="modify_vector_store" /> | `UPDATE` | <CopyableCode code="vector_store_id" /> |
