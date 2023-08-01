---
title: revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - revisions
  - run
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
<tr><td><b>Name</b></td><td><code>revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.run.revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token indicating there are more items than page_size. Use it in the next ListRevisions request to continue. |
| `revisions` | `array` | The resulting list of Revisions. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, revisionsId, servicesId` | Gets information about a Revision. |
| `list` | `SELECT` | `locationsId, projectsId, servicesId` | Lists Revisions from a given Service, or from a given location. |
| `delete` | `DELETE` | `locationsId, projectsId, revisionsId, servicesId` | Deletes a Revision. |
