---
title: nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - nodes
  - tpu
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
<tr><td><b>Name</b></td><td><code>nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.tpu.nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | The next page token or empty if none. |
| `nodes` | `array` | The listed nodes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, nodesId, projectsId` | Gets the details of a node. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists nodes. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a node. |
| `delete` | `DELETE` | `locationsId, nodesId, projectsId` | Deletes a node. |
| `patch` | `EXEC` | `locationsId, nodesId, projectsId` | Updates the configurations of a node. |
| `start` | `EXEC` | `locationsId, nodesId, projectsId` | Starts a node. |
| `stop` | `EXEC` | `locationsId, nodesId, projectsId` | Stops a node. This operation is only available with single TPU nodes. |
