---
title: conversion_events
hide_title: false
hide_table_of_contents: false
keywords:
  - conversion_events
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
<tr><td><b>Name</b></td><td><code>conversion_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analyticsadmin.conversion_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of this conversion event. Format: properties/&#123;property&#125;/conversionEvents/&#123;conversion_event&#125; |
| `createTime` | `string` | Output only. Time when this conversion event was created in the property. |
| `custom` | `boolean` | Output only. If set to true, this conversion event refers to a custom event. If set to false, this conversion event refers to a default event in GA. Default events typically have special meaning in GA. Default events are usually created for you by the GA system, but in some cases can be created by property admins. Custom events count towards the maximum number of custom conversion events that may be created per property. |
| `deletable` | `boolean` | Output only. If set, this event can currently be deleted via DeleteConversionEvent. |
| `eventName` | `string` | Immutable. The event name for this conversion event. Examples: 'click', 'purchase' |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `properties_conversionEvents_get` | `SELECT` | `conversionEventsId, propertiesId` | Retrieve a single conversion event. |
| `properties_conversionEvents_list` | `SELECT` | `propertiesId` | Returns a list of conversion events in the specified parent property. Returns an empty list if no conversion events are found. |
| `properties_conversionEvents_create` | `INSERT` | `propertiesId` | Creates a conversion event with the specified attributes. |
| `properties_conversionEvents_delete` | `DELETE` | `conversionEventsId, propertiesId` | Deletes a conversion event in a property. |
