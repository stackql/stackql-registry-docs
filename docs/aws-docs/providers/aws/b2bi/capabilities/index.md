---
title: capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - capabilities
  - b2bi
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


Used to retrieve a list of <code>capabilities</code> in a region or to create or delete a <code>capabilities</code> resource, use <code>capability</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::B2BI::Capability Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.b2bi.capabilities" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="capability_id" /></td><td><code>string</code></td><td></td></tr>
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
capability_id
FROM aws.b2bi.capabilities
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>capability</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- capability.iql (required properties only)
INSERT INTO aws.b2bi.capabilities (
 Configuration,
 Name,
 Type,
 region
)
SELECT 
'{{ Configuration }}',
 '{{ Name }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- capability.iql (all properties)
INSERT INTO aws.b2bi.capabilities (
 Configuration,
 InstructionsDocuments,
 Name,
 Tags,
 Type,
 region
)
SELECT 
 '{{ Configuration }}',
 '{{ InstructionsDocuments }}',
 '{{ Name }}',
 '{{ Tags }}',
 '{{ Type }}',
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
  - name: capability
    props:
      - name: Configuration
        value: null
      - name: InstructionsDocuments
        value:
          - BucketName: '{{ BucketName }}'
            Key: '{{ Key }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.b2bi.capabilities
WHERE data__Identifier = '<CapabilityId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>capabilities</code> resource, the following permissions are required:

### Create
```json
b2bi:CreateCapability,
b2bi:TagResource,
events:ListRules,
events:PutRule,
events:PutTargets,
logs:CreateLogDelivery,
logs:CreateLogGroup,
logs:CreateLogStream,
logs:DescribeLogGroups,
logs:DescribeLogStreams,
logs:DescribeResourcePolicies,
logs:ListLogDeliveries,
logs:PutLogEvents,
logs:PutResourcePolicy,
s3:GetObject,
s3:ListBucket
```

### Delete
```json
b2bi:DeleteCapability
```

### List
```json
b2bi:ListCapabilities
```

