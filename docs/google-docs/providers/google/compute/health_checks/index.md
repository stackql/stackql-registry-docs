---
title: health_checks
hide_title: false
hide_table_of_contents: false
keywords:
  - health_checks
  - compute
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

Creates, updates, deletes, gets or lists a <code>health_checks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.health_checks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. For example, a name that is 1-63 characters long, matches the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="checkIntervalSec" /> | `integer` | How often (in seconds) to send a health check. The default value is 5 seconds. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in 3339 text format. |
| <CopyableCode code="grpcHealthCheck" /> | `object` |  |
| <CopyableCode code="healthyThreshold" /> | `integer` | A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2. |
| <CopyableCode code="http2HealthCheck" /> | `object` |  |
| <CopyableCode code="httpHealthCheck" /> | `object` |  |
| <CopyableCode code="httpsHealthCheck" /> | `object` |  |
| <CopyableCode code="kind" /> | `string` | Type of the resource. |
| <CopyableCode code="logConfig" /> | `object` | Configuration of logging on a health check. If logging is enabled, logs will be exported to Stackdriver. |
| <CopyableCode code="region" /> | `string` | [Output Only] Region where the health check resides. Not applicable to global health checks. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="sourceRegions" /> | `array` | The list of cloud regions from which health checks are performed. If any regions are specified, then exactly 3 regions should be specified. The region names must be valid names of Google Cloud regions. This can only be set for global health check. If this list is non-empty, then there are restrictions on what other health check fields are supported and what other resources can use this health check: - SSL, HTTP2, and GRPC protocols are not supported. - The TCP request field is not supported. - The proxyHeader field for HTTP, HTTPS, and TCP is not supported. - The checkIntervalSec field must be at least 30. - The health check cannot be used with BackendService nor with managed instance group auto-healing.  |
| <CopyableCode code="sslHealthCheck" /> | `object` |  |
| <CopyableCode code="tcpHealthCheck" /> | `object` |  |
| <CopyableCode code="timeoutSec" /> | `integer` | How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec. |
| <CopyableCode code="type" /> | `string` | Specifies the type of the healthCheck, either TCP, SSL, HTTP, HTTPS, HTTP2 or GRPC. Exactly one of the protocol-specific health check fields must be specified, which must match type field. |
| <CopyableCode code="unhealthyThreshold" /> | `integer` | A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="healthCheck, project" /> | Returns the specified HealthCheck resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of HealthCheck resources available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a HealthCheck resource in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="healthCheck, project" /> | Deletes the specified HealthCheck resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="healthCheck, project" /> | Updates a HealthCheck resource in the specified project using the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="healthCheck, project" /> | Updates a HealthCheck resource in the specified project using the data included in the request. |

## `SELECT` examples

Retrieves the list of HealthCheck resources available to the specified project.

