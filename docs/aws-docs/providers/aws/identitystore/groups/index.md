---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - identitystore
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

Creates, updates, deletes or gets a <code>group</code> resource or lists <code>groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IdentityStore::Group</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.identitystore.groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A string containing the description of the group.</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>A string containing the name of the group. This value is commonly displayed when the group is referenced.</td></tr>
<tr><td><CopyableCode code="group_id" /></td><td><code>string</code></td><td>The unique identifier for a group in the identity store.</td></tr>
<tr><td><CopyableCode code="identity_store_id" /></td><td><code>string</code></td><td>The globally unique identifier for the identity store.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html"><code>AWS::IdentityStore::Group</code></a>.

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
    <td><CopyableCode code="IdentityStoreId, DisplayName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
Gets all <code>groups</code> in a region.
```sql
SELECT
region,
description,
display_name,
group_id,
identity_store_id
FROM aws.identitystore.groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>group</code>.
```sql
SELECT
region,
description,
display_name,
group_id,
identity_store_id
FROM aws.identitystore.groups
WHERE region = 'us-east-1' AND data__Identifier = '<GroupId>|<IdentityStoreId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.identitystore.groups (
 DisplayName,
 IdentityStoreId,
 region
)
SELECT 
'{{ DisplayName }}',
 '{{ IdentityStoreId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.identitystore.groups (
 Description,
 DisplayName,
 IdentityStoreId,
 region
)
SELECT 
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ IdentityStoreId }}',
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
  - name: group
    props:
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: IdentityStoreId
        value: '{{ IdentityStoreId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.identitystore.groups
WHERE data__Identifier = '<GroupId|IdentityStoreId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>groups</code> resource, the following permissions are required:

### Create
```json
identitystore:CreateGroup,
identitystore:DescribeGroup
```

### Read
```json
identitystore:DescribeGroup
```

### Update
```json
identitystore:DescribeGroup,
identitystore:UpdateGroup
```

### Delete
```json
identitystore:DescribeGroup,
identitystore:DeleteGroup
```

### List
```json
identitystore:ListGroups
```
