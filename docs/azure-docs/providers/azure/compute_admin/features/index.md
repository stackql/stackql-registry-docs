---
title: features
hide_title: false
hide_table_of_contents: false
keywords:
  - features
  - compute_admin
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
<tr><td><b>Name</b></td><td><code>features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute_admin.features</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Properties of features. |
| `type` | `string` | Type of Resource. |
| `location` | `string` | Location of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Features_Get` | `SELECT` | `featureName, location, subscriptionId` | Get an existing feature. |
| `Features_List` | `SELECT` | `location, subscriptionId` | Get a list of existing features. |
| `DisableTenantSubscriptionFeature` | `EXEC` | `featureName, location, subscriptionId` | Disable the tenant subscription feature. |
| `EnableTenantSubscriptionFeature` | `EXEC` | `featureName, location, subscriptionId` | Enable the tenant subscription feature. |
| `UpdateGlobalFeatureSettings` | `EXEC` | `featureName, location, subscriptionId` | Update the feature settings. |
