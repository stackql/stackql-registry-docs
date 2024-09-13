---
title: attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - attachments
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

Creates, updates, deletes or gets an <code>attachment</code> resource or lists <code>attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.attachments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | ID of the environment group attachment. |
| <CopyableCode code="createdAt" /> | `string` | Output only. The time at which the environment group attachment was created as milliseconds since epoch. |
| <CopyableCode code="environment" /> | `string` | Required. ID of the attached environment. |
| <CopyableCode code="environmentGroupId" /> | `string` | Output only. ID of the environment group. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_envgroups_attachments_get" /> | `SELECT` | <CopyableCode code="attachmentsId, envgroupsId, organizationsId" /> | Gets an environment group attachment. |
| <CopyableCode code="organizations_envgroups_attachments_list" /> | `SELECT` | <CopyableCode code="envgroupsId, organizationsId" /> | Lists all attachments of an environment group. |
| <CopyableCode code="organizations_instances_attachments_get" /> | `SELECT` | <CopyableCode code="attachmentsId, instancesId, organizationsId" /> | Gets an attachment. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_instances_attachments_list" /> | `SELECT` | <CopyableCode code="instancesId, organizationsId" /> | Lists all attachments to an instance. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_envgroups_attachments_create" /> | `INSERT` | <CopyableCode code="envgroupsId, organizationsId" /> | Creates a new attachment of an environment to an environment group. |
| <CopyableCode code="organizations_instances_attachments_create" /> | `INSERT` | <CopyableCode code="instancesId, organizationsId" /> | Creates a new attachment of an environment to an instance. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_envgroups_attachments_delete" /> | `DELETE` | <CopyableCode code="attachmentsId, envgroupsId, organizationsId" /> | Deletes an environment group attachment. |
| <CopyableCode code="organizations_instances_attachments_delete" /> | `DELETE` | <CopyableCode code="attachmentsId, instancesId, organizationsId" /> | Deletes an attachment. **Note:** Not supported for Apigee hybrid. |

## `SELECT` examples

Lists all attachments of an environment group.

```sql
SELECT
name,
createdAt,
environment,
environmentGroupId
FROM google.apigee.attachments
WHERE envgroupsId = '{{ envgroupsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>attachments</code> resource.

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
INSERT INTO google.apigee.attachments (
envgroupsId,
organizationsId,
createdAt,
environmentGroupId,
environment,
name
)
SELECT 
'{{ envgroupsId }}',
'{{ organizationsId }}',
'{{ createdAt }}',
'{{ environmentGroupId }}',
'{{ environment }}',
'{{ name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: createdAt
        value: '{{ createdAt }}'
      - name: environmentGroupId
        value: '{{ environmentGroupId }}'
      - name: environment
        value: '{{ environment }}'
      - name: name
        value: '{{ name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified attachment resource.

```sql
DELETE FROM google.apigee.attachments
WHERE attachmentsId = '{{ attachmentsId }}'
AND envgroupsId = '{{ envgroupsId }}'
AND organizationsId = '{{ organizationsId }}';
```
