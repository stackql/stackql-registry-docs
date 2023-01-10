---
title: data_access_level
hide_title: false
hide_table_of_contents: false
keywords:
  - data_access_level
  - policies
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_access_level</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.policies.data_access_level</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getDataAccessLevelPolicy` | `SELECT` |  | Get the Data Access Level policy. When enabled, this policy sets the default data access level for all newly created dashboards to the viewer’s role access filter. Otherwise, newly created dashboards will default to the sharer’s role access filter and might display data that viewers’ roles don’t allow them to view. [Learn More](https://help.sumologic.com/Manage/Security/Data_Access_Level_for_Shared_Dashboards) |
| `setDataAccessLevelPolicy` | `EXEC` | `data__enabled` | Set the Data Access Level policy. When enabled, this policy sets the default data access level for all newly created dashboards to the viewer’s role access filter. Otherwise, newly created dashboards will default to the sharer’s role access filter and might display data that viewers’ roles don’t allow them to view. [Learn More](https://help.sumologic.com/Manage/Security/Data_Access_Level_for_Shared_Dashboards) |
