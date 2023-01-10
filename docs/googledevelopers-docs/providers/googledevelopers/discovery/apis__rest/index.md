---
title: apis__rest
hide_title: false
hide_table_of_contents: false
keywords:
  - apis__rest
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
<tr><td><b>Name</b></td><td><code>apis__rest</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.discovery.apis__rest</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of this API. |
| `name` | `string` | The name of this API. |
| `description` | `string` | The description of this API. |
| `packagePath` | `string` | The package of the owner of this API. See ownerDomain. |
| `revision` | `string` | The version of this API. |
| `title` | `string` | The title of this API. |
| `icons` | `object` | Links to 16x16 and 32x32 icons representing the API. |
| `basePath` | `string` | [DEPRECATED] The base path for REST requests. |
| `version` | `string` | The version of this API. |
| `resources` | `object` | The resources in this API. |
| `baseUrl` | `string` | [DEPRECATED] The base URL for REST requests. |
| `etag` | `string` | The ETag for this response. |
| `version_module` | `boolean` |  |
| `kind` | `string` | The kind for this response. |
| `schemas` | `object` | The schemas for this API. |
| `ownerName` | `string` | The name of the owner of this API. See ownerDomain. |
| `exponentialBackoffDefault` | `boolean` | Enable exponential backoff for suitable methods in the generated clients. |
| `discoveryVersion` | `string` | Indicate the version of the Discovery API used to generate this doc. |
| `batchPath` | `string` | The path for REST batch requests. |
| `auth` | `object` | Authentication information. |
| `methods` | `object` | API-level methods for this API. |
| `rootUrl` | `string` | The root URL under which all API services live. |
| `features` | `array` | A list of supported features for this API. |
| `protocol` | `string` | The protocol described by this document. |
| `ownerDomain` | `string` | The domain of the owner of this API. Together with the ownerName and a packagePath values, this can be used to generate a library for this API which would have a unique fully qualified name. |
| `documentationLink` | `string` | A link to human readable documentation for the API. |
| `parameters` | `object` | Common parameters that apply across all apis. |
| `servicePath` | `string` | The base path for all REST requests. |
| `canonicalName` | `string` | Indicates how the API name should be capitalized and split into various parts. Useful for generating pretty class names. |
| `labels` | `array` | Labels for the status of this API, such as labs or deprecated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `apis_getRest` | `SELECT` | `api, version` |
