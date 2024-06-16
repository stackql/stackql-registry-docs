---
title: packages
hide_title: false
hide_table_of_contents: false
keywords:
  - packages
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
<tr><td><b>Name</b></td><td><code>packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.packages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of the Test Base Package. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a Test Base Package. |
| <CopyableCode code="list_by_test_base_account" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the packages under a Test Base Account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Create or replace (overwrite/recreate, with potential downtime) a Test Base Package. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Deletes a Test Base Package. |
| <CopyableCode code="hard_delete" /> | `EXEC` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Hard Delete a Test Base Package. |
| <CopyableCode code="run_test" /> | `EXEC` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Trigger a test run on the package. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Update an existing Test Base Package. |
