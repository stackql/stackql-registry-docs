---
title: releases
hide_title: false
hide_table_of_contents: false
keywords:
  - releases
  - clouddeploy
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
<tr><td><b>Name</b></td><td><code>releases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddeploy.releases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `releases` | `array` | The `Release` objects. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId, releasesId` | Gets details of a single Release. |
| `list` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId` | Lists Releases in a given project and location. |
| `create` | `INSERT` | `deliveryPipelinesId, locationsId, projectsId` | Creates a new Release in a given project and location. |
| `abandon` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId` | Abandons a Release in the Delivery Pipeline. |
