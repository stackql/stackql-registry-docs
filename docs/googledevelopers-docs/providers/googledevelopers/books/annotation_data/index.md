---
title: annotation_data
hide_title: false
hide_table_of_contents: false
keywords:
  - annotation_data
  - books
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
<tr><td><b>Name</b></td><td><code>annotation_data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.books.annotation_data</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique id for this annotation data. |
| `volumeId` | `string` | The volume id for this data. * |
| `encodedData` | `string` | Base64 encoded data for this annotation data. |
| `layerId` | `string` | The Layer id for this data. * |
| `updated` | `string` | Timestamp for the last time this data was updated. (RFC 3339 UTC date-time format). |
| `annotationType` | `string` | The type of annotation this data is for. |
| `data` | `object` |  |
| `kind` | `string` | Resource Type |
| `selfLink` | `string` | URL for this resource. * |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `layers_annotationData_get` | `SELECT` | `annotationDataId, contentVersion, layerId, volumeId` | Gets the annotation data. |
| `layers_annotationData_list` | `SELECT` | `contentVersion, layerId, volumeId` | Gets the annotation data for a volume and layer. |
