---
title: replication_protection_intents
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_intents
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
<tr><td><b>Name</b></td><td><code>replication_protection_intents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_protection_intents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `type` | `string` | Resource Type |
| `location` | `string` | Resource Location |
| `properties` | `object` | Replication protection intent custom data details. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationProtectionIntents_Get` | `SELECT` | `api-version, intentObjectName, resourceGroupName, resourceName, subscriptionId` | Gets the details of an ASR replication protection intent. |
| `ReplicationProtectionIntents_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Gets the list of ASR replication protection intent objects in the vault. |
| `ReplicationProtectionIntents_Create` | `INSERT` | `api-version, intentObjectName, resourceGroupName, resourceName, subscriptionId` | The operation to create an ASR replication protection intent item. |
