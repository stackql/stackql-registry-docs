---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - files
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
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.files.files" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_files" /> | `SELECT` |  |
| <CopyableCode code="retrieve_file" /> | `SELECT` | <CopyableCode code="file_id" /> |
| <CopyableCode code="create_file" /> | `INSERT` |  |
| <CopyableCode code="delete_file" /> | `DELETE` | <CopyableCode code="file_id" /> |
| <CopyableCode code="download_file" /> | `EXEC` | <CopyableCode code="file_id" /> |
