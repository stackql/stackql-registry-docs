---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - data_migration
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.files" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | HTTP strong entity tag value. This is ignored if submitted. |
| <CopyableCode code="properties" /> | `object` | Base class for file properties. |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | The files resource is a nested, proxy-only resource representing a file stored under the project resource. This method retrieves information about a file. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, groupName, projectName, serviceName, subscriptionId" /> | The project resource is a nested resource representing a stored migration project. This method returns a list of files owned by a project resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` |  | The PUT method creates a new file or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` |  | This method deletes a file. |
| <CopyableCode code="read" /> | `EXEC` | <CopyableCode code="api-version, fileName, groupName, projectName, serviceName, subscriptionId" /> | This method is used for requesting storage information using which contents of the file can be downloaded. |
| <CopyableCode code="read_write" /> | `EXEC` | <CopyableCode code="api-version, fileName, groupName, projectName, serviceName, subscriptionId" /> | This method is used for requesting information for reading and writing the file content. |
| <CopyableCode code="update" /> | `EXEC` |  | This method updates an existing file. |
