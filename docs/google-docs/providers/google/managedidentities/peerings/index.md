---
title: peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - peerings
  - managedidentities
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
<tr><td><b>Name</b></td><td><code>peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.managedidentities.peerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `peerings` | `array` | A list of Managed Identities Service Peerings in the project. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `peeringsId, projectsId` | Gets details of a single Peering. |
| `list` | `SELECT` | `projectsId` | Lists Peerings in a given project. |
| `create` | `INSERT` | `projectsId` | Creates a Peering for Managed AD instance. |
| `delete` | `DELETE` | `peeringsId, projectsId` | Deletes identified Peering. |
| `patch` | `EXEC` | `peeringsId, projectsId` | Updates the labels for specified Peering. |
