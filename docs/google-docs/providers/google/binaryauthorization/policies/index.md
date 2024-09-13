---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - binaryauthorization
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

Creates, updates, deletes or gets an <code>policy</code> resource or lists <code>policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.binaryauthorization.policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the Binary Authorization platform policy, in the form of `projects/*/platforms/*/policies/*`. |
| <CopyableCode code="description" /> | `string` | Optional. A description comment about the policy. |
| <CopyableCode code="etag" /> | `string` | Optional. Used to prevent updating the policy when another request has updated it since it was retrieved. |
| <CopyableCode code="gkePolicy" /> | `object` | A Binary Authorization policy for a GKE cluster. This is one type of policy that can occur as a `PlatformPolicy`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the policy was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="platformsId, policiesId, projectsId" /> | Gets a platform policy. Returns `NOT_FOUND` if the policy doesn't exist. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="platformsId, projectsId" /> | Lists platform policies owned by a project in the specified platform. Returns `INVALID_ARGUMENT` if the project or the platform doesn't exist. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="platformsId, projectsId" /> | Creates a platform policy, and returns a copy of it. Returns `NOT_FOUND` if the project or platform doesn't exist, `INVALID_ARGUMENT` if the request is malformed, `ALREADY_EXISTS` if the policy already exists, and `INVALID_ARGUMENT` if the policy contains a platform-specific policy that does not match the platform value specified in the URL. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="platformsId, policiesId, projectsId" /> | Deletes a platform policy. Returns `NOT_FOUND` if the policy doesn't exist. |
| <CopyableCode code="evaluate" /> | `EXEC` | <CopyableCode code="policiesId, projectsId" /> | Evaluates a Kubernetes object versus a GKE platform policy. Returns `NOT_FOUND` if the policy doesn't exist, `INVALID_ARGUMENT` if the policy or request is malformed and `PERMISSION_DENIED` if the client does not have sufficient permissions. |
| <CopyableCode code="replace_platform_policy" /> | `EXEC` | <CopyableCode code="platformsId, policiesId, projectsId" /> | Replaces a platform policy. Returns `NOT_FOUND` if the policy doesn't exist. |

## `SELECT` examples

Lists platform policies owned by a project in the specified platform. Returns `INVALID_ARGUMENT` if the project or the platform doesn't exist.

```sql
SELECT
name,
description,
etag,
gkePolicy,
updateTime
FROM google.binaryauthorization.policies
WHERE platformsId = '{{ platformsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policies</code> resource.

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
INSERT INTO google.binaryauthorization.policies (
platformsId,
projectsId,
name,
description,
gkePolicy,
updateTime,
etag
)
SELECT 
'{{ platformsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ gkePolicy }}',
'{{ updateTime }}',
'{{ etag }}'
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
      - name: description
        value: '{{ description }}'
      - name: gkePolicy
        value: '{{ gkePolicy }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: etag
        value: '{{ etag }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified policy resource.

```sql
DELETE FROM google.binaryauthorization.policies
WHERE platformsId = '{{ platformsId }}'
AND policiesId = '{{ policiesId }}'
AND projectsId = '{{ projectsId }}';
```
