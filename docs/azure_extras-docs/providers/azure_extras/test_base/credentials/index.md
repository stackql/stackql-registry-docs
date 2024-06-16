---
title: credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - credentials
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
<tr><td><b>Name</b></td><td><code>credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.credentials" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="credentialName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Creates or replaces a Test Base Credential. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="credentialName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Deletes an existing test base credential. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="credentialName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Updates an existing test base credential. |
