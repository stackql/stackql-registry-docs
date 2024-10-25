---
title: vector_store_files
hide_title: false
hide_table_of_contents: false
keywords:
  - vector_store_files
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
<tr><td><b>Name</b></td><td><code>vector_store_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.vector_stores.vector_store_files" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints. |
| <CopyableCode code="chunking_strategy" /> | `object` | The strategy used to chunk the file. |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) for when the vector store file was created. |
| <CopyableCode code="last_error" /> | `object` | The last error associated with this vector store file. Will be `null` if there are no errors. |
| <CopyableCode code="object" /> | `string` | The object type, which is always `vector_store.file`. |
| <CopyableCode code="status" /> | `string` | The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use. |
| <CopyableCode code="usage_bytes" /> | `integer` | The total vector store usage in bytes. Note that this may be different from the original file size. |
| <CopyableCode code="vector_store_id" /> | `string` | The ID of the [vector store](/docs/api-reference/vector-stores/object) that the [File](/docs/api-reference/files) is attached to. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_vector_store_file" /> | `SELECT` | <CopyableCode code="file_id, vector_store_id" /> |
| <CopyableCode code="list_vector_store_files" /> | `SELECT` | <CopyableCode code="vector_store_id" /> |
| <CopyableCode code="create_vector_store_file" /> | `INSERT` | <CopyableCode code="vector_store_id, data__file_id" /> |
| <CopyableCode code="delete_vector_store_file" /> | `DELETE` | <CopyableCode code="file_id, vector_store_id" /> |
