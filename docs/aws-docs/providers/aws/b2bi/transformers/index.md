---
title: transformers
hide_title: false
hide_table_of_contents: false
keywords:
  - transformers
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

Creates, updates, deletes or gets a <code>transformer</code> resource or lists <code>transformers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transformers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::B2BI::Transformer Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.b2bi.transformers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="edi_type" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="file_format" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="mapping_template" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sample_document" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="transformer_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="transformer_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="EdiType, FileFormat, MappingTemplate, Name, Status, region" /></td>
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
Gets all <code>transformers</code> in a region.
```sql
SELECT
region,
created_at,
edi_type,
file_format,
mapping_template,
modified_at,
name,
sample_document,
status,
tags,
transformer_arn,
transformer_id
FROM aws.b2bi.transformers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>transformer</code>.
```sql
SELECT
region,
created_at,
edi_type,
file_format,
mapping_template,
modified_at,
name,
sample_document,
status,
tags,
transformer_arn,
transformer_id
FROM aws.b2bi.transformers
WHERE region = 'us-east-1' AND data__Identifier = '<TransformerId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transformer</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.b2bi.transformers (
 EdiType,
 FileFormat,
 MappingTemplate,
 Name,
 Status,
 region
)
SELECT 
'{{ EdiType }}',
 '{{ FileFormat }}',
 '{{ MappingTemplate }}',
 '{{ Name }}',
 '{{ Status }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.b2bi.transformers (
 EdiType,
 FileFormat,
 MappingTemplate,
 Name,
 SampleDocument,
 Status,
 Tags,
 region
)
SELECT 
 '{{ EdiType }}',
 '{{ FileFormat }}',
 '{{ MappingTemplate }}',
 '{{ Name }}',
 '{{ SampleDocument }}',
 '{{ Status }}',
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
  - name: transformer
    props:
      - name: EdiType
        value: null
      - name: FileFormat
        value: '{{ FileFormat }}'
      - name: MappingTemplate
        value: '{{ MappingTemplate }}'
      - name: Name
        value: '{{ Name }}'
      - name: SampleDocument
        value: '{{ SampleDocument }}'
      - name: Status
        value: '{{ Status }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.b2bi.transformers
WHERE data__Identifier = '<TransformerId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>transformers</code> resource, the following permissions are required:

### Create
```json
b2bi:CreateTransformer,
b2bi:TagResource,
b2bi:UpdateTransformer,
logs:CreateLogDelivery,
logs:CreateLogGroup,
logs:CreateLogStream,
logs:DescribeLogGroups,
logs:DescribeLogStreams,
logs:DescribeResourcePolicies,
logs:ListLogDeliveries,
logs:PutLogEvents,
logs:PutResourcePolicy
```

### Read
```json
b2bi:GetTransformer,
b2bi:ListTagsForResource
```

### Update
```json
b2bi:TagResource,
b2bi:UntagResource,
b2bi:UpdateTransformer
```

### Delete
```json
b2bi:DeleteTransformer,
logs:DeleteLogDelivery,
logs:ListLogDeliveries
```

### List
```json
b2bi:ListTransformers
```

