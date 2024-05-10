---
title: location_smbs
hide_title: false
hide_table_of_contents: false
keywords:
  - location_smbs
  - datasync
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


Used to retrieve a list of <code>location_smbs</code> in a region or to create or delete a <code>location_smbs</code> resource, use <code>location_smb</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_smbs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationSMB.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.location_smbs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the SMB location that is created.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
location_arn
FROM aws.datasync.location_smbs
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>location_smb</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- location_smb.iql (required properties only)
INSERT INTO aws.datasync.location_smbs (
 AgentArns,
 User,
 region
)
SELECT 
'{{ AgentArns }}',
 '{{ User }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- location_smb.iql (all properties)
INSERT INTO aws.datasync.location_smbs (
 AgentArns,
 Domain,
 MountOptions,
 Password,
 ServerHostname,
 Subdirectory,
 User,
 Tags,
 region
)
SELECT 
 '{{ AgentArns }}',
 '{{ Domain }}',
 '{{ MountOptions }}',
 '{{ Password }}',
 '{{ ServerHostname }}',
 '{{ Subdirectory }}',
 '{{ User }}',
 '{{ Tags }}',
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
  - name: location_smb
    props:
      - name: AgentArns
        value:
          - '{{ AgentArns[0] }}'
      - name: Domain
        value: '{{ Domain }}'
      - name: MountOptions
        value:
          Version: '{{ Version }}'
      - name: Password
        value: '{{ Password }}'
      - name: ServerHostname
        value: '{{ ServerHostname }}'
      - name: Subdirectory
        value: '{{ Subdirectory }}'
      - name: User
        value: '{{ User }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.datasync.location_smbs
WHERE data__Identifier = '<LocationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>location_smbs</code> resource, the following permissions are required:

### Create
```json
datasync:CreateLocationSmb,
datasync:DescribeLocationSmb,
datasync:ListTagsForResource,
datasync:TagResource
```

### Delete
```json
datasync:DeleteLocation
```

### List
```json
datasync:ListLocations
```

