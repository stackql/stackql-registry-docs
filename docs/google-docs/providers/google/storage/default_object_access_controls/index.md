---
title: default_object_access_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - default_object_access_controls
  - storage
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

Creates, updates, deletes, gets or lists a <code>default_object_access_controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>default_object_access_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storage.default_object_access_controls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the access-control entry. |
| <CopyableCode code="bucket" /> | `string` | The name of the bucket. |
| <CopyableCode code="domain" /> | `string` | The domain associated with the entity, if any. |
| <CopyableCode code="email" /> | `string` | The email address associated with the entity, if any. |
| <CopyableCode code="entity" /> | `string` | The entity holding the permission, in one of the following forms: 
- user-userId 
- user-email 
- group-groupId 
- group-email 
- domain-domain 
- project-team-projectId 
- allUsers 
- allAuthenticatedUsers Examples: 
- The user liz@example.com would be user-liz@example.com. 
- The group example@googlegroups.com would be group-example@googlegroups.com. 
- To refer to all members of the Google Apps for Business domain example.com, the entity would be domain-example.com. |
| <CopyableCode code="entityId" /> | `string` | The ID for the entity, if any. |
| <CopyableCode code="etag" /> | `string` | HTTP 1.1 Entity tag for the access-control entry. |
| <CopyableCode code="generation" /> | `string` | The content generation of the object, if applied to an object. |
| <CopyableCode code="kind" /> | `string` | The kind of item this is. For object access control entries, this is always storage#objectAccessControl. |
| <CopyableCode code="object" /> | `string` | The name of the object, if applied to an object. |
| <CopyableCode code="projectTeam" /> | `object` | The project team associated with the entity, if any. |
| <CopyableCode code="role" /> | `string` | The access permission for the entity. |
| <CopyableCode code="selfLink" /> | `string` | The link to this access-control entry. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bucket, entity" /> | Returns the default object ACL entry for the specified entity on the specified bucket. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="bucket" /> | Retrieves default object ACL entries on the specified bucket. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="bucket" /> | Creates a new default object ACL entry on the specified bucket. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bucket, entity" /> | Permanently deletes the default object ACL entry for the specified entity on the specified bucket. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="bucket, entity" /> | Patches a default object ACL entry on the specified bucket. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="bucket, entity" /> | Updates a default object ACL entry on the specified bucket. |

## `SELECT` examples

Retrieves default object ACL entries on the specified bucket.

```sql
SELECT
id,
bucket,
domain,
email,
entity,
entityId,
etag,
generation,
kind,
object,
projectTeam,
role,
selfLink
FROM google.storage.default_object_access_controls
WHERE bucket = '{{ bucket }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>default_object_access_controls</code> resource.

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
INSERT INTO google.storage.default_object_access_controls (
bucket,
bucket,
domain,
email,
entity,
entityId,
etag,
generation,
id,
kind,
object,
projectTeam,
role,
selfLink
)
SELECT 
'{{ bucket }}',
'{{ bucket }}',
'{{ domain }}',
'{{ email }}',
'{{ entity }}',
'{{ entityId }}',
'{{ etag }}',
'{{ generation }}',
'{{ id }}',
'{{ kind }}',
'{{ object }}',
'{{ projectTeam }}',
'{{ role }}',
'{{ selfLink }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: bucket
        value: '{{ bucket }}'
      - name: domain
        value: '{{ domain }}'
      - name: email
        value: '{{ email }}'
      - name: entity
        value: '{{ entity }}'
      - name: entityId
        value: '{{ entityId }}'
      - name: etag
        value: '{{ etag }}'
      - name: generation
        value: '{{ generation }}'
      - name: id
        value: '{{ id }}'
      - name: kind
        value: '{{ kind }}'
      - name: object
        value: '{{ object }}'
      - name: projectTeam
        value:
          - name: projectNumber
            value: '{{ projectNumber }}'
          - name: team
            value: '{{ team }}'
      - name: role
        value: '{{ role }}'
      - name: selfLink
        value: '{{ selfLink }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>default_object_access_controls</code> resource.

```sql
/*+ update */
UPDATE google.storage.default_object_access_controls
SET 
bucket = '{{ bucket }}',
domain = '{{ domain }}',
email = '{{ email }}',
entity = '{{ entity }}',
entityId = '{{ entityId }}',
etag = '{{ etag }}',
generation = '{{ generation }}',
id = '{{ id }}',
kind = '{{ kind }}',
object = '{{ object }}',
projectTeam = '{{ projectTeam }}',
role = '{{ role }}',
selfLink = '{{ selfLink }}'
WHERE 
bucket = '{{ bucket }}'
AND entity = '{{ entity }}';
```

## `DELETE` example

Deletes the specified <code>default_object_access_controls</code> resource.

```sql
/*+ delete */
DELETE FROM google.storage.default_object_access_controls
WHERE bucket = '{{ bucket }}'
AND entity = '{{ entity }}';
```
