---
title: http_health_checks
hide_title: false
hide_table_of_contents: false
keywords:
  - http_health_checks
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

Creates, updates, deletes, gets or lists a <code>http_health_checks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>http_health_checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.http_health_checks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="checkIntervalSec" /> | `integer` | How often (in seconds) to send a health check. The default value is 5 seconds. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="healthyThreshold" /> | `integer` | A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2. |
| <CopyableCode code="host" /> | `string` | The value of the host header in the HTTP health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#httpHealthCheck for HTTP health checks. |
| <CopyableCode code="port" /> | `integer` | The TCP port number for the HTTP health check request. The default value is 80. |
| <CopyableCode code="requestPath" /> | `string` | The request path of the HTTP health check request. The default value is /. This field does not support query parameters. Must comply with RFC3986. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="timeoutSec" /> | `integer` | How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec. |
| <CopyableCode code="unhealthyThreshold" /> | `integer` | A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="httpHealthCheck, project" /> | Returns the specified HttpHealthCheck resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of HttpHealthCheck resources available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a HttpHealthCheck resource in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="httpHealthCheck, project" /> | Deletes the specified HttpHealthCheck resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="httpHealthCheck, project" /> | Updates a HttpHealthCheck resource in the specified project using the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="httpHealthCheck, project" /> | Updates a HttpHealthCheck resource in the specified project using the data included in the request. |

## `SELECT` examples

Retrieves the list of HttpHealthCheck resources available to the specified project.

```sql
SELECT
id,
name,
description,
checkIntervalSec,
creationTimestamp,
healthyThreshold,
host,
kind,
port,
requestPath,
selfLink,
timeoutSec,
unhealthyThreshold
FROM google.compute.http_health_checks
WHERE project = '{{ project }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>http_health_checks</code> resource.

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
INSERT INTO google.compute.http_health_checks (
project,
name,
description,
host,
requestPath,
port,
checkIntervalSec,
timeoutSec,
unhealthyThreshold,
healthyThreshold
)
SELECT 
'{{ project }}',
'{{ name }}',
'{{ description }}',
'{{ host }}',
'{{ requestPath }}',
'{{ port }}',
'{{ checkIntervalSec }}',
'{{ timeoutSec }}',
'{{ unhealthyThreshold }}',
'{{ healthyThreshold }}'
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
    - name: host
      value: string
    - name: requestPath
      value: string
    - name: port
      value: integer
    - name: checkIntervalSec
      value: integer
    - name: timeoutSec
      value: integer
    - name: unhealthyThreshold
      value: integer
    - name: healthyThreshold
      value: integer
    - name: selfLink
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>http_health_checks</code> resource.

```sql
/*+ update */
UPDATE google.compute.http_health_checks
SET 
name = '{{ name }}',
description = '{{ description }}',
host = '{{ host }}',
requestPath = '{{ requestPath }}',
port = '{{ port }}',
checkIntervalSec = '{{ checkIntervalSec }}',
timeoutSec = '{{ timeoutSec }}',
unhealthyThreshold = '{{ unhealthyThreshold }}',
healthyThreshold = '{{ healthyThreshold }}'
WHERE 
httpHealthCheck = '{{ httpHealthCheck }}'
AND project = '{{ project }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>http_health_checks</code> resource.

```sql
/*+ update */
REPLACE google.compute.http_health_checks
SET 
name = '{{ name }}',
description = '{{ description }}',
host = '{{ host }}',
requestPath = '{{ requestPath }}',
port = '{{ port }}',
checkIntervalSec = '{{ checkIntervalSec }}',
timeoutSec = '{{ timeoutSec }}',
unhealthyThreshold = '{{ unhealthyThreshold }}',
healthyThreshold = '{{ healthyThreshold }}'
WHERE 
httpHealthCheck = '{{ httpHealthCheck }}'
AND project = '{{ project }}';
```

## `DELETE` example

Deletes the specified <code>http_health_checks</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.http_health_checks
WHERE httpHealthCheck = '{{ httpHealthCheck }}'
AND project = '{{ project }}';
```
