---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - app_configuration
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_configuration.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125;. |
| `origin` | `string` | Origin of the operation |
| `properties` | `object` | Extra Operation properties |
| `display` | `object` | The display information for a configuration store operation. |
| `isDataAction` | `boolean` | Indicates whether the operation is a data action |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Operations_List` | `SELECT` |  | Lists the operations available from this provider. |
| `Operations_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks whether the configuration store name is available for use. |
| `Operations_RegionalCheckNameAvailability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks whether the configuration store name is available for use. |
