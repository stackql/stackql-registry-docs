---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - sqladmin
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

Creates, updates, deletes or gets an <code>user</code> resource or lists <code>users</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sqladmin.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the user in the Cloud SQL instance. Can be omitted for `update` because it is already specified in the URL. |
| <CopyableCode code="dualPasswordType" /> | `string` | Dual password status for the user. |
| <CopyableCode code="etag" /> | `string` | This field is deprecated and will be removed from a future version of the API. |
| <CopyableCode code="host" /> | `string` | Optional. The host from which the user can connect. For `insert` operations, host defaults to an empty string. For `update` operations, host is specified as part of the request URL. The host name cannot be updated after insertion. For a MySQL instance, it's required; for a PostgreSQL or SQL Server instance, it's optional. |
| <CopyableCode code="instance" /> | `string` | The name of the Cloud SQL instance. This does not include the project ID. Can be omitted for `update` because it is already specified on the URL. |
| <CopyableCode code="kind" /> | `string` | This is always `sql#user`. |
| <CopyableCode code="password" /> | `string` | The password for the user. |
| <CopyableCode code="passwordPolicy" /> | `object` | User level password validation policy. |
| <CopyableCode code="project" /> | `string` | The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable. Can be omitted for `update` because it is already specified on the URL. |
| <CopyableCode code="sqlserverUserDetails" /> | `object` | Represents a Sql Server user on the Cloud SQL instance. |
| <CopyableCode code="type" /> | `string` | The user type. It determines the method to authenticate the user during login. The default is the database's built-in user type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instance, name, project" /> | Retrieves a resource containing information about a user. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instance, project" /> | Lists users in the specified Cloud SQL instance. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="instance, project" /> | Creates a new user in a Cloud SQL instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instance, project" /> | Deletes a user from a Cloud SQL instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="instance, project" /> | Updates an existing user in a Cloud SQL instance. |

## `SELECT` examples

Lists users in the specified Cloud SQL instance.

```sql
SELECT
name,
dualPasswordType,
etag,
host,
instance,
kind,
password,
passwordPolicy,
project,
sqlserverUserDetails,
type
FROM google.sqladmin.users
WHERE instance = '{{ instance }}'
AND project = '{{ project }}'; 
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
INSERT INTO google.sqladmin.users (
instance,
project,
kind,
password,
etag,
name,
host,
instance,
project,
type,
sqlserverUserDetails,
passwordPolicy,
dualPasswordType
)
SELECT 
'{{ instance }}',
'{{ project }}',
'{{ kind }}',
'{{ password }}',
'{{ etag }}',
'{{ name }}',
'{{ host }}',
'{{ instance }}',
'{{ project }}',
'{{ type }}',
'{{ sqlserverUserDetails }}',
'{{ passwordPolicy }}',
'{{ dualPasswordType }}'
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
      - name: password
        value: '{{ password }}'
      - name: etag
        value: '{{ etag }}'
      - name: name
        value: '{{ name }}'
      - name: host
        value: '{{ host }}'
      - name: instance
        value: '{{ instance }}'
      - name: project
        value: '{{ project }}'
      - name: type
        value: '{{ type }}'
      - name: sqlserverUserDetails
        value: '{{ sqlserverUserDetails }}'
      - name: passwordPolicy
        value: '{{ passwordPolicy }}'
      - name: dualPasswordType
        value: '{{ dualPasswordType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified user resource.

```sql
DELETE FROM google.sqladmin.users
WHERE instance = '{{ instance }}'
AND project = '{{ project }}';
```
