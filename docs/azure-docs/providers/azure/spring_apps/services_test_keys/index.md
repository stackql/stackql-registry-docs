---
title: services_test_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - services_test_keys
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>services_test_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.services_test_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `enabled` | `boolean` | Indicates whether the test endpoint feature enabled or not |
| `primaryKey` | `string` | Primary key |
| `primaryTestEndpoint` | `string` | Primary test endpoint |
| `secondaryKey` | `string` | Secondary key |
| `secondaryTestEndpoint` | `string` | Secondary test endpoint |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` |
