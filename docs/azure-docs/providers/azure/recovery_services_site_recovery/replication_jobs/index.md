---
title: replication_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_jobs
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Job custom data details. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, jobName, resourceGroupName, resourceName, subscriptionId" /> | Get the details of an Azure Site Recovery job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Gets the list of Azure Site Recovery Jobs for the vault. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="api-version, jobName, resourceGroupName, resourceName, subscriptionId" /> | The operation to cancel an Azure Site Recovery job. |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | The operation to export the details of the Azure Site Recovery jobs of the vault. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="api-version, jobName, resourceGroupName, resourceName, subscriptionId" /> | The operation to restart an Azure Site Recovery job. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="api-version, jobName, resourceGroupName, resourceName, subscriptionId" /> | The operation to resume an Azure Site Recovery job. |
