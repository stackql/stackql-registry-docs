---
title: functions
hide_title: false
hide_table_of_contents: false
keywords:
  - functions
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


Used to retrieve a list of <code>functions</code> in a region or to create or delete a <code>functions</code> resource, use <code>function</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudFront::Function</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.functions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="function_arn" /></td><td><code>string</code></td><td></td></tr>
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
function_arn
FROM aws.cloudfront.functions
;
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>function</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- function.iql (required properties only)
INSERT INTO aws.cloudfront.functions (
 FunctionCode,
 FunctionConfig,
 Name,
 region
)
SELECT 
'{{ FunctionCode }}',
 '{{ FunctionConfig }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- function.iql (all properties)
INSERT INTO aws.cloudfront.functions (
 AutoPublish,
 FunctionCode,
 FunctionConfig,
 FunctionMetadata,
 Name,
 region
)
SELECT 
 '{{ AutoPublish }}',
 '{{ FunctionCode }}',
 '{{ FunctionConfig }}',
 '{{ FunctionMetadata }}',
 '{{ Name }}',
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
  - name: function
    props:
      - name: AutoPublish
        value: '{{ AutoPublish }}'
      - name: FunctionCode
        value: '{{ FunctionCode }}'
      - name: FunctionConfig
        value:
          Comment: '{{ Comment }}'
          Runtime: '{{ Runtime }}'
          KeyValueStoreAssociations:
            - KeyValueStoreARN: '{{ KeyValueStoreARN }}'
      - name: FunctionMetadata
        value:
          FunctionARN: '{{ FunctionARN }}'
      - name: Name
        value: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cloudfront.functions
WHERE data__Identifier = '<FunctionARN>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>functions</code> resource, the following permissions are required:

### Create
```json
cloudfront:CreateFunction,
cloudfront:PublishFunction,
cloudfront:DescribeFunction
```

### Delete
```json
cloudfront:DeleteFunction,
cloudfront:DescribeFunction
```

### List
```json
cloudfront:ListFunctions
```

