---
title: single_sign_on_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - single_sign_on_configurations
  - datadog
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
<tr><td><b>Name</b></td><td><code>single_sign_on_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.datadog.single_sign_on_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ARM id of the resource. |
| `name` | `string` | Name of the configuration. |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SingleSignOnConfigurations_Get` | `SELECT` | `configurationName, monitorName, resourceGroupName, subscriptionId` |
| `SingleSignOnConfigurations_List` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `SingleSignOnConfigurations_CreateOrUpdate` | `INSERT` | `configurationName, monitorName, resourceGroupName, subscriptionId` |
