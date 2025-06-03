---
title: external_volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - external_volumes
  - external_volume
  - snowflake
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage snowflake resources using SQL
custom_edit_url: null
image: /img/providers/snowflake/stackql-snowflake-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>external_volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>external_volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.external_volume.external_volumes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | String that specifies the identifier (the name) for the external volume; must be unique in your account. |
| <CopyableCode code="allow_writes" /> | `boolean` | Specifies whether write operations are allowed for the external volume; must be set to TRUE for Iceberg tables that use Snowflake as the catalog. |
| <CopyableCode code="comment" /> | `string` | String (literal) that specifies a comment for the external volume. |
| <CopyableCode code="created_on" /> | `string` | Date and time when the external volume was created. |
| <CopyableCode code="owner" /> | `string` | Role that owns the external volume |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the external volume |
| <CopyableCode code="storage_locations" /> | `array` | Set of named cloud storage locations in different regions and, optionally, cloud platforms. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_external_volume" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | - | Fetch an external volume |
| <CopyableCode code="list_external_volumes" /> | `SELECT` | <CopyableCode code="endpoint" /> | <CopyableCode code="like" /> | List external volumes |
| <CopyableCode code="create_external_volume" /> | `INSERT` | <CopyableCode code="data__name, data__storage_locations, endpoint" /> | <CopyableCode code="createMode" /> | Create an external volume |
| <CopyableCode code="delete_external_volume" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete an external volume |
| <CopyableCode code="undrop_external_volume" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | - | Undrop an external volume |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |

</details>

## `SELECT` examples

<Tabs
    defaultValue="list_external_volumes"
    values={[
        { label: 'list_external_volumes', value: 'list_external_volumes' },
        { label: 'fetch_external_volume', value: 'fetch_external_volume' }
    ]
}>
<TabItem value="list_external_volumes">

List external volumes

```sql
SELECT
name,
allow_writes,
comment,
created_on,
owner,
owner_role_type,
storage_locations
FROM snowflake.external_volume.external_volumes
WHERE endpoint = '{{ endpoint }}';
```
</TabItem>
<TabItem value="fetch_external_volume">

Fetch an external volume

```sql
SELECT
name,
allow_writes,
comment,
created_on,
owner,
owner_role_type,
storage_locations
FROM snowflake.external_volume.external_volumes
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>external_volumes</code> resource.

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
INSERT INTO snowflake.external_volume.external_volumes (
data__name,
data__storage_locations,
data__allow_writes,
data__comment,
endpoint
)
SELECT 
'{{ name }}',
'{{ storage_locations }}',
{{ allow_writes }},
'{{ comment }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.external_volume.external_volumes (
data__name,
data__storage_locations,
endpoint
)
SELECT 
'{{ name }}',
'{{ storage_locations }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
# Description fields below are for documentation purposes only and are not required in the manifest
- name: external_volumes
  props:
    - name: endpoint
      value: string
      description: Required parameter for the external_volumes resource.
    - name: name
      value: string
      description: >-
        String that specifies the identifier (the name) for the external volume;
        must be unique in your account. (Required parameter for the
        external_volumes resource.)
    - name: storage_locations
      value:
        - name: name
          value: string
        - name: storage_provider
          value: string
          description: >-
            Specifies the cloud storage provider that stores your data files.
            (valid values: 'S3', 'S3GOV', 'GCS', 'AZURE')
      description: >-
        Set of named cloud storage locations in different regions and,
        optionally, cloud platforms. (Required parameter for the
        external_volumes resource.)
    - name: allow_writes
      value: boolean
      description: >-
        Specifies whether write operations are allowed for the external volume;
        must be set to TRUE for Iceberg tables that use Snowflake as the
        catalog.
    - name: comment
      value: string
      description: String (literal) that specifies a comment for the external volume.
```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>external_volumes</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.external_volume.external_volumes
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
