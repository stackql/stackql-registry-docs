---
title: layers
hide_title: false
hide_table_of_contents: false
keywords:
  - layers
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
<tr><td><b>Name</b></td><td><code>layers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.books.layers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique id of this layer summary. |
| `selfLink` | `string` | URL to this resource. |
| `annotationsLink` | `string` | The link to get the annotations for this layer. |
| `annotationCount` | `integer` | The number of annotations for this layer. |
| `annotationsDataLink` | `string` | Link to get data for this annotation. |
| `dataCount` | `integer` | The number of data items for this layer. |
| `annotationTypes` | `array` | The list of annotation types contained for this layer. |
| `layerId` | `string` | The layer id for this summary. |
| `kind` | `string` | Resource Type |
| `updated` | `string` | Timestamp for the last time an item in this layer was updated. (RFC 3339 UTC date-time format). |
| `volumeAnnotationsVersion` | `string` | The current version of this layer's volume annotations. Note that this version applies only to the data in the books.layers.volumeAnnotations.* responses. The actual annotation data is versioned separately. |
| `contentVersion` | `string` | The content version this resource is for. |
| `volumeId` | `string` | The volume id this resource is for. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `summaryId, volumeId` | Gets the layer summary for a volume. |
| `list` | `SELECT` | `volumeId` | List the layer summaries for a volume. |
