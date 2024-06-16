---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - batch
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
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.application" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="etag" /> | `string` | The ETag of the resource, used for concurrency statements. |
| <CopyableCode code="properties" /> | `object` | The properties associated with the Application. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, applicationName, resourceGroupName, subscriptionId" /> | Gets information about the specified application. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all of the applications in the specified account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, applicationName, resourceGroupName, subscriptionId" /> | Adds an application to the specified Batch account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, applicationName, resourceGroupName, subscriptionId" /> | Deletes an application. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, applicationName, resourceGroupName, subscriptionId" /> | Updates settings for the specified application. |
