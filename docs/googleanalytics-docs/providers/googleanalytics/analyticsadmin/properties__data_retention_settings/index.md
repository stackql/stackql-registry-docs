---
title: properties__data_retention_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - properties__data_retention_settings
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
<tr><td><b>Name</b></td><td><code>properties__data_retention_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analyticsadmin.properties__data_retention_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name for this DataRetentionSetting resource. Format: properties/&#123;property&#125;/dataRetentionSettings |
| `resetUserDataOnNewActivity` | `boolean` | If true, reset the retention period for the user identifier with every event from that user. |
| `eventDataRetention` | `string` | The length of time that event-level data is retained. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `properties_getDataRetentionSettings` | `SELECT` | `propertiesId` |
