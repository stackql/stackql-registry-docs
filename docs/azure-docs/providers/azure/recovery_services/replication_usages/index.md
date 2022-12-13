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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services.replication_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `protectedItemCount` | `integer` | Number of replication protected items for this vault. |
| `recoveryPlanCount` | `integer` | Number of replication recovery plans for this vault. |
| `recoveryServicesProviderAuthType` | `integer` | The authentication type of recovery service providers in the vault. |
| `registeredServersCount` | `integer` | Number of servers registered to this vault. |
| `jobsSummary` | `object` | Summary of the replication job data for this vault. |
| `monitoringSummary` | `object` | Summary of the replication monitoring data for this vault. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ReplicationUsages_List` | `SELECT` | `api-version, resourceGroupName, subscriptionId, vaultName` |
