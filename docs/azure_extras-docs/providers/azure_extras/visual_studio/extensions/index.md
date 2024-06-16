---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - visual_studio
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
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.visual_studio.extensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier of the resource. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="plan" /> | `object` | Plan data for an extension resource. |
| <CopyableCode code="properties" /> | `object` | Resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountResourceName, extensionResourceName, resourceGroupName, subscriptionId" /> | Gets the details of an extension associated with a Visual Studio Team Services account resource. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountResourceName, resourceGroupName, subscriptionId" /> | Gets the details of the extension resources created within the resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountResourceName, extensionResourceName, resourceGroupName, subscriptionId" /> | Registers the extension with a Visual Studio Team Services account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountResourceName, extensionResourceName, resourceGroupName, subscriptionId" /> | Removes an extension resource registration for a Visual Studio Team Services account. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountResourceName, extensionResourceName, resourceGroupName, subscriptionId" /> | Updates an existing extension registration for the Visual Studio Team Services account. |
