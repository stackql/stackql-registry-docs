---
title: files_no_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - files_no_subscription
  - support
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
<tr><td><b>Name</b></td><td><code>files_no_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.files_no_subscription" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fileName, fileWorkspaceName" /> | Returns details of a specific file in a work space. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="fileWorkspaceName" /> | Lists all the Files information under a workspace for an Azure subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fileName, fileWorkspaceName" /> | Creates a new file under a workspace. |
| <CopyableCode code="upload" /> | `EXEC` | <CopyableCode code="fileName, fileWorkspaceName" /> | This API allows you to upload content to a file |
