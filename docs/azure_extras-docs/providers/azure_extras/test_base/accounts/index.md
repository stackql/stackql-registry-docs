---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (either system assigned, or none) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a Test Base Account resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a Test Base Account. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the Test Base Accounts in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the Test Base Accounts in a subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Create or replace (overwrite/recreate, with potential downtime) a Test Base Account in the specified subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Deletes a Test Base Account. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the Test Base Accounts in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all the Test Base Accounts in a subscription. |
| <CopyableCode code="check_package_name_availability" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName, data__applicationName, data__name, data__version" /> | Checks that the Test Base Package name and version is valid and is not already in use. |
| <CopyableCode code="offboard" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Offboard a Test Base Account. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Update an existing Test Base Account. |
