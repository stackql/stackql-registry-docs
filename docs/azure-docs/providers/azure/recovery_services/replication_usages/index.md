---
title: replication_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_usages
  - recovery_services
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
<tr><td><b>Name</b></td><td><code>replication_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services.replication_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="jobsSummary" /> | `object` | Summary of the replication job data for this vault. |
| <CopyableCode code="monitoringSummary" /> | `object` | Summary of the replication monitoring data for this vault. |
| <CopyableCode code="protectedItemCount" /> | `integer` | Number of replication protected items for this vault. |
| <CopyableCode code="recoveryPlanCount" /> | `integer` | Number of replication recovery plans for this vault. |
| <CopyableCode code="recoveryServicesProviderAuthType" /> | `integer` | The authentication type of recovery service providers in the vault. |
| <CopyableCode code="registeredServersCount" /> | `integer` | Number of servers registered to this vault. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> |
