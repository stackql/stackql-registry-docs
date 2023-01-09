---
title: data_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - data_streams
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
<tr><td><b>Name</b></td><td><code>data_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analyticsadmin.data_streams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of this Data Stream. Format: properties/&#123;property_id&#125;/dataStreams/&#123;stream_id&#125; Example: "properties/1000/dataStreams/2000" |
| `createTime` | `string` | Output only. Time when this stream was originally created. |
| `displayName` | `string` | Human-readable display name for the Data Stream. Required for web data streams. The max allowed display name length is 255 UTF-16 code units. |
| `iosAppStreamData` | `object` | Data specific to iOS app streams. |
| `type` | `string` | Required. Immutable. The type of this DataStream resource. |
| `updateTime` | `string` | Output only. Time when stream payload fields were last updated. |
| `webStreamData` | `object` | Data specific to web streams. |
| `androidAppStreamData` | `object` | Data specific to Android app streams. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `properties_dataStreams_get` | `SELECT` | `dataStreamsId, propertiesId` | Lookup for a single DataStream. |
| `properties_dataStreams_list` | `SELECT` | `propertiesId` | Lists DataStreams on a property. |
| `properties_dataStreams_create` | `INSERT` | `propertiesId` | Creates a DataStream. |
| `properties_dataStreams_delete` | `DELETE` | `dataStreamsId, propertiesId` | Deletes a DataStream on a property. |
| `properties_dataStreams_patch` | `EXEC` | `dataStreamsId, propertiesId` | Updates a DataStream on a property. |
