---
title: apis_rest
hide_title: false
hide_table_of_contents: false
keywords:
  - apis_rest
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
<tr><td><b>Name</b></td><td><code>apis_rest</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.discovery.apis_rest</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of this API. |
| `name` | `string` | The name of this API. |
| `description` | `string` | The description of this API. |
| `schemas` | `object` | The schemas for this API. |
| `basePath` | `string` | [DEPRECATED] The base path for REST requests. |
| `etag` | `string` | The ETag for this response. |
| `revision` | `string` | The version of this API. |
| `kind` | `string` | The kind for this response. |
| `batchPath` | `string` | The path for REST batch requests. |
| `discoveryVersion` | `string` | Indicate the version of the Discovery API used to generate this doc. |
| `title` | `string` | The title of this API. |
| `features` | `array` | A list of supported features for this API. |
| `ownerName` | `string` | The name of the owner of this API. See ownerDomain. |
| `protocol` | `string` | The protocol described by this document. |
| `packagePath` | `string` | The package of the owner of this API. See ownerDomain. |
| `canonicalName` | `string` | Indicates how the API name should be capitalized and split into various parts. Useful for generating pretty class names. |
| `ownerDomain` | `string` | The domain of the owner of this API. Together with the ownerName and a packagePath values, this can be used to generate a library for this API which would have a unique fully qualified name. |
| `documentationLink` | `string` | A link to human readable documentation for the API. |
| `resources` | `object` | The resources in this API. |
| `labels` | `array` | Labels for the status of this API, such as labs or deprecated. |
| `baseUrl` | `string` | [DEPRECATED] The base URL for REST requests. |
| `exponentialBackoffDefault` | `boolean` | Enable exponential backoff for suitable methods in the generated clients. |
| `rootUrl` | `string` | The root URL under which all API services live. |
| `version_module` | `boolean` |  |
| `icons` | `object` | Links to 16x16 and 32x32 icons representing the API. |
| `methods` | `object` | API-level methods for this API. |
| `version` | `string` | The version of this API. |
| `servicePath` | `string` | The base path for all REST requests. |
| `parameters` | `object` | Common parameters that apply across all apis. |
| `auth` | `object` | Authentication information. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `apis_getRest` | `SELECT` | `api, version` |
