---
title: favorite_processes
hide_title: false
hide_table_of_contents: false
keywords:
  - favorite_processes
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
<tr><td><b>Name</b></td><td><code>favorite_processes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.favorite_processes" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="favoriteProcessResourceName, packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a favorite process for a Test Base Package. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists the favorite processes for a specific package. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="favoriteProcessResourceName, packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Create or replace a favorite process for a Test Base Package. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="favoriteProcessResourceName, packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Deletes a favorite process for a specific package. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists the favorite processes for a specific package. |
