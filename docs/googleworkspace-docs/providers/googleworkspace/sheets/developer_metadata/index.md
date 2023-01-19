---
title: developer_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - developer_metadata
  - sheets
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>developer_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.sheets.developer_metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `object` | A location where metadata may be associated in a spreadsheet. |
| `metadataId` | `integer` | The spreadsheet-scoped unique ID that identifies the metadata. IDs may be specified when metadata is created, otherwise one will be randomly generated and assigned. Must be positive. |
| `metadataKey` | `string` | The metadata key. There may be multiple metadata in a spreadsheet with the same key. Developer metadata must always have a key specified. |
| `metadataValue` | `string` | Data associated with the metadata's key. |
| `visibility` | `string` | The metadata visibility. Developer metadata must always have a visibility specified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `spreadsheets_developerMetadata_get` | `SELECT` | `metadataId, spreadsheetId` | Returns the developer metadata with the specified ID. The caller must specify the spreadsheet ID and the developer metadata's unique metadataId. |
| `spreadsheets_developerMetadata_search` | `EXEC` | `spreadsheetId` | Returns all developer metadata matching the specified DataFilter. If the provided DataFilter represents a DeveloperMetadataLookup object, this will return all DeveloperMetadata entries selected by it. If the DataFilter represents a location in a spreadsheet, this will return all developer metadata associated with locations intersecting that region. |
