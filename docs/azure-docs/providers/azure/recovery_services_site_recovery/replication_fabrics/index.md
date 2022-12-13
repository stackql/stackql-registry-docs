---
title: replication_fabrics
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_fabrics
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_fabrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_fabrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `properties` | `object` | Fabric properties. |
| `type` | `string` | Resource Type |
| `location` | `string` | Resource Location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationFabrics_Get` | `SELECT` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | Gets the details of an Azure Site Recovery fabric. |
| `ReplicationFabrics_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Gets a list of the Azure Site Recovery fabrics in the vault. |
| `ReplicationFabrics_Create` | `INSERT` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | The operation to create an Azure Site Recovery fabric (for e.g. Hyper-V site). |
| `ReplicationFabrics_Delete` | `DELETE` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | The operation to delete or remove an Azure Site Recovery fabric. |
| `ReplicationFabrics_CheckConsistency` | `EXEC` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | The operation to perform a consistency check on the fabric. |
| `ReplicationFabrics_MigrateToAad` | `EXEC` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | The operation to migrate an Azure Site Recovery fabric to AAD. |
| `ReplicationFabrics_Purge` | `EXEC` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | The operation to purge(force delete) an Azure Site Recovery fabric. |
| `ReplicationFabrics_ReassociateGateway` | `EXEC` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | The operation to move replications from a process server to another process server. |
| `ReplicationFabrics_RenewCertificate` | `EXEC` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | Renews the connection certificate for the ASR replication fabric. |
