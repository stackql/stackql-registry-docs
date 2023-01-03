---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicedirectory.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name for the service in the format `projects/*/locations/*/namespaces/*/services/*`. |
| `endpoints` | `array` | Output only. Endpoints associated with this service. Returned on LookupService.ResolveService. Control plane clients should use RegistrationService.ListEndpoints. |
| `annotations` | `object` | Optional. Annotations for the service. This data can be consumed by service clients. Restrictions: * The entire annotations dictionary may contain up to 2000 characters, spread accoss all key-value pairs. Annotations that go beyond this limit are rejected * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/). Annotations that fails to meet these requirements are rejected Note: This field is equivalent to the `metadata` field in the v1beta1 API. They have the same syntax and read/write to the same location in Service Directory. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_namespaces_services_get` | `SELECT` | `locationsId, namespacesId, projectsId, servicesId` | Gets a service. |
| `projects_locations_namespaces_services_list` | `SELECT` | `locationsId, namespacesId, projectsId` | Lists all services belonging to a namespace. |
| `projects_locations_namespaces_services_create` | `INSERT` | `locationsId, namespacesId, projectsId` | Creates a service, and returns the new service. |
| `projects_locations_namespaces_services_delete` | `DELETE` | `locationsId, namespacesId, projectsId, servicesId` | Deletes a service. This also deletes all endpoints associated with the service. |
| `projects_locations_namespaces_services_patch` | `EXEC` | `locationsId, namespacesId, projectsId, servicesId` | Updates a service. |
| `projects_locations_namespaces_services_resolve` | `EXEC` | `locationsId, namespacesId, projectsId, servicesId` | Returns a service and its associated endpoints. Resolving a service is not considered an active developer method. |
