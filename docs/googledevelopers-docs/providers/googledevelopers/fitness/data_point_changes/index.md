---
title: data_point_changes
hide_title: false
hide_table_of_contents: false
keywords:
  - data_point_changes
  - fitness
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_point_changes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.fitness.data_point_changes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The continuation token, which is used to page through large result sets. Provide this value in a subsequent request to return the next page of results. |
| `dataSourceId` | `string` | The data stream ID of the data source with data point changes. |
| `deletedDataPoint` | `array` | Deleted data points for the user. Note, for modifications this should be parsed before handling insertions. |
| `insertedDataPoint` | `array` | Inserted data points for the user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users_dataSources_dataPointChanges_list` | `SELECT` | `dataSourceId, userId` |
