---
title: data_transfer_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - data_transfer_jobs
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>data_transfer_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.data_transfer_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | The properties of a DataTransfer Job |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId" /> | Get a Data Transfer Job. |
| <CopyableCode code="list_by_database_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Get a list of Data Transfer jobs. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId, data__properties" /> | Creates a Data Transfer Job. |
| <CopyableCode code="_list_by_database_account" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Get a list of Data Transfer jobs. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId" /> | Cancels a Data Transfer Job. |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId" /> | Pause a Data Transfer Job. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId" /> | Resumes a Data Transfer Job. |
