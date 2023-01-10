---
title: provider_resource_types
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_resource_types
  - resources
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
<tr><td><b>Name</b></td><td><code>provider_resource_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resources.provider_resource_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `locationMappings` | `array` | The location mappings that are supported by this resource type. |
| `apiVersions` | `array` | The API version. |
| `apiProfiles` | `array` | The API profiles for the resource provider. |
| `defaultApiVersion` | `string` | The default API version. |
| `aliases` | `array` | The aliases that are supported by this resource type. |
| `zoneMappings` | `array` |  |
| `capabilities` | `string` | The additional capabilities offered by this resource type. |
| `properties` | `object` | The properties. |
| `resourceType` | `string` | The resource type. |
| `locations` | `array` | The collection of locations where this resource type can be created. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ProviderResourceTypes_List` | `SELECT` | `resourceProviderNamespace, subscriptionId` |
