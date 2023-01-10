---
title: custom_dimensions
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_dimensions
  - analyticsadmin
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
<tr><td><b>Id</b></td><td><code>googleanalytics.analyticsadmin.custom_dimensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name for this CustomDimension resource. Format: properties/&#123;property&#125;/customDimensions/&#123;customDimension&#125; |
| `description` | `string` | Optional. Description for this custom dimension. Max length of 150 characters. |
| `disallowAdsPersonalization` | `boolean` | Optional. If set to true, sets this dimension as NPA and excludes it from ads personalization. This is currently only supported by user-scoped custom dimensions. |
| `displayName` | `string` | Required. Display name for this custom dimension as shown in the Analytics UI. Max length of 82 characters, alphanumeric plus space and underscore starting with a letter. Legacy system-generated display names may contain square brackets, but updates to this field will never permit square brackets. |
| `parameterName` | `string` | Required. Immutable. Tagging parameter name for this custom dimension. If this is a user-scoped dimension, then this is the user property name. If this is an event-scoped dimension, then this is the event parameter name. May only contain alphanumeric and underscore characters, starting with a letter. Max length of 24 characters for user-scoped dimensions, 40 characters for event-scoped dimensions. |
| `scope` | `string` | Required. Immutable. The scope of this dimension. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `properties_customDimensions_get` | `SELECT` | `customDimensionsId, propertiesId` | Lookup for a single CustomDimension. |
| `properties_customDimensions_list` | `SELECT` | `propertiesId` | Lists CustomDimensions on a property. |
| `properties_customDimensions_create` | `INSERT` | `propertiesId` | Creates a CustomDimension. |
| `properties_customDimensions_archive` | `EXEC` | `customDimensionsId, propertiesId` | Archives a CustomDimension on a property. |
| `properties_customDimensions_patch` | `EXEC` | `customDimensionsId, propertiesId` | Updates a CustomDimension on a property. |
