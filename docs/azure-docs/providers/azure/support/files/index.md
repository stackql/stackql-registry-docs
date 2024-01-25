---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
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
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.support.files</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fileName, fileWorkspaceName, subscriptionId` | Returns details of a specific file in a work space. |
| `list` | `SELECT` | `fileWorkspaceName, subscriptionId` | Lists all the Files information under a workspace for an Azure subscription. |
| `create` | `INSERT` | `fileName, fileWorkspaceName, subscriptionId` | Creates a new file under a workspace for the specified subscription. |
| `_list` | `EXEC` | `fileWorkspaceName, subscriptionId` | Lists all the Files information under a workspace for an Azure subscription. |
| `upload` | `EXEC` | `fileName, fileWorkspaceName, subscriptionId` | This API allows you to upload content to a file |
