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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicedirectory.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name for the service in the format `projects/*/locations/*/namespaces/*/services/*`. |
| <CopyableCode code="annotations" /> | `object` | Optional. Annotations for the service. This data can be consumed by service clients. Restrictions: * The entire annotations dictionary may contain up to 2000 characters, spread accoss all key-value pairs. Annotations that go beyond this limit are rejected * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/). Annotations that fails to meet these requirements are rejected Note: This field is equivalent to the `metadata` field in the v1beta1 API. They have the same syntax and read/write to the same location in Service Directory. |
| <CopyableCode code="endpoints" /> | `array` | Output only. Endpoints associated with this service. Returned on LookupService.ResolveService. Control plane clients should use RegistrationService.ListEndpoints. |
| <CopyableCode code="uid" /> | `string` | Output only. The globally unique identifier of the service in the UUID4 format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, namespacesId, projectsId, servicesId" /> | Gets a service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, namespacesId, projectsId" /> | Lists all services belonging to a namespace. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, namespacesId, projectsId" /> | Creates a service, and returns the new service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, namespacesId, projectsId, servicesId" /> | Deletes a service. This also deletes all endpoints associated with the service. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, namespacesId, projectsId, servicesId" /> | Updates a service. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, namespacesId, projectsId" /> | Lists all services belonging to a namespace. |
| <CopyableCode code="resolve" /> | `EXEC` | <CopyableCode code="locationsId, namespacesId, projectsId, servicesId" /> | Returns a service and its associated endpoints. Resolving a service is not considered an active developer method. |
