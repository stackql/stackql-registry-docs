---
title: python2_package
hide_title: false
hide_table_of_contents: false
keywords:
  - python2_package
  - automation
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
<tr><td><b>Name</b></td><td><code>python2_package</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.python2_package" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Gets the etag of the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Definition of the module property type. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, packageName, resourceGroupName, subscriptionId" /> | Retrieve the python 2 package identified by package name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of python 2 packages. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, packageName, resourceGroupName, subscriptionId, data__properties" /> | Create or Update the python 2 package identified by package name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, packageName, resourceGroupName, subscriptionId" /> | Delete the python 2 package by name. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="automationAccountName, packageName, resourceGroupName, subscriptionId" /> | Update the python 2 package identified by package name. |
