---
title: volume_annotations
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_annotations
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
<tr><td><b>Name</b></td><td><code>volume_annotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.books.volume_annotations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique id of this volume annotation. |
| `pageIds` | `array` | Pages the annotation spans. |
| `selectedText` | `string` | Excerpt from the volume. |
| `updated` | `string` | Timestamp for the last time this anntoation was updated. (RFC 3339 UTC date-time format). |
| `annotationType` | `string` | The type of annotation this is. |
| `annotationDataId` | `string` | The annotation data id for this volume annotation. |
| `data` | `string` | Data for this annotation. |
| `deleted` | `boolean` | Indicates that this annotation is deleted. |
| `volumeId` | `string` | The Volume this annotation is for. |
| `contentRanges` | `object` | The content ranges to identify the selected text. |
| `annotationDataLink` | `string` | Link to get data for this annotation. |
| `layerId` | `string` | The Layer this annotation is for. |
| `selfLink` | `string` | URL to this resource. |
| `kind` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `layers_volumeAnnotations_get` | `SELECT` | `annotationId, layerId, volumeId` | Gets the volume annotation. |
| `layers_volumeAnnotations_list` | `SELECT` | `contentVersion, layerId, volumeId` | Gets the volume annotations for a volume and layer. |
