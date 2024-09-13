
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

Creates, updates, deletes or gets an <code>backend_bucket</code> resource or lists <code>backend_buckets</code> in a region

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
| <CopyableCode code="set_edge_security_policy" /> | `EXEC` | <CopyableCode code="backendBucket, project" /> | Sets the edge security policy for the specified backend bucket. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="backendBucket, project" /> | Updates the specified BackendBucket resource with the data included in the request. |

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
kind,
id,
creationTimestamp,
name,
description,
selfLink,
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
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ selfLink }}',
'{{ bucketName }}',
true|false,
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
      - name: selfLink
        value: '{{ selfLink }}'
      - name: bucketName
        value: '{{ bucketName }}'
      - name: enableCdn
        value: '{{ enableCdn }}'
      - name: cdnPolicy
        value: '{{ cdnPolicy }}'
      - name: customResponseHeaders
        value: '{{ customResponseHeaders }}'
      - name: edgeSecurityPolicy
        value: '{{ edgeSecurityPolicy }}'
      - name: compressionMode
        value: '{{ compressionMode }}'
      - name: usedBy
        value: '{{ usedBy }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a backend_bucket only if the necessary resources are available.

```sql
UPDATE google.compute.backend_buckets
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
selfLink = '{{ selfLink }}',
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

Deletes the specified backend_bucket resource.

```sql
DELETE FROM google.compute.backend_buckets
WHERE backendBucket = '{{ backendBucket }}'
AND project = '{{ project }}';
```
