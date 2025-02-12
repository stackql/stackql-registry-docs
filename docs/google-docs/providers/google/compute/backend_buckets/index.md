---
title: backend_buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - backend_buckets
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

Creates, updates, deletes, gets or lists a <code>backend_buckets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backend_buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.backend_buckets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] Unique identifier for the resource; defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional textual description of the resource; provided by the client when the resource is created. |
| <CopyableCode code="bucketName" /> | `string` | Cloud Storage bucket name. |
| <CopyableCode code="cdnPolicy" /> | `object` | Message containing Cloud CDN configuration for a backend bucket. |
| <CopyableCode code="compressionMode" /> | `string` | Compress text responses using Brotli or gzip compression, based on the client's Accept-Encoding header. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="customResponseHeaders" /> | `array` | Headers that the Application Load Balancer should add to proxied responses. |
| <CopyableCode code="edgeSecurityPolicy" /> | `string` | [Output Only] The resource URL for the edge security policy associated with this backend bucket. |
| <CopyableCode code="enableCdn" /> | `boolean` | If true, enable Cloud CDN for this BackendBucket. |
| <CopyableCode code="kind" /> | `string` | Type of the resource. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="usedBy" /> | `array` | [Output Only] List of resources referencing that backend bucket. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backendBucket, project" /> | Returns the specified BackendBucket resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of BackendBucket resources available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a BackendBucket resource in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backendBucket, project" /> | Deletes the specified BackendBucket resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="backendBucket, project" /> | Updates the specified BackendBucket resource with the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="backendBucket, project" /> | Updates the specified BackendBucket resource with the data included in the request. |
| <CopyableCode code="set_edge_security_policy" /> | `EXEC` | <CopyableCode code="backendBucket, project" /> | Sets the edge security policy for the specified backend bucket. |

## `SELECT` examples

Retrieves the list of BackendBucket resources available to the specified project.

```sql
SELECT
id,
name,
description,
bucketName,
cdnPolicy,
compressionMode,
creationTimestamp,
customResponseHeaders,
edgeSecurityPolicy,
enableCdn,
kind,
selfLink,
usedBy
FROM google.compute.backend_buckets
WHERE project = '{{ project }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backend_buckets</code> resource.

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
INSERT INTO google.compute.backend_buckets (
project,
name,
description,
bucketName,
enableCdn,
cdnPolicy,
customResponseHeaders,
edgeSecurityPolicy,
compressionMode,
usedBy
)
SELECT 
'{{ project }}',
'{{ name }}',
'{{ description }}',
'{{ bucketName }}',
{{ enableCdn }},
'{{ cdnPolicy }}',
'{{ customResponseHeaders }}',
'{{ edgeSecurityPolicy }}',
'{{ compressionMode }}',
'{{ usedBy }}'
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
    - name: selfLink
      value: string
    - name: bucketName
      value: string
    - name: enableCdn
      value: boolean
    - name: cdnPolicy
      value:
        - name: signedUrlKeyNames
          value:
            - string
        - name: signedUrlCacheMaxAgeSec
          value: string
        - name: requestCoalescing
          value: boolean
        - name: cacheMode
          value: string
        - name: defaultTtl
          value: integer
        - name: maxTtl
          value: integer
        - name: clientTtl
          value: integer
        - name: negativeCaching
          value: boolean
        - name: negativeCachingPolicy
          value:
            - - name: code
                value: integer
              - name: ttl
                value: integer
        - name: bypassCacheOnRequestHeaders
          value:
            - - name: headerName
                value: string
        - name: serveWhileStale
          value: integer
        - name: cacheKeyPolicy
          value:
            - name: queryStringWhitelist
              value:
                - string
            - name: includeHttpHeaders
              value:
                - string
    - name: customResponseHeaders
      value:
        - string
    - name: edgeSecurityPolicy
      value: string
    - name: compressionMode
      value: string
    - name: usedBy
      value:
        - - name: reference
            value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>backend_buckets</code> resource.

```sql
/*+ update */
UPDATE google.compute.backend_buckets
SET 
name = '{{ name }}',
description = '{{ description }}',
bucketName = '{{ bucketName }}',
enableCdn = true|false,
cdnPolicy = '{{ cdnPolicy }}',
customResponseHeaders = '{{ customResponseHeaders }}',
edgeSecurityPolicy = '{{ edgeSecurityPolicy }}',
compressionMode = '{{ compressionMode }}',
usedBy = '{{ usedBy }}'
WHERE 
backendBucket = '{{ backendBucket }}'
AND project = '{{ project }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>backend_buckets</code> resource.

```sql
/*+ update */
REPLACE google.compute.backend_buckets
SET 
name = '{{ name }}',
description = '{{ description }}',
bucketName = '{{ bucketName }}',
enableCdn = true|false,
cdnPolicy = '{{ cdnPolicy }}',
customResponseHeaders = '{{ customResponseHeaders }}',
edgeSecurityPolicy = '{{ edgeSecurityPolicy }}',
compressionMode = '{{ compressionMode }}',
usedBy = '{{ usedBy }}'
WHERE 
backendBucket = '{{ backendBucket }}'
AND project = '{{ project }}';
```

## `DELETE` example

Deletes the specified <code>backend_buckets</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.backend_buckets
WHERE backendBucket = '{{ backendBucket }}'
AND project = '{{ project }}';
```
