---
title: grpc_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - grpc_routes
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

Creates, updates, deletes, gets or lists a <code>grpc_routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grpc_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkservices.grpc_routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the GrpcRoute resource. It matches pattern `projects/*/locations/global/grpcRoutes/` |
| <CopyableCode code="description" /> | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="gateways" /> | `array` | Optional. Gateways defines a list of gateways this GrpcRoute is attached to, as one of the routing rules to route the requests served by the gateway. Each gateway reference should match the pattern: `projects/*/locations/global/gateways/` |
| <CopyableCode code="hostnames" /> | `array` | Required. Service hostnames with an optional port for which this route describes traffic. Format: [:] Hostname is the fully qualified domain name of a network host. This matches the RFC 1123 definition of a hostname with 2 notable exceptions: - IPs are not allowed. - A hostname may be prefixed with a wildcard label (`*.`). The wildcard label must appear by itself as the first label. Hostname can be "precise" which is a domain name without the terminating dot of a network host (e.g. `foo.example.com`) or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. `*.example.com`). Note that as per RFC1035 and RFC1123, a label must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character. No other punctuation is allowed. The routes associated with a Mesh or Gateway must have unique hostnames. If you attempt to attach multiple routes with conflicting hostnames, the configuration will be rejected. For example, while it is acceptable for routes for the hostnames `*.foo.bar.com` and `*.bar.com` to be associated with the same route, it is not possible to associate two routes both with `*.bar.com` or both with `bar.com`. If a port is specified, then gRPC clients must use the channel URI with the port to match this rule (i.e. "xds:///service:123"), otherwise they must supply the URI without a port (i.e. "xds:///service"). |
| <CopyableCode code="labels" /> | `object` | Optional. Set of label tags associated with the GrpcRoute resource. |
| <CopyableCode code="meshes" /> | `array` | Optional. Meshes defines a list of meshes this GrpcRoute is attached to, as one of the routing rules to route the requests served by the mesh. Each mesh reference should match the pattern: `projects/*/locations/global/meshes/` |
| <CopyableCode code="rules" /> | `array` | Required. A list of detailed rules defining how to route traffic. Within a single GrpcRoute, the GrpcRoute.RouteAction associated with the first matching GrpcRoute.RouteRule will be executed. At least one rule must be supplied. |
| <CopyableCode code="selfLink" /> | `string` | Output only. Server-defined URL of this resource |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="grpcRoutesId, locationsId, projectsId" /> | Gets details of a single GrpcRoute. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists GrpcRoutes in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new GrpcRoute in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="grpcRoutesId, locationsId, projectsId" /> | Deletes a single GrpcRoute. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="grpcRoutesId, locationsId, projectsId" /> | Updates the parameters of a single GrpcRoute. |

## `SELECT` examples

Lists GrpcRoutes in a given project and location.

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
FROM google.networkservices.grpc_routes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>grpc_routes</code> resource.

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
INSERT INTO google.networkservices.grpc_routes (
locationsId,
projectsId,
name,
labels,
description,
hostnames,
meshes,
gateways,
rules
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ labels }}',
'{{ description }}',
'{{ hostnames }}',
'{{ meshes }}',
'{{ gateways }}',
'{{ rules }}'
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
    - name: labels
      value: object
    - name: description
      value: string
    - name: hostnames
      value:
        - string
    - name: meshes
      value:
        - string
    - name: gateways
      value:
        - string
    - name: rules
      value:
        - - name: matches
            value:
              - - name: method
                  value:
                    - name: type
                      value: string
                    - name: grpcService
                      value: string
                    - name: grpcMethod
                      value: string
                    - name: caseSensitive
                      value: boolean
                - name: headers
                  value:
                    - - name: type
                        value: string
                      - name: key
                        value: string
                      - name: value
                        value: string
          - name: action
            value:
              - name: destinations
                value:
                  - - name: serviceName
                      value: string
                    - name: weight
                      value: integer
              - name: faultInjectionPolicy
                value:
                  - name: delay
                    value:
                      - name: fixedDelay
                        value: string
                      - name: percentage
                        value: integer
                  - name: abort
                    value:
                      - name: httpStatus
                        value: integer
                      - name: percentage
                        value: integer
              - name: timeout
                value: string
              - name: retryPolicy
                value:
                  - name: retryConditions
                    value:
                      - string
                  - name: numRetries
                    value: integer
              - name: statefulSessionAffinity
                value:
                  - name: cookieTtl
                    value: string
              - name: idleTimeout
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>grpc_routes</code> resource.

```sql
/*+ update */
UPDATE google.networkservices.grpc_routes
SET 
name = '{{ name }}',
labels = '{{ labels }}',
description = '{{ description }}',
hostnames = '{{ hostnames }}',
meshes = '{{ meshes }}',
gateways = '{{ gateways }}',
rules = '{{ rules }}'
WHERE 
grpcRoutesId = '{{ grpcRoutesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>grpc_routes</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkservices.grpc_routes
WHERE grpcRoutesId = '{{ grpcRoutesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
