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


Used to retrieve a list of <code>transformers</code> in a region or to create or delete a <code>transformers</code> resource, use <code>transformer</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transformers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::B2BI::Transformer Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.b2bi.transformers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
transformer_id
FROM aws.b2bi.transformers
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>transformer</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- transformer.iql (required properties only)
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
-- transformer.iql (all properties)
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

## `DELETE` Example

```sql
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

