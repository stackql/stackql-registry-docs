---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - files
  - filemanagement
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>files</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.filemanagement.files" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="file_path, deployment_name" /> | Deletes a file. If the request is successful, there is no response body. |
| <CopyableCode code="download" /> | `EXEC` | <CopyableCode code="file_path, deployment_name" /> | Downloads a file. The file contents are the response body. This is a standard HTTP file download, not a JSON RPC. It supports the Range and If-Unmodified-Since HTTP headers. |
| <CopyableCode code="upload" /> | `EXEC` | <CopyableCode code="file_path, deployment_name" /> | Uploads a file of up to 5 GiB. The file contents should be sent as the request body as raw bytes (an octet stream); do not encode or otherwise modify the bytes before sending. The contents of the resulting file will be exactly the bytes sent in the request body. If the request is successful, there is no response body. |

## `DELETE` example

Deletes a <code>files</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.filemanagement.files
WHERE file_path = '{{ file_path }}' AND
deployment_name = '{{ deployment_name }}';
```
