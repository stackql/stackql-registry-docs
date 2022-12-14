---
title: data_masking_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - data_masking_policies
  - sql
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
<tr><td><b>Name</b></td><td><code>data_masking_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.data_masking_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The properties of a database data masking policy. |
| `kind` | `string` | The kind of data masking policy. Metadata, used for Azure portal. |
| `location` | `string` | The location of the data masking policy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataMaskingPolicies_Get` | `SELECT` | `dataMaskingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId` | Gets a database data masking policy. |
| `DataMaskingPolicies_CreateOrUpdate` | `INSERT` | `dataMaskingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId` | Creates or updates a database data masking policy |