```sql
SELECT
id,
name,
description,
checkIntervalSec,
creationTimestamp,
grpcHealthCheck,
healthyThreshold,
http2HealthCheck,
httpHealthCheck,
httpsHealthCheck,
kind,
logConfig,
region,
selfLink,
sourceRegions,
sslHealthCheck,
tcpHealthCheck,
timeoutSec,
type,
unhealthyThreshold
FROM google.compute.health_checks
WHERE project = '{{ project }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>health_checks</code> resource.

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
INSERT INTO google.compute.health_checks (
project,
name,
description,
checkIntervalSec,
timeoutSec,
unhealthyThreshold,
healthyThreshold,
type,
tcpHealthCheck,
sslHealthCheck,
httpHealthCheck,
httpsHealthCheck,
http2HealthCheck,
grpcHealthCheck,
sourceRegions,
region,
logConfig
)
SELECT 
'{{ project }}',
'{{ name }}',
'{{ description }}',
'{{ checkIntervalSec }}',
'{{ timeoutSec }}',
'{{ unhealthyThreshold }}',
'{{ healthyThreshold }}',
'{{ type }}',
'{{ tcpHealthCheck }}',
'{{ sslHealthCheck }}',
'{{ httpHealthCheck }}',
'{{ httpsHealthCheck }}',
'{{ http2HealthCheck }}',
'{{ grpcHealthCheck }}',
'{{ sourceRegions }}',
'{{ region }}',
'{{ logConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: id
      value: string
    - name: creationTimestamp
      value: string
    - name: name
      value: string
    - name: description
      value: string
    - name: checkIntervalSec
      value: integer
    - name: timeoutSec
      value: integer
    - name: unhealthyThreshold
      value: integer
    - name: healthyThreshold
      value: integer
    - name: type
      value: string
    - name: tcpHealthCheck
      value:
        - name: port
          value: integer
        - name: portName
          value: string
        - name: portSpecification
          value: string
        - name: request
          value: string
        - name: response
          value: string
        - name: proxyHeader
          value: string
    - name: sslHealthCheck
      value:
        - name: port
          value: integer
        - name: portName
          value: string
        - name: portSpecification
          value: string
        - name: request
          value: string
        - name: response
          value: string
        - name: proxyHeader
          value: string
    - name: httpHealthCheck
      value:
        - name: port
          value: integer
        - name: portName
          value: string
        - name: portSpecification
          value: string
        - name: host
          value: string
        - name: requestPath
          value: string
        - name: proxyHeader
          value: string
        - name: response
          value: string
    - name: httpsHealthCheck
      value:
        - name: port
          value: integer
        - name: portName
          value: string
        - name: portSpecification
          value: string
        - name: host
          value: string
        - name: requestPath
          value: string
        - name: proxyHeader
          value: string
        - name: response
          value: string
    - name: http2HealthCheck
      value:
        - name: port
          value: integer
        - name: portName
          value: string
        - name: portSpecification
          value: string
        - name: host
          value: string
        - name: requestPath
          value: string
        - name: proxyHeader
          value: string
        - name: response
          value: string
    - name: grpcHealthCheck
      value:
        - name: port
          value: integer
        - name: portName
          value: string
        - name: portSpecification
          value: string
        - name: grpcServiceName
          value: string
    - name: sourceRegions
      value:
        - string
    - name: selfLink
      value: string
    - name: region
      value: string
    - name: logConfig
      value:
        - name: enable
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>health_checks</code> resource.

```sql
/*+ update */
UPDATE google.compute.health_checks
SET 
name = '{{ name }}',
description = '{{ description }}',
checkIntervalSec = '{{ checkIntervalSec }}',
timeoutSec = '{{ timeoutSec }}',
unhealthyThreshold = '{{ unhealthyThreshold }}',
healthyThreshold = '{{ healthyThreshold }}',
type = '{{ type }}',
tcpHealthCheck = '{{ tcpHealthCheck }}',
sslHealthCheck = '{{ sslHealthCheck }}',
httpHealthCheck = '{{ httpHealthCheck }}',
httpsHealthCheck = '{{ httpsHealthCheck }}',
http2HealthCheck = '{{ http2HealthCheck }}',
grpcHealthCheck = '{{ grpcHealthCheck }}',
sourceRegions = '{{ sourceRegions }}',
region = '{{ region }}',
logConfig = '{{ logConfig }}'
WHERE 
healthCheck = '{{ healthCheck }}'
AND project = '{{ project }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>health_checks</code> resource.

```sql
/*+ update */
REPLACE google.compute.health_checks
SET 
name = '{{ name }}',
description = '{{ description }}',
checkIntervalSec = '{{ checkIntervalSec }}',
timeoutSec = '{{ timeoutSec }}',
unhealthyThreshold = '{{ unhealthyThreshold }}',
healthyThreshold = '{{ healthyThreshold }}',
type = '{{ type }}',
tcpHealthCheck = '{{ tcpHealthCheck }}',
sslHealthCheck = '{{ sslHealthCheck }}',
httpHealthCheck = '{{ httpHealthCheck }}',
httpsHealthCheck = '{{ httpsHealthCheck }}',
http2HealthCheck = '{{ http2HealthCheck }}',
grpcHealthCheck = '{{ grpcHealthCheck }}',
sourceRegions = '{{ sourceRegions }}',
region = '{{ region }}',
logConfig = '{{ logConfig }}'
WHERE 
healthCheck = '{{ healthCheck }}'
AND project = '{{ project }}';
```

## `DELETE` example

Deletes the specified <code>health_checks</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.health_checks
WHERE healthCheck = '{{ healthCheck }}'
AND project = '{{ project }}';
```
