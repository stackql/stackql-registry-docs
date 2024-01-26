---
title: databases_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - databases_keys
  - redis_enterprise
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>databases_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.redis_enterprise.databases_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `primaryKey` | `string` | The current primary key that clients can use to authenticate |
| `secondaryKey` | `string` | The current secondary key that clients can use to authenticate |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `clusterName, databaseName, resourceGroupName, subscriptionId` |
