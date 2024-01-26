---
title: single_sign_on
hide_title: false
hide_table_of_contents: false
keywords:
  - single_sign_on
  - dynatrace
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
<tr><td><b>Name</b></td><td><code>single_sign_on</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.dynatrace.single_sign_on</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The details of a Dynatrace single sign-on. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `configurationName, monitorName, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `configurationName, monitorName, resourceGroupName, subscriptionId, data__properties` |
| `_list` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
