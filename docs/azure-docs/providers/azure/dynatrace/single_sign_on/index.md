---
title: single_sign_on
hide_title: false
hide_table_of_contents: false
keywords:
  - single_sign_on
  - dynatrace
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
<tr><td><b>Name</b></td><td><code>single_sign_on</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dynatrace.single_sign_on</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | The details of a Dynatrace single sign-on. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SingleSignOn_Get` | `SELECT` | `configurationName, monitorName, resourceGroupName, subscriptionId` |
| `SingleSignOn_List` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `SingleSignOn_CreateOrUpdate` | `INSERT` | `configurationName, monitorName, resourceGroupName, subscriptionId, data__properties` |
