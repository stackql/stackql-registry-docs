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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>draft_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.draft_packages" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a Test Base Draft Package. |
| <CopyableCode code="list_by_test_base_account" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the draft packages under a test base account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Creates or replaces a Test Base Draft Package. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Deletes a Test Base Draft Package. |
| <CopyableCode code="_list_by_test_base_account" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the draft packages under a test base account. |
| <CopyableCode code="copy_from_package" /> | `EXEC` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName, data__packageId" /> | Copy package file and metadata from a package to this draft package |
| <CopyableCode code="extract_file" /> | `EXEC` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName, data__sourceFile" /> | Performs extracting file operation for a Test Base Draft Package |
| <CopyableCode code="generate_folders_and_scripts" /> | `EXEC` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Generates folders and scripts |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Updates an existing Test Base Draft Package. |
