---
title: http_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - http_routes
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

Creates, updates, deletes, gets or lists a <code>http_routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>http_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkservices.http_routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the HttpRoute resource. It matches pattern `projects/*/locations/global/httpRoutes/http_route_name>`. |
| <CopyableCode code="description" /> | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="gateways" /> | `array` | Optional. Gateways defines a list of gateways this HttpRoute is attached to, as one of the routing rules to route the requests served by the gateway. Each gateway reference should match the pattern: `projects/*/locations/global/gateways/` |
| <CopyableCode code="hostnames" /> | `array` | Required. Hostnames define a set of hosts that should match against the HTTP host header to select a HttpRoute to process the request. Hostname is the fully qualified domain name of a network host, as defined by RFC 1123 with the exception that: - IPs are not allowed. - A hostname may be prefixed with a wildcard label (`*.`). The wildcard label must appear by itself as the first label. Hostname can be "precise" which is a domain name without the terminating dot of a network host (e.g. `foo.example.com`) or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. `*.example.com`). Note that as per RFC1035 and RFC1123, a label must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character. No other punctuation is allowed. The routes associated with a Mesh or Gateways must have unique hostnames. If you attempt to attach multiple routes with conflicting hostnames, the configuration will be rejected. For example, while it is acceptable for routes for the hostnames `*.foo.bar.com` and `*.bar.com` to be associated with the same Mesh (or Gateways under the same scope), it is not possible to associate two routes both with `*.bar.com` or both with `bar.com`. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of label tags associated with the HttpRoute resource. |
| <CopyableCode code="meshes" /> | `array` | Optional. Meshes defines a list of meshes this HttpRoute is attached to, as one of the routing rules to route the requests served by the mesh. Each mesh reference should match the pattern: `projects/*/locations/global/meshes/` The attached Mesh should be of a type SIDECAR |
| <CopyableCode code="rules" /> | `array` | Required. Rules that define how traffic is routed and handled. Rules will be matched sequentially based on the RouteMatch specified for the rule. |
| <CopyableCode code="selfLink" /> | `string` | Output only. Server-defined URL of this resource |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="httpRoutesId, locationsId, projectsId" /> | Gets details of a single HttpRoute. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists HttpRoute in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new HttpRoute in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="httpRoutesId, locationsId, projectsId" /> | Deletes a single HttpRoute. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="httpRoutesId, locationsId, projectsId" /> | Updates the parameters of a single HttpRoute. |

## `SELECT` examples

Lists HttpRoute in a given project and location.

```sql
SELECT
name,
description,
createTime,
gateways,
hostnames,
labels,
meshes,
rules,
selfLink,
updateTime
FROM google.networkservices.http_routes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>http_routes</code> resource.

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
INSERT INTO google.networkservices.http_routes (
locationsId,
projectsId,
name,
selfLink,
description,
createTime,
updateTime,
hostnames,
meshes,
gateways,
labels,
rules
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ selfLink }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ hostnames }}',
'{{ meshes }}',
'{{ gateways }}',
'{{ labels }}',
'{{ rules }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: description
        value: '{{ description }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: hostnames
        value: '{{ hostnames }}'
      - name: meshes
        value: '{{ meshes }}'
      - name: gateways
        value: '{{ gateways }}'
      - name: labels
        value: '{{ labels }}'
      - name: rules
        value: '{{ rules }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>http_routes</code> resource.

```sql
/*+ update */
UPDATE google.networkservices.http_routes
SET 
name = '{{ name }}',
selfLink = '{{ selfLink }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
hostnames = '{{ hostnames }}',
meshes = '{{ meshes }}',
gateways = '{{ gateways }}',
labels = '{{ labels }}',
rules = '{{ rules }}'
WHERE 
httpRoutesId = '{{ httpRoutesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>http_routes</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkservices.http_routes
WHERE httpRoutesId = '{{ httpRoutesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
