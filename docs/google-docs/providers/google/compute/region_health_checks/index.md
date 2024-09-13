
---
title: region_health_checks
hide_title: false
hide_table_of_contents: false
keywords:
  - region_health_checks
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

Creates, updates, deletes or gets an <code>region_health_check</code> resource or lists <code>region_health_checks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_health_checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_health_checks" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="healthCheck, project, region" /> | Returns the specified HealthCheck resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves the list of HealthCheck resources available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a HealthCheck resource in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="healthCheck, project, region" /> | Deletes the specified HealthCheck resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="healthCheck, project, region" /> | Updates a HealthCheck resource in the specified project using the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="healthCheck, project, region" /> | Updates a HealthCheck resource in the specified project using the data included in the request. |

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
FROM google.compute.region_health_checks
WHERE project = '{{ project }}'
AND region = '{{ region }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_health_checks</code> resource.

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
INSERT INTO google.compute.region_health_checks (
project,
region,
kind,
id,
creationTimestamp,
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
selfLink,
region,
logConfig
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
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
'{{ selfLink }}',
'{{ region }}',
'{{ logConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: kind
        value: '{{ kind }}'
      - name: id
        value: '{{ id }}'
      - name: creationTimestamp
        value: '{{ creationTimestamp }}'
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: checkIntervalSec
        value: '{{ checkIntervalSec }}'
      - name: timeoutSec
        value: '{{ timeoutSec }}'
      - name: unhealthyThreshold
        value: '{{ unhealthyThreshold }}'
      - name: healthyThreshold
        value: '{{ healthyThreshold }}'
      - name: type
        value: '{{ type }}'
      - name: tcpHealthCheck
        value: '{{ tcpHealthCheck }}'
      - name: sslHealthCheck
        value: '{{ sslHealthCheck }}'
      - name: httpHealthCheck
        value: '{{ httpHealthCheck }}'
      - name: httpsHealthCheck
        value: '{{ httpsHealthCheck }}'
      - name: http2HealthCheck
        value: '{{ http2HealthCheck }}'
      - name: grpcHealthCheck
        value: '{{ grpcHealthCheck }}'
      - name: sourceRegions
        value: '{{ sourceRegions }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: region
        value: '{{ region }}'
      - name: logConfig
        value: '{{ logConfig }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a region_health_check only if the necessary resources are available.

```sql
UPDATE google.compute.region_health_checks
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
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
selfLink = '{{ selfLink }}',
region = '{{ region }}',
logConfig = '{{ logConfig }}'
WHERE 
healthCheck = '{{ healthCheck }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```

## `DELETE` example

Deletes the specified region_health_check resource.

```sql
DELETE FROM google.compute.region_health_checks
WHERE healthCheck = '{{ healthCheck }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
