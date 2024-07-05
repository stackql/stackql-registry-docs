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

Creates, updates, deletes or gets a <code>function</code> resource or lists <code>functions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudFront::Function</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.functions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="auto_publish" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="function_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="function_code" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="function_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="function_metadata" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stage" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, FunctionConfig, FunctionCode, region" /></td>
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
Gets all <code>functions</code> in a region.
```sql
SELECT
region,
auto_publish,
function_arn,
function_code,
function_config,
function_metadata,
name,
stage
FROM aws.cloudfront.functions
;
```
Gets all properties from an individual <code>function</code>.
```sql
SELECT
region,
auto_publish,
function_arn,
function_code,
function_config,
function_metadata,
name,
stage
FROM aws.cloudfront.functions
WHERE data__Identifier = '<FunctionARN>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>function</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
cloudfront:DescribeFunction,
cloudfront:GetFunction
```

### Update
```json
cloudfront:UpdateFunction,
cloudfront:PublishFunction,
cloudfront:DescribeFunction
```

