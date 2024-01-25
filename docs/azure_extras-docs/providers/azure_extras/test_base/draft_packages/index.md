---
title: draft_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - draft_packages
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
<tr><td><b>Name</b></td><td><code>draft_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.draft_packages</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets a Test Base Draft Package. |
| `list_by_test_base_account` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the draft packages under a test base account. |
| `create` | `INSERT` | `draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName` | Creates or replaces a Test Base Draft Package. |
| `delete` | `DELETE` | `draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName` | Deletes a Test Base Draft Package. |
| `_list_by_test_base_account` | `EXEC` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the draft packages under a test base account. |
| `copy_from_package` | `EXEC` | `draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName, data__packageId` | Copy package file and metadata from a package to this draft package |
| `extract_file` | `EXEC` | `draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName, data__sourceFile` | Performs extracting file operation for a Test Base Draft Package |
| `generate_folders_and_scripts` | `EXEC` | `draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName` | Generates folders and scripts |
| `update` | `EXEC` | `draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName` | Updates an existing Test Base Draft Package. |
