---
title: stages
hide_title: false
hide_table_of_contents: false
keywords:
  - stages
  - stage
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

Creates, updates, deletes, gets or lists a <code>stages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.stage.stages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="cloud" /> | `string` | Cloud provider; always NULL for an internal stage. |
| <CopyableCode code="comment" /> | `string` | Specifies a comment for the stage. |
| <CopyableCode code="created_on" /> | `string` | Date and time when the stage was created. |
| <CopyableCode code="credentials" /> | `object` | Specifies the credentials of the stage. |
| <CopyableCode code="directory_table" /> | `object` | Directory table parameters of the stage. |
| <CopyableCode code="encryption" /> | `object` | Encryption parameters of the stage. |
| <CopyableCode code="endpoint" /> | `string` | The S3-compatible API endpoint associated with the stage; always NULL for stages that are not S3-compatible. |
| <CopyableCode code="has_credentials" /> | `boolean` | Indicates that the external stage has access credentials; always false for an internal stage. |
| <CopyableCode code="has_encryption_key" /> | `boolean` | Indicates that the external stage contains encrypted files; always false for an internal stage. |
| <CopyableCode code="kind" /> | `string` | Specifies whether the stage is permanent or temporary. |
| <CopyableCode code="owner" /> | `string` | Role that owns the stage. |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the object, either ROLE or DATABASE_ROLE. If a Snowflake Native App owns the object, the value is APPLICATION. Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| <CopyableCode code="region" /> | `string` | Region where the stage is located. |
| <CopyableCode code="storage_integration" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="url" /> | `string` | URL for the external stage; blank for an internal stage. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_stage" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Fetch a stage using the describe command output. |
| <CopyableCode code="list_stages" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | <CopyableCode code="like" /> | Lists stages under the database and schema, with show options as query parameters. |
| <CopyableCode code="create_stage" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__name, endpoint" /> | <CopyableCode code="createMode" /> | Create a stage, with standard create modifiers as query parameters. See the Stage component definition for what is required to be provided in the request body. |
| <CopyableCode code="delete_stage" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a stage with the stage name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful. |

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
    defaultValue="list_stages"
    values={[
        { label: 'list_stages', value: 'list_stages' },
        { label: 'fetch_stage', value: 'fetch_stage' }
    ]
}>
<TabItem value="list_stages">

Lists stages under the database and schema, with show options as query parameters.

```sql
SELECT
name,
cloud,
comment,
created_on,
credentials,
directory_table,
encryption,
endpoint,
has_credentials,
has_encryption_key,
kind,
owner,
owner_role_type,
region,
storage_integration,
url
FROM snowflake.stage.stages
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
<TabItem value="fetch_stage">

Fetch a stage using the describe command output.

```sql
SELECT
name,
cloud,
comment,
created_on,
credentials,
directory_table,
encryption,
endpoint,
has_credentials,
has_encryption_key,
kind,
owner,
owner_role_type,
region,
storage_integration,
url
FROM snowflake.stage.stages
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>stages</code> resource.

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
INSERT INTO snowflake.stage.stages (
data__name,
data__kind,
data__url,
data__endpoint,
data__storage_integration,
data__comment,
data__credentials,
data__encryption,
data__directory_table,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ kind }}',
'{{ url }}',
'{{ endpoint }}',
'{{ storage_integration }}',
'{{ comment }}',
'{{ credentials }}',
'{{ encryption }}',
'{{ directory_table }}',
'{{ database_name }}',
'{{ schema_name }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.stage.stages (
data__name,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: stages
  props:
    - name: database_name
      value: string
    - name: schema_name
      value: string
    - name: data__name
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
      description: >-
        A Snowflake object identifier. If the identifier contains spaces or
        special characters, the entire string must be enclosed in double quotes.
        Identifiers enclosed in double quotes are also case-sensitive.
    - name: kind
      value: string
      description: Specifies whether the stage is permanent or temporary.
    - name: url
      value: string
      description: URL for the external stage; blank for an internal stage.
    - name: endpoint
      value: string
      description: >-
        The S3-compatible API endpoint associated with the stage; always NULL
        for stages that are not S3-compatible.
    - name: storage_integration
      value: string
      description: >-
        A Snowflake object identifier. If the identifier contains spaces or
        special characters, the entire string must be enclosed in double quotes.
        Identifiers enclosed in double quotes are also case-sensitive.
    - name: comment
      value: string
      description: Specifies a comment for the stage.
    - name: credentials
      value:
        - name: credential_type
          value: string
          description: Type of the credential, can be either AWS or AZURE.
      description: Specifies the credentials of the stage.
    - name: encryption
      value:
        - name: type
          value: string
          description: Specifies the encryption type used.
        - name: master_key
          value: string
          description: >-
            Specifies the client-side master key used to encrypt the files in
            the bucket. The master key must be a 128-bit or 256-bit key in
            Base64-encoded form.
        - name: kms_key_id
          value: string
          description: >-
            Optionally specifies the ID for the KMS-managed key used to encrypt
            files unloaded into the bucket.
      description: Encryption parameters of the stage.
    - name: directory_table
      value:
        - name: enable
          value: boolean
          description: >-
            Specifies whether to add a directory table to the stage. When the
            value is TRUE, a directory table is created with the stage.
        - name: refresh_on_create
          value: boolean
          description: >-
            Specifies whether to automatically refresh the directory table
            metadata once, immediately after the stage is created.
        - name: auto_refresh
          value: boolean
          description: >-
            Specifies whether Snowflake should enable triggering automatic
            refreshes of the directory table metadata when new or updated data
            files are available in the named external stage specified in the URL
            value.
        - name: notification_integration
          value: string
          description: >-
            Specifies the name of the notification integration used to
            automatically refresh the directory table metadata.
      description: Directory table parameters of the stage.

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>stages</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.stage.stages
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
