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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicedirectory.endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name for the endpoint in the format `projects/*/locations/*/namespaces/*/services/*/endpoints/*`. |
| <CopyableCode code="address" /> | `string` | Optional. An IPv4 or IPv6 address. Service Directory rejects bad addresses like: * `8.8.8` * `8.8.8.8:53` * `test:bad:address` * `[::1]` * `[::1]:8080` Limited to 45 characters. |
| <CopyableCode code="annotations" /> | `object` | Optional. Annotations for the endpoint. This data can be consumed by service clients. Restrictions: * The entire annotations dictionary may contain up to 512 characters, spread accoss all key-value pairs. Annotations that go beyond this limit are rejected * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/) Annotations that fails to meet these requirements are rejected. Note: This field is equivalent to the `metadata` field in the v1beta1 API. They have the same syntax and read/write to the same location in Service Directory. |
| <CopyableCode code="network" /> | `string` | Immutable. The Google Compute Engine network (VPC) of the endpoint in the format `projects//locations/global/networks/*`. The project must be specified by project number (project id is rejected). Incorrectly formatted networks are rejected, we also check to make sure that you have the servicedirectory.networks.attach permission on the project specified. |
| <CopyableCode code="port" /> | `integer` | Optional. Service Directory rejects values outside of `[0, 65535]`. |
| <CopyableCode code="uid" /> | `string` | Output only. The globally unique identifier of the endpoint in the UUID4 format. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointsId, locationsId, namespacesId, projectsId, servicesId" /> | Gets an endpoint. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, namespacesId, projectsId, servicesId" /> | Lists all endpoints. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, namespacesId, projectsId, servicesId" /> | Creates an endpoint, and returns the new endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointsId, locationsId, namespacesId, projectsId, servicesId" /> | Deletes an endpoint. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="endpointsId, locationsId, namespacesId, projectsId, servicesId" /> | Updates an endpoint. |

## `SELECT` examples

Lists all endpoints.

```sql
SELECT
name,
address,
annotations,
network,
port,
uid
FROM google.servicedirectory.endpoints
WHERE locationsId = '{{ locationsId }}'
AND namespacesId = '{{ namespacesId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoints</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.servicedirectory.endpoints (
locationsId,
namespacesId,
projectsId,
servicesId,
name,
address,
port,
annotations,
network
)
SELECT 
'{{ locationsId }}',
'{{ namespacesId }}',
'{{ projectsId }}',
'{{ servicesId }}',
'{{ name }}',
'{{ address }}',
'{{ port }}',
'{{ annotations }}',
'{{ network }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: address
      value: string
    - name: port
      value: integer
    - name: annotations
      value: object
    - name: network
      value: string
    - name: uid
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>endpoints</code> resource.

```sql
/*+ update */
UPDATE google.servicedirectory.endpoints
SET 
name = '{{ name }}',
address = '{{ address }}',
port = '{{ port }}',
annotations = '{{ annotations }}',
network = '{{ network }}'
WHERE 
endpointsId = '{{ endpointsId }}'
AND locationsId = '{{ locationsId }}'
AND namespacesId = '{{ namespacesId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```

## `DELETE` example

Deletes the specified <code>endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM google.servicedirectory.endpoints
WHERE endpointsId = '{{ endpointsId }}'
AND locationsId = '{{ locationsId }}'
AND namespacesId = '{{ namespacesId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```
