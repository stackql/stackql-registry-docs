---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - servicedirectory
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
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicedirectory.endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name for the endpoint in the format `projects/*/locations/*/namespaces/*/services/*/endpoints/*`. |
| `annotations` | `object` | Optional. Annotations for the endpoint. This data can be consumed by service clients. Restrictions: * The entire annotations dictionary may contain up to 512 characters, spread accoss all key-value pairs. Annotations that go beyond this limit are rejected * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/) Annotations that fails to meet these requirements are rejected. Note: This field is equivalent to the `metadata` field in the v1beta1 API. They have the same syntax and read/write to the same location in Service Directory. |
| `network` | `string` | Immutable. The Google Compute Engine network (VPC) of the endpoint in the format `projects//locations/global/networks/*`. The project must be specified by project number (project id is rejected). Incorrectly formatted networks are rejected, we also check to make sure that you have the servicedirectory.networks.attach permission on the project specified. |
| `port` | `integer` | Optional. Service Directory rejects values outside of `[0, 65535]`. |
| `address` | `string` | Optional. An IPv4 or IPv6 address. Service Directory rejects bad addresses like: * `8.8.8` * `8.8.8.8:53` * `test:bad:address` * `[::1]` * `[::1]:8080` Limited to 45 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_namespaces_services_endpoints_get` | `SELECT` | `endpointsId, locationsId, namespacesId, projectsId, servicesId` | Gets an endpoint. |
| `projects_locations_namespaces_services_endpoints_list` | `SELECT` | `locationsId, namespacesId, projectsId, servicesId` | Lists all endpoints. |
| `projects_locations_namespaces_services_endpoints_create` | `INSERT` | `locationsId, namespacesId, projectsId, servicesId` | Creates an endpoint, and returns the new endpoint. |
| `projects_locations_namespaces_services_endpoints_delete` | `DELETE` | `endpointsId, locationsId, namespacesId, projectsId, servicesId` | Deletes an endpoint. |
| `projects_locations_namespaces_services_endpoints_patch` | `EXEC` | `endpointsId, locationsId, namespacesId, projectsId, servicesId` | Updates an endpoint. |
