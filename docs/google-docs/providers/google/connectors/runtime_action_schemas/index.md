---
title: runtime_action_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - runtime_action_schemas
  - connectors
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runtime_action_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.connectors.runtime_action_schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `action` | `string` | Output only. Name of the action. |
| `inputParameters` | `array` | Output only. List of input parameter metadata for the action. |
| `resultMetadata` | `array` | Output only. List of result field metadata. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_connections_runtimeActionSchemas_list` | `SELECT` | `connectionsId, locationsId, projectsId` |
