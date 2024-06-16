---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - storage_import_export
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_import_export.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Specifies the resource identifier of the job. |
| <CopyableCode code="name" /> | `string` | Specifies the name of the job. |
| <CopyableCode code="identity" /> | `object` | Specifies the identity properties.  |
| <CopyableCode code="location" /> | `string` | Specifies the Azure location where the job is created. |
| <CopyableCode code="properties" /> | `object` | Specifies the job properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Specifies the tags that are assigned to the job. |
| <CopyableCode code="type" /> | `string` | Specifies the type of the job resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, jobName, resourceGroupName, subscriptionId" /> | Gets information about an existing job. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Returns all active and completed jobs in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Returns all active and completed jobs in a subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, jobName, resourceGroupName, subscriptionId" /> | Creates a new job or updates an existing job in the specified subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, jobName, resourceGroupName, subscriptionId" /> | Deletes an existing job. Only jobs in the Creating or Completed states can be deleted. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, jobName, resourceGroupName, subscriptionId" /> | Updates specific properties of a job. You can call this operation to notify the Import/Export service that the hard drives comprising the import or export job have been shipped to the Microsoft data center. It can also be used to cancel an existing job. |
