---
title: tcp_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - tcp_routes
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

Creates, updates, deletes, gets or lists a <code>tcp_routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tcp_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkservices.tcp_routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the TcpRoute resource. It matches pattern `projects/*/locations/global/tcpRoutes/tcp_route_name>`. |
| <CopyableCode code="description" /> | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="gateways" /> | `array` | Optional. Gateways defines a list of gateways this TcpRoute is attached to, as one of the routing rules to route the requests served by the gateway. Each gateway reference should match the pattern: `projects/*/locations/global/gateways/` |
| <CopyableCode code="labels" /> | `object` | Optional. Set of label tags associated with the TcpRoute resource. |
| <CopyableCode code="meshes" /> | `array` | Optional. Meshes defines a list of meshes this TcpRoute is attached to, as one of the routing rules to route the requests served by the mesh. Each mesh reference should match the pattern: `projects/*/locations/global/meshes/` The attached Mesh should be of a type SIDECAR |
| <CopyableCode code="rules" /> | `array` | Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match. |
| <CopyableCode code="selfLink" /> | `string` | Output only. Server-defined URL of this resource |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, tcpRoutesId" /> | Gets details of a single TcpRoute. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists TcpRoute in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new TcpRoute in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, tcpRoutesId" /> | Deletes a single TcpRoute. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, tcpRoutesId" /> | Updates the parameters of a single TcpRoute. |

## `SELECT` examples

Lists TcpRoute in a given project and location.

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
FROM google.networkservices.tcp_routes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tcp_routes</code> resource.

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
INSERT INTO google.networkservices.tcp_routes (
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
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: selfLink
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: description
      value: string
    - name: rules
      value:
        - - name: matches
            value:
              - - name: address
                  value: string
                - name: port
                  value: string
          - name: action
            value:
              - name: destinations
                value:
                  - - name: serviceName
                      value: string
                    - name: weight
                      value: integer
              - name: originalDestination
                value: boolean
              - name: idleTimeout
                value: string
    - name: meshes
      value:
        - string
    - name: gateways
      value:
        - string
    - name: labels
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tcp_routes</code> resource.

```sql
/*+ update */
UPDATE google.networkservices.tcp_routes
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
AND tcpRoutesId = '{{ tcpRoutesId }}';
```

## `DELETE` example

Deletes the specified <code>tcp_routes</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkservices.tcp_routes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tcpRoutesId = '{{ tcpRoutesId }}';
```
