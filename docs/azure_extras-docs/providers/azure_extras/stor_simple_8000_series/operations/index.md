---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - stor_simple_8000_series
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.stor_simple_8000_series.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the operation being performed on a particular object. Name format: "&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;read\|write\|delete\|action&#125;". Eg. Microsoft.StorSimple/managers/devices/volumeContainers/read, Microsoft.StorSimple/managers/devices/alerts/clearAlerts/action |
| `display` | `object` | Contains the localized display information for this particular operation/action. These value will be used by several clients for (a) custom role definitions for RBAC, (b) complex query filters for the event service and (c) audit history/records for management operations. |
| `origin` | `string` | The intended executor of the operation; governs the display of the operation in the RBAC UX and the audit logs UX. Default value is "user,system" |
| `properties` | `object` | Represents properties of AvailableProviderOperation |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` |  |
