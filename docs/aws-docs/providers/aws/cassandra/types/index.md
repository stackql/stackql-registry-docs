---
title: types
hide_title: false
hide_table_of_contents: false
keywords:
  - types
  - cassandra
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>type</code> resource or lists <code>types</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Cassandra::Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cassandra.types" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="keyspace_name" /></td><td><code>string</code></td><td>Name of the Keyspace which contains the User-Defined Type.</td></tr>
<tr><td><CopyableCode code="type_name" /></td><td><code>string</code></td><td>Name of the User-Defined Type.</td></tr>
<tr><td><CopyableCode code="fields" /></td><td><code>array</code></td><td>Field definitions of the User-Defined Type</td></tr>
<tr><td><CopyableCode code="direct_referring_tables" /></td><td><code>array</code></td><td>List of Tables that directly reference the User-Defined Type in their columns.</td></tr>
<tr><td><CopyableCode code="direct_parent_types" /></td><td><code>array</code></td><td>List of parent User-Defined Types that directly reference the User-Defined Type in their fields.</td></tr>
<tr><td><CopyableCode code="max_nesting_depth" /></td><td><code>integer</code></td><td>Maximum nesting depth of the User-Defined Type across the field types.</td></tr>
<tr><td><CopyableCode code="last_modified_timestamp" /></td><td><code>number</code></td><td>Timestamp of the last time the User-Defined Type's meta data was modified.</td></tr>
<tr><td><CopyableCode code="keyspace_arn" /></td><td><code>string</code></td><td>ARN of the Keyspace which contains the User-Defined Type.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-type.html"><code>AWS::Cassandra::Type</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="KeyspaceName, TypeName, Fields, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>types</code> in a region.
```sql
SELECT
region,
keyspace_name,
type_name,
fields,
direct_referring_tables,
direct_parent_types,
max_nesting_depth,
last_modified_timestamp,
keyspace_arn
FROM aws.cassandra.types
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>type</code>.
```sql
SELECT
region,
keyspace_name,
type_name,
fields,
direct_referring_tables,
direct_parent_types,
max_nesting_depth,
last_modified_timestamp,
keyspace_arn
FROM aws.cassandra.types
WHERE region = 'us-east-1' AND data__Identifier = '<KeyspaceName>|<TypeName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>type</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.cassandra.types (
 KeyspaceName,
 TypeName,
 Fields,
 region
)
SELECT 
'{{ KeyspaceName }}',
 '{{ TypeName }}',
 '{{ Fields }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cassandra.types (
 KeyspaceName,
 TypeName,
 Fields,
 region
)
SELECT 
 '{{ KeyspaceName }}',
 '{{ TypeName }}',
 '{{ Fields }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: type
    props:
      - name: KeyspaceName
        value: '{{ KeyspaceName }}'
      - name: TypeName
        value: '{{ TypeName }}'
      - name: Fields
        value:
          - FieldName: '{{ FieldName }}'
            FieldType: '{{ FieldType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cassandra.types
WHERE data__Identifier = '<KeyspaceName|TypeName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>types</code> resource, the following permissions are required:

### Create
```json
cassandra:Create,
cassandra:Select
```

### Read
```json
cassandra:Select
```

### Delete
```json
cassandra:Drop,
cassandra:Select
```

### List
```json
cassandra:Select
```
