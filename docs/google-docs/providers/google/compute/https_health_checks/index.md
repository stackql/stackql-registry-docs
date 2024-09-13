
---
title: https_health_checks
hide_title: false
hide_table_of_contents: false
keywords:
  - https_health_checks
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

Creates, updates, deletes or gets an <code>https_health_check</code> resource or lists <code>https_health_checks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>https_health_checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.https_health_checks" /></td></tr>
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
| <CopyableCode code="host" /> | `string` | The value of the host header in the HTTPS health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used. |
| <CopyableCode code="kind" /> | `string` | Type of the resource. |
| <CopyableCode code="port" /> | `integer` | The TCP port number for the HTTPS health check request. The default value is 443. |
| <CopyableCode code="requestPath" /> | `string` | The request path of the HTTPS health check request. The default value is "/". Must comply with RFC3986. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="timeoutSec" /> | `integer` | How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have a greater value than checkIntervalSec. |
| <CopyableCode code="unhealthyThreshold" /> | `integer` | A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="httpsHealthCheck, project" /> | Returns the specified HttpsHealthCheck resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of HttpsHealthCheck resources available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a HttpsHealthCheck resource in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="httpsHealthCheck, project" /> | Deletes the specified HttpsHealthCheck resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="httpsHealthCheck, project" /> | Updates a HttpsHealthCheck resource in the specified project using the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="httpsHealthCheck, project" /> | Updates a HttpsHealthCheck resource in the specified project using the data included in the request. |

## `SELECT` examples

Retrieves the list of HttpsHealthCheck resources available to the specified project.

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
FROM google.compute.https_health_checks
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>https_health_checks</code> resource.

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
INSERT INTO google.compute.https_health_checks (
project,
kind,
id,
creationTimestamp,
name,
description,
host,
requestPath,
port,
checkIntervalSec,
timeoutSec,
unhealthyThreshold,
healthyThreshold,
selfLink
)
SELECT 
'{{ project }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ host }}',
'{{ requestPath }}',
'{{ port }}',
'{{ checkIntervalSec }}',
'{{ timeoutSec }}',
'{{ unhealthyThreshold }}',
'{{ healthyThreshold }}',
'{{ selfLink }}'
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
      - name: host
        value: '{{ host }}'
      - name: requestPath
        value: '{{ requestPath }}'
      - name: port
        value: '{{ port }}'
      - name: checkIntervalSec
        value: '{{ checkIntervalSec }}'
      - name: timeoutSec
        value: '{{ timeoutSec }}'
      - name: unhealthyThreshold
        value: '{{ unhealthyThreshold }}'
      - name: healthyThreshold
        value: '{{ healthyThreshold }}'
      - name: selfLink
        value: '{{ selfLink }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a https_health_check only if the necessary resources are available.

```sql
UPDATE google.compute.https_health_checks
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
host = '{{ host }}',
requestPath = '{{ requestPath }}',
port = '{{ port }}',
checkIntervalSec = '{{ checkIntervalSec }}',
timeoutSec = '{{ timeoutSec }}',
unhealthyThreshold = '{{ unhealthyThreshold }}',
healthyThreshold = '{{ healthyThreshold }}',
selfLink = '{{ selfLink }}'
WHERE 
httpsHealthCheck = '{{ httpsHealthCheck }}'
AND project = '{{ project }}';
```

## `DELETE` example

Deletes the specified https_health_check resource.

```sql
DELETE FROM google.compute.https_health_checks
WHERE httpsHealthCheck = '{{ httpsHealthCheck }}'
AND project = '{{ project }}';
```
