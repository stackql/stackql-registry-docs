---
title: custom_dimensions
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_dimensions
  - analytics
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_dimensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.custom_dimensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Custom dimension ID. |
| `name` | `string` | Name of the custom dimension. |
| `kind` | `string` | Kind value for a custom dimension. Set to "analytics#customDimension". It is a read-only field. |
| `scope` | `string` | Scope of the custom dimension: HIT, SESSION, USER or PRODUCT. |
| `created` | `string` | Time the custom dimension was created. |
| `index` | `integer` | Index of the custom dimension. |
| `active` | `boolean` | Boolean indicating whether the custom dimension is active. |
| `selfLink` | `string` | Link for the custom dimension |
| `parentLink` | `object` | Parent link for the custom dimension. Points to the property to which the custom dimension belongs. |
| `accountId` | `string` | Account ID. |
| `webPropertyId` | `string` | Property ID. |
| `updated` | `string` | Time the custom dimension was last modified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_customDimensions_get` | `SELECT` | `accountId, customDimensionId, webPropertyId` | Get a custom dimension to which the user has access. |
| `management_customDimensions_list` | `SELECT` | `accountId, webPropertyId` | Lists custom dimensions to which the user has access. |
| `management_customDimensions_insert` | `EXEC` | `accountId, webPropertyId` | Create a new custom dimension. |
| `management_customDimensions_patch` | `EXEC` | `accountId, customDimensionId, webPropertyId` | Updates an existing custom dimension. This method supports patch semantics. |
| `management_customDimensions_update` | `EXEC` | `accountId, customDimensionId, webPropertyId` | Updates an existing custom dimension. |
