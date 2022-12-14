---
title: data_masking_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - data_masking_rules
  - synapse
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
<tr><td><b>Name</b></td><td><code>data_masking_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.data_masking_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | The kind of Data Masking Rule. Metadata, used for Azure portal. |
| `location` | `string` | The location of the data masking rule. |
| `properties` | `object` | The properties of a Sql pool data masking rule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataMaskingRules_Get` | `SELECT` | `dataMaskingPolicyName, dataMaskingRuleName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Gets the specific Sql pool data masking rule. |
| `DataMaskingRules_ListBySqlPool` | `SELECT` | `dataMaskingPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Gets a list of Sql pool data masking rules. |
| `DataMaskingRules_CreateOrUpdate` | `INSERT` | `dataMaskingPolicyName, dataMaskingRuleName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Creates or updates a Sql pool data masking rule. |
