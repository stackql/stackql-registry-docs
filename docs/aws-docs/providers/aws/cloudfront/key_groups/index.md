---
title: key_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - key_groups
  - cloudfront
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

Creates, updates, deletes or gets a <code>key_group</code> resource or lists <code>key_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudFront::KeyGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.key_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="key_group_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

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
    <td><CopyableCode code="KeyGroupConfig, region" /></td>
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
Gets all <code>key_groups</code> in a region.
```sql
SELECT
region,
id,
key_group_config,
last_modified_time
FROM aws.cloudfront.key_groups
;
```
Gets all properties from an individual <code>key_group</code>.
```sql
SELECT
region,
id,
key_group_config,
last_modified_time
FROM aws.cloudfront.key_groups
WHERE data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>key_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudfront.key_groups (
 KeyGroupConfig,
 region
)
SELECT 
'{{ KeyGroupConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudfront.key_groups (
 KeyGroupConfig,
 region
)
SELECT 
 '{{ KeyGroupConfig }}',
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
  - name: key_group
    props:
      - name: KeyGroupConfig
        value:
          Comment: '{{ Comment }}'
          Items:
            - '{{ Items[0] }}'
          Name: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cloudfront.key_groups
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>key_groups</code> resource, the following permissions are required:

### Create
```json
cloudfront:CreateKeyGroup
```

### Delete
```json
cloudfront:DeleteKeyGroup,
cloudfront:GetKeyGroup
```

### List
```json
cloudfront:ListKeyGroups
```

### Read
```json
cloudfront:GetKeyGroup
```

### Update
```json
cloudfront:UpdateKeyGroup,
cloudfront:GetKeyGroup
```

