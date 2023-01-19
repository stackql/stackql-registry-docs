---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
  - discovery
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
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.discovery.apis</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id of this API. |
| `name` | `string` | The name of the API. |
| `description` | `string` | The description of this API. |
| `preferred` | `boolean` | True if this version is the preferred version to use. |
| `icons` | `object` | Links to 16x16 and 32x32 icons representing the API. |
| `kind` | `string` | The kind for this response. |
| `version` | `string` | The version of the API. |
| `discoveryRestUrl` | `string` | The URL for the discovery REST document. |
| `discoveryLink` | `string` | A link to the discovery document. |
| `documentationLink` | `string` | A link to human readable documentation for the API. |
| `labels` | `array` | Labels for the status of this API, such as labs or deprecated. |
| `title` | `string` | The title of this API. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
