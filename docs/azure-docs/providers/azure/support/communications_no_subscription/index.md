---
title: communications_no_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - communications_no_subscription
  - support
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
<tr><td><b>Name</b></td><td><code>communications_no_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.support.communications_no_subscription</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Describes the properties of a communication resource. |
| `type` | `string` | Type of the resource 'Microsoft.Support/communications'. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `communicationName, supportTicketName` | Returns communication details for a support ticket. |
| `create` | `INSERT` | `communicationName, supportTicketName` | Adds a new customer communication to an Azure support ticket. |
| `check_name_availability` | `EXEC` | `supportTicketName, data__name, data__type` | Check the availability of a resource name. This API should be used to check the uniqueness of the name for adding a new communication to the support ticket. |
