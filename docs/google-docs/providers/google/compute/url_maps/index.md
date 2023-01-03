---
title: url_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - url_maps
  - compute
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
<tr><td><b>Name</b></td><td><code>url_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.url_maps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `hostRules` | `array` | The list of host rules to use against the URL. |
| `defaultRouteAction` | `object` |  |
| `headerAction` | `object` | The request and response header transformations that take effect before the request is passed along to the selected backendService. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field is ignored when inserting a UrlMap. An up-to-date fingerprint must be provided in order to update the UrlMap, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a UrlMap. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `defaultUrlRedirect` | `object` | Specifies settings for an HTTP redirect. |
| `region` | `string` | [Output Only] URL of the region where the regional URL map resides. This field is not applicable to global URL maps. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `defaultService` | `string` | The full or partial URL of the defaultService resource to which traffic is directed if none of the hostRules match. If defaultRouteAction is also specified, advanced routing actions, such as URL rewrites, take effect before sending the request to the backend. However, if defaultService is specified, defaultRouteAction cannot contain any weightedBackendServices. Conversely, if routeAction specifies any weightedBackendServices, service must not be specified. Only one of defaultService, defaultUrlRedirect , or defaultRouteAction.weightedBackendService must be set. defaultService has no effect when the URL map is bound to a target gRPC proxy that has the validateForProxyless field set to true. |
| `pathMatchers` | `array` | The list of named PathMatchers to use against the URL. |
| `tests` | `array` | The list of expected URL mapping tests. Request to update the UrlMap succeeds only if all test cases pass. You can specify a maximum of 100 tests per UrlMap. Not supported when the URL map is bound to a target gRPC proxy that has validateForProxyless field set to true. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#urlMaps for url maps. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `urlMaps_get` | `SELECT` | `project, urlMap` | Returns the specified UrlMap resource. Gets a list of available URL maps by making a list() request. |
| `urlMaps_list` | `SELECT` | `project` | Retrieves the list of UrlMap resources available to the specified project. |
| `urlMaps_insert` | `INSERT` | `project` | Creates a UrlMap resource in the specified project using the data included in the request. |
| `urlMaps_delete` | `DELETE` | `project, urlMap` | Deletes the specified UrlMap resource. |
| `urlMaps_invalidateCache` | `EXEC` | `project, urlMap` | Initiates a cache invalidation operation, invalidating the specified path, scoped to the specified UrlMap. For more information, see [Invalidating cached content](/cdn/docs/invalidating-cached-content). |
| `urlMaps_patch` | `EXEC` | `project, urlMap` | Patches the specified UrlMap resource with the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| `urlMaps_update` | `EXEC` | `project, urlMap` | Updates the specified UrlMap resource with the data included in the request. |
| `urlMaps_validate` | `EXEC` | `project, urlMap` | Runs static validation for the UrlMap. In particular, the tests of the provided UrlMap will be run. Calling this method does NOT create the UrlMap. |
