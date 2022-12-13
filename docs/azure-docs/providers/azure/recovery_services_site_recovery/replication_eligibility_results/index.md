---
title: replication_eligibility_results
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_eligibility_results
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
<tr><td><b>Name</b></td><td><code>replication_eligibility_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_eligibility_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets Unique ARM identifier for this object. |
| `name` | `string` | Gets the name of this object. |
| `type` | `string` | Gets the object type. |
| `properties` | `object` | Properties model for replication eligibility results API. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ReplicationEligibilityResults_List` | `SELECT` | `api-version, resourceGroupName, subscriptionId, virtualMachineName` |
| `ReplicationEligibilityResults_Get` | `EXEC` | `api-version, resourceGroupName, subscriptionId, virtualMachineName` |
