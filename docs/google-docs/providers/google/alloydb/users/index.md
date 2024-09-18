---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - alloydb
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

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.alloydb.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the resource in the form of projects/{project}/locations/{location}/cluster/{cluster}/users/{user}. |
| <CopyableCode code="databaseRoles" /> | `array` | Optional. List of database roles this user has. The database role strings are subject to the PostgreSQL naming conventions. |
| <CopyableCode code="keepExtraRoles" /> | `boolean` | Input only. If the user already exists and it has additional roles, keep them granted. |
| <CopyableCode code="password" /> | `string` | Input only. Password for the user. |
| <CopyableCode code="userType" /> | `string` | Optional. Type of this user. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, projectsId, usersId" /> | Gets details of a single User. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Lists Users in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Creates a new User in a given project, location, and cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clustersId, locationsId, projectsId, usersId" /> | Deletes a single User. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="clustersId, locationsId, projectsId, usersId" /> | Updates the parameters of a single User. |

## `SELECT` examples

Lists Users in a given project and location.

```sql
SELECT
name,
databaseRoles,
keepExtraRoles,
password,
userType
FROM google.alloydb.users
WHERE clustersId = '{{ clustersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>users</code> resource.

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
INSERT INTO google.alloydb.users (
clustersId,
locationsId,
projectsId,
password,
databaseRoles,
userType,
keepExtraRoles
)
SELECT 
'{{ clustersId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ password }}',
'{{ databaseRoles }}',
'{{ userType }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
password: string
databaseRoles:
  - type: string
userType: string
keepExtraRoles: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>users</code> resource.

```sql
/*+ update */
UPDATE google.alloydb.users
SET 
password = '{{ password }}',
databaseRoles = '{{ databaseRoles }}',
userType = '{{ userType }}',
keepExtraRoles = true|false
WHERE 
clustersId = '{{ clustersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND usersId = '{{ usersId }}';
```

## `DELETE` example

Deletes the specified <code>users</code> resource.

```sql
/*+ delete */
DELETE FROM google.alloydb.users
WHERE clustersId = '{{ clustersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND usersId = '{{ usersId }}';
```
