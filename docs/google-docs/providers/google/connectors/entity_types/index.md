---
title: entity_types
hide_title: false
hide_table_of_contents: false
keywords:
  - entity_types
  - connectors
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
<tr><td><b>Name</b></td><td><code>entity_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.connectors.entity_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unsupportedTypeNames` | `array` | List of entity type names which contain unsupported Datatypes. Check datatype.proto for more information. |
| `nextPageToken` | `string` | Next page token if more entity types available. |
| `types` | `array` | List of metadata related to all entity types. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_connections_entityTypes_list` | `SELECT` | `connectionsId, locationsId, projectsId` |