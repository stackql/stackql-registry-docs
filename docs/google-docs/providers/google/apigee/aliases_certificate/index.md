---
title: aliases_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases_certificate
  - apigee
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
<tr><td><b>Name</b></td><td><code>aliases_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.aliases_certificate</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `data` | `string` | The HTTP request/response body as raw binary. |
| `extensions` | `array` | Application specific response metadata. Must be set in the first response for streaming APIs. |
| `contentType` | `string` | The HTTP Content-Type header value specifying the content type of the body. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_environments_keystores_aliases_get_certificate` | `SELECT` | `aliasesId, environmentsId, keystoresId, organizationsId` |
