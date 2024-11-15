---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - databases
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of a database user. |
| <CopyableCode code="access_cert" /> | `string` | Access certificate for TLS client authentication. (Kafka only) |
| <CopyableCode code="access_key" /> | `string` | Access key for TLS client authentication. (Kafka only) |
| <CopyableCode code="mysql_settings" /> | `object` |  |
| <CopyableCode code="password" /> | `string` | A randomly generated password for the database user. |
| <CopyableCode code="role" /> | `string` | A string representing the database user's role. The value will be either "primary" or "normal". |
| <CopyableCode code="settings" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="databases_get_user" /> | `SELECT` | <CopyableCode code="database_cluster_uuid, username" /> | To show information about an existing database user, send a GET request to `/v2/databases/$DATABASE_ID/users/$USERNAME`. Note: User management is not supported for Redis clusters. The response will be a JSON object with a `user` key. This will be set to an object containing the standard database user attributes. For MySQL clusters, additional options will be contained in the `mysql_settings` object. For Kafka clusters, additional options will be contained in the `settings` object. |
| <CopyableCode code="databases_list_users" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To list all of the users for your database cluster, send a GET request to `/v2/databases/$DATABASE_ID/users`. Note: User management is not supported for Redis clusters. The result will be a JSON object with a `users` key. This will be set to an array of database user objects, each of which will contain the standard database user attributes. For MySQL clusters, additional options will be contained in the mysql_settings object. |
| <CopyableCode code="databases_add_user" /> | `INSERT` | <CopyableCode code="database_cluster_uuid, data__name" /> | To add a new database user, send a POST request to `/v2/databases/$DATABASE_ID/users` with the desired username. Note: User management is not supported for Redis clusters. When adding a user to a MySQL cluster, additional options can be configured in the `mysql_settings` object. When adding a user to a Kafka cluster, additional options can be configured in the `settings` object. The response will be a JSON object with a key called `user`. The value of this will be an object that contains the standard attributes associated with a database user including its randomly generated password. |
| <CopyableCode code="databases_delete_user" /> | `DELETE` | <CopyableCode code="database_cluster_uuid, username" /> | To remove a specific database user, send a DELETE request to `/v2/databases/$DATABASE_ID/users/$USERNAME`. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. Note: User management is not supported for Redis clusters. |
| <CopyableCode code="databases_reset_auth" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, username" /> | To reset the password for a database user, send a POST request to `/v2/databases/$DATABASE_ID/users/$USERNAME/reset_auth`. For `mysql` databases, the authentication method can be specifying by including a key in the JSON body called `mysql_settings` with the `auth_plugin` value specified. The response will be a JSON object with a `user` key. This will be set to an object containing the standard database user attributes. |
| <CopyableCode code="databases_update_user" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, username" /> | To update an existing database user, send a PUT request to `/v2/databases/$DATABASE_ID/users/$USERNAME` with the desired settings. **Note**: only `settings` can be updated via this type of request. If you wish to change the name of a user, you must recreate a new user. The response will be a JSON object with a key called `user`. The value of this will be an object that contains the name of the update database user, along with the `settings` object that has been updated. |

## `SELECT` examples

To list all of the users for your database cluster, send a GET request to `/v2/databases/$DATABASE_ID/users`. Note: User management is not supported for Redis clusters. The result will be a JSON object with a `users` key. This will be set to an array of database user objects, each of which will contain the standard database user attributes. For MySQL clusters, additional options will be contained in the mysql_settings object.


```sql
SELECT
name,
access_cert,
access_key,
mysql_settings,
password,
role,
settings
FROM digitalocean.databases.users
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>users</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.databases.users (
data__readonly,
database_cluster_uuid,
data__name
)
SELECT 
'{{ readonly }}',
'{{ database_cluster_uuid }}',
'{{ name }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.databases.users (
data__name,
database_cluster_uuid
)
SELECT 
'{{ name }}',
'{{ database_cluster_uuid }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: users
  props:
    - name: database_cluster_uuid
      value: string
    - name: data__name
      value: string
    - name: readonly
      value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>users</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.databases.users
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}'
AND username = '{{ username }}';
```
