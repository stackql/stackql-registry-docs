---
title: metadata_imports
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata_imports
  - metastore
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metadata_imports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.metastore.metadata_imports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `metadataImports` | `array` | The imports in the specified service. |
| `nextPageToken` | `string` | A token that can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, metadataImportsId, projectsId, servicesId` | Gets details of a single import. |
| `list` | `SELECT` | `locationsId, projectsId, servicesId` | Lists imports in a service. |
| `create` | `INSERT` | `locationsId, projectsId, servicesId` | Creates a new MetadataImport in a given project and location. |
| `patch` | `EXEC` | `locationsId, metadataImportsId, projectsId, servicesId` | Updates a single import. Only the description field of MetadataImport is supported to be updated. |
