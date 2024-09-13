---
title: envgroups
hide_title: false
hide_table_of_contents: false
keywords:
  - envgroups
  - apigee
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

Creates, updates, deletes or gets an <code>envgroup</code> resource or lists <code>envgroups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>envgroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.envgroups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | ID of the environment group. |
| <CopyableCode code="createdAt" /> | `string` | Output only. The time at which the environment group was created as milliseconds since epoch. |
| <CopyableCode code="hostnames" /> | `array` | Required. Host names for this environment group. |
| <CopyableCode code="lastModifiedAt" /> | `string` | Output only. The time at which the environment group was last updated as milliseconds since epoch. |
| <CopyableCode code="state" /> | `string` | Output only. State of the environment group. Values other than ACTIVE means the resource is not ready to use. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_envgroups_get" /> | `SELECT` | <CopyableCode code="envgroupsId, organizationsId" /> | Gets an environment group. |
| <CopyableCode code="organizations_envgroups_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all environment groups. |
| <CopyableCode code="organizations_envgroups_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a new environment group. |
| <CopyableCode code="organizations_envgroups_delete" /> | `DELETE` | <CopyableCode code="envgroupsId, organizationsId" /> | Deletes an environment group. |
| <CopyableCode code="organizations_envgroups_patch" /> | `UPDATE` | <CopyableCode code="envgroupsId, organizationsId" /> | Updates an environment group. |

## `SELECT` examples

Lists all environment groups.

```sql
SELECT
name,
createdAt,
hostnames,
lastModifiedAt,
state
FROM google.apigee.envgroups
WHERE organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>envgroups</code> resource.

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
INSERT INTO google.apigee.envgroups (
organizationsId,
lastModifiedAt,
state,
name,
hostnames,
createdAt
)
SELECT 
'{{ organizationsId }}',
'{{ lastModifiedAt }}',
'{{ state }}',
'{{ name }}',
'{{ hostnames }}',
'{{ createdAt }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: lastModifiedAt
        value: '{{ lastModifiedAt }}'
      - name: state
        value: '{{ state }}'
      - name: name
        value: '{{ name }}'
      - name: hostnames
        value: '{{ hostnames }}'
      - name: createdAt
        value: '{{ createdAt }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a envgroup only if the necessary resources are available.

```sql
UPDATE google.apigee.envgroups
SET 
lastModifiedAt = '{{ lastModifiedAt }}',
state = '{{ state }}',
name = '{{ name }}',
hostnames = '{{ hostnames }}',
createdAt = '{{ createdAt }}'
WHERE 
envgroupsId = '{{ envgroupsId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `DELETE` example

Deletes the specified envgroup resource.

```sql
DELETE FROM google.apigee.envgroups
WHERE envgroupsId = '{{ envgroupsId }}'
AND organizationsId = '{{ organizationsId }}';
```
