---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - deployments
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.deployments.files" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the file tree entry |
| <CopyableCode code="children" /> | `array` | The list of children files of the directory (only valid for the `directory` type) |
| <CopyableCode code="contentType" /> | `string` | The content-type of the file (only valid for the `file` type) |
| <CopyableCode code="mode" /> | `number` | The file "mode" indicating file type and permissions. |
| <CopyableCode code="symlink" /> | `string` | Not currently used. See `file-list-to-tree.ts`. |
| <CopyableCode code="type" /> | `string` | String indicating the type of file tree entry. |
| <CopyableCode code="uid" /> | `string` | The unique identifier of the file (only valid for the `file` type) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_deployment_files" /> | `SELECT` | <CopyableCode code="id, teamId" /> | Allows to retrieve the file structure of a deployment by supplying the deployment unique identifier. |
| <CopyableCode code="get_deployment_file_contents" /> | `EXEC` | <CopyableCode code="fileId, id, teamId" /> | Allows to retrieve the content of a file by supplying the file identifier and the deployment unique identifier. The response body will contain the raw content of the file. |
| <CopyableCode code="upload_file" /> | `EXEC` | <CopyableCode code="teamId" /> | Before you create a deployment you need to upload the required files for that deployment. To do it, you need to first upload each file to this endpoint. Once that's completed, you can create a new deployment with the uploaded files. The file content must be placed inside the body of the request. In the case of a successful response you'll receive a status code 200 with an empty body. |
