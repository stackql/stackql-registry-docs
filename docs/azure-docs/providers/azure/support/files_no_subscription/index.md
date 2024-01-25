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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>files_no_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.support.files_no_subscription</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fileName, fileWorkspaceName` | Returns details of a specific file in a work space. |
| `list` | `SELECT` | `fileWorkspaceName` | Lists all the Files information under a workspace for an Azure subscription. |
| `create` | `INSERT` | `fileName, fileWorkspaceName` | Creates a new file under a workspace. |
| `_list` | `EXEC` | `fileWorkspaceName` | Lists all the Files information under a workspace for an Azure subscription. |
| `upload` | `EXEC` | `fileName, fileWorkspaceName` | This API allows you to upload content to a file |
