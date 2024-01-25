---
title: draft_packages_path
hide_title: false
hide_table_of_contents: false
keywords:
  - draft_packages_path
  - test_base
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>draft_packages_path</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.draft_packages_path</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `baseUrl` | `string` | The base URL of the storage account. |
| `draftPackagePath` | `string` | The relative path of the folder hosting package files. |
| `expirationTime` | `string` | Expiry date of the SAS token. |
| `sasToken` | `string` | A SAS token for the storage account to access workspace. |
| `workingPath` | `string` | The relative path for a temporary folder for package creation work. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName` |
