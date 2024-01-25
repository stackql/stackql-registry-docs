---
title: accounts_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_keys
  - purview
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
<tr><td><b>Name</b></td><td><code>accounts_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.purview.accounts_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `atlasKafkaPrimaryEndpoint` | `string` | Gets or sets the primary connection string. |
| `atlasKafkaSecondaryEndpoint` | `string` | Gets or sets the secondary connection string. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` |
