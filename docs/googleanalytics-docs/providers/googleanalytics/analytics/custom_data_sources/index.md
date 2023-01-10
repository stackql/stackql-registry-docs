---
title: custom_data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_data_sources
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
<tr><td><b>Name</b></td><td><code>custom_data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.custom_data_sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Custom data source ID. |
| `name` | `string` | Name of this custom data source. |
| `description` | `string` | Description of custom data source. |
| `schema` | `array` | Collection of schema headers of the custom data source. |
| `selfLink` | `string` | Link for this Analytics custom data source. |
| `profilesLinked` | `array` | IDs of views (profiles) linked to the custom data source. |
| `webPropertyId` | `string` | Web property ID of the form UA-XXXXX-YY to which this custom data source belongs. |
| `kind` | `string` | Resource type for Analytics custom data source. |
| `type` | `string` | Type of the custom data source. |
| `parentLink` | `object` | Parent link for this custom data source. Points to the web property to which this custom data source belongs. |
| `childLink` | `object` |  |
| `importBehavior` | `string` |  |
| `uploadType` | `string` | Upload type of the custom data source. |
| `accountId` | `string` | Account ID to which this custom data source belongs. |
| `updated` | `string` | Time this custom data source was last modified. |
| `created` | `string` | Time this custom data source was created. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `management_customDataSources_list` | `SELECT` | `accountId, webPropertyId` |
