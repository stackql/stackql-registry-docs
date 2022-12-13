---
title: replication_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_policies
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
<tr><td><b>Name</b></td><td><code>replication_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `properties` | `object` | Protection profile custom data details. |
| `type` | `string` | Resource Type |
| `location` | `string` | Resource Location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationPolicies_Get` | `SELECT` | `api-version, policyName, resourceGroupName, resourceName, subscriptionId` | Gets the details of a replication policy. |
| `ReplicationPolicies_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the replication policies for a vault. |
| `ReplicationPolicies_Create` | `INSERT` | `api-version, policyName, resourceGroupName, resourceName, subscriptionId` | The operation to create a replication policy. |
| `ReplicationPolicies_Delete` | `DELETE` | `api-version, policyName, resourceGroupName, resourceName, subscriptionId` | The operation to delete a replication policy. |
| `ReplicationPolicies_Update` | `EXEC` | `api-version, policyName, resourceGroupName, resourceName, subscriptionId` | The operation to update a replication policy. |
