---
title: annotations
hide_title: false
hide_table_of_contents: false
keywords:
  - annotations
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
<tr><td><b>Name</b></td><td><code>annotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.books.annotations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of this annotation, in the form of a GUID. |
| `afterSelectedText` | `string` | Anchor text after excerpt. For requests, if the user bookmarked a screen that has no flowing text on it, then this field should be empty. |
| `selectedText` | `string` | Excerpt from the volume. |
| `created` | `string` | Timestamp for the created time of this annotation. |
| `updated` | `string` | Timestamp for the last time this annotation was modified. |
| `kind` | `string` | Resource type. |
| `currentVersionRanges` | `object` | Selection ranges for the most recent content version. |
| `highlightStyle` | `string` | The highlight style for this annotation. |
| `clientVersionRanges` | `object` | Selection ranges sent from the client. |
| `selfLink` | `string` | URL to this resource. |
| `layerSummary` | `object` |  |
| `deleted` | `boolean` | Indicates that this annotation is deleted. |
| `volumeId` | `string` | The volume that this annotation belongs to. |
| `pageIds` | `array` | Pages that this annotation spans. |
| `data` | `string` | User-created data for this annotation. |
| `layerId` | `string` | The layer this annotation is for. |
| `beforeSelectedText` | `string` | Anchor text before excerpt. For requests, if the user bookmarked a screen that has no flowing text on it, then this field should be empty. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `mylibrary_annotations_list` | `SELECT` |  | Retrieves a list of annotations, possibly filtered. |
| `mylibrary_annotations_delete` | `DELETE` | `annotationId` | Deletes an annotation. |
| `mylibrary_annotations_insert` | `EXEC` |  | Inserts a new annotation. |
| `mylibrary_annotations_summary` | `EXEC` | `layerIds, volumeId` | Gets the summary of specified layers. |
| `mylibrary_annotations_update` | `EXEC` | `annotationId` | Updates an existing annotation. |
