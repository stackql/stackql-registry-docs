---
title: tls_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - tls_routes
  - networkservices
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

Creates, updates, deletes, gets or lists a <code>tls_routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tls_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkservices.tls_routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the TlsRoute resource. It matches pattern `projects/*/locations/global/tlsRoutes/tls_route_name>`. |
| <CopyableCode code="description" /> | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="gateways" /> | `array` | Optional. Gateways defines a list of gateways this TlsRoute is attached to, as one of the routing rules to route the requests served by the gateway. Each gateway reference should match the pattern: `projects/*/locations/global/gateways/` |
| <CopyableCode code="labels" /> | `object` | Optional. Set of label tags associated with the TlsRoute resource. |
| <CopyableCode code="meshes" /> | `array` | Optional. Meshes defines a list of meshes this TlsRoute is attached to, as one of the routing rules to route the requests served by the mesh. Each mesh reference should match the pattern: `projects/*/locations/global/meshes/` The attached Mesh should be of a type SIDECAR |
| <CopyableCode code="rules" /> | `array` | Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match. |
| <CopyableCode code="selfLink" /> | `string` | Output only. Server-defined URL of this resource |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, tlsRoutesId" /> | Gets details of a single TlsRoute. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists TlsRoute in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new TlsRoute in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, tlsRoutesId" /> | Deletes a single TlsRoute. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, tlsRoutesId" /> | Updates the parameters of a single TlsRoute. |

## `SELECT` examples

Lists TlsRoute in a given project and location.

```sql
SELECT
name,
description,
createTime,
gateways,
labels,
meshes,
rules,
selfLink,
updateTime
FROM google.networkservices.tls_routes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tls_routes</code> resource.

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
INSERT INTO google.networkservices.tls_routes (
locationsId,
projectsId,
name,
description,
rules,
meshes,
gateways,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ rules }}',
'{{ meshes }}',
'{{ gateways }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
selfLink: string
createTime: string
updateTime: string
description: string
rules:
  - matches:
      - sniHost:
          - type: string
        alpn:
          - type: string
    action:
      destinations:
        - serviceName: string
          weight: integer
      idleTimeout: string
meshes:
  - type: string
gateways:
  - type: string
labels: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tls_routes</code> resource.

```sql
/*+ update */
UPDATE google.networkservices.tls_routes
SET 
name = '{{ name }}',
description = '{{ description }}',
rules = '{{ rules }}',
meshes = '{{ meshes }}',
gateways = '{{ gateways }}',
labels = '{{ labels }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tlsRoutesId = '{{ tlsRoutesId }}';
```

## `DELETE` example

Deletes the specified <code>tls_routes</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkservices.tls_routes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tlsRoutesId = '{{ tlsRoutesId }}';
```
