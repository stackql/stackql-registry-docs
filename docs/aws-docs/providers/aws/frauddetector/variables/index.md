---
title: variables
hide_title: false
hide_table_of_contents: false
keywords:
  - variables
  - frauddetector
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

Creates, updates, deletes or gets a <code>variable</code> resource or lists <code>variables</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>variables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema for a Variable in Amazon Fraud Detector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.frauddetector.variables" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the variable.</td></tr>
<tr><td><CopyableCode code="data_source" /></td><td><code>string</code></td><td>The source of the data.</td></tr>
<tr><td><CopyableCode code="data_type" /></td><td><code>string</code></td><td>The data type.</td></tr>
<tr><td><CopyableCode code="default_value" /></td><td><code>string</code></td><td>The default value for the variable when no value is received.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags associated with this variable.</td></tr>
<tr><td><CopyableCode code="variable_type" /></td><td><code>string</code></td><td>The variable type. For more information see https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the variable.</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td>The time when the variable was created.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>The time when the variable was last updated.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html"><code>AWS::FraudDetector::Variable</code></a>.

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
    <td><CopyableCode code="DataType, DataSource, DefaultValue, Name, region" /></td>
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
Gets all <code>variables</code> in a region.
```sql
SELECT
region,
name,
data_source,
data_type,
default_value,
description,
tags,
variable_type,
arn,
created_time,
last_updated_time
FROM aws.frauddetector.variables
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>variable</code>.
```sql
SELECT
region,
name,
data_source,
data_type,
default_value,
description,
tags,
variable_type,
arn,
created_time,
last_updated_time
FROM aws.frauddetector.variables
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>variable</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.frauddetector.variables (
 Name,
 DataSource,
 DataType,
 DefaultValue,
 region
)
SELECT 
'{{ Name }}',
 '{{ DataSource }}',
 '{{ DataType }}',
 '{{ DefaultValue }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.frauddetector.variables (
 Name,
 DataSource,
 DataType,
 DefaultValue,
 Description,
 Tags,
 VariableType,
 region
)
SELECT 
 '{{ Name }}',
 '{{ DataSource }}',
 '{{ DataType }}',
 '{{ DefaultValue }}',
 '{{ Description }}',
 '{{ Tags }}',
 '{{ VariableType }}',
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
  - name: variable
    props:
      - name: Name
        value: '{{ Name }}'
      - name: DataSource
        value: '{{ DataSource }}'
      - name: DataType
        value: '{{ DataType }}'
      - name: DefaultValue
        value: '{{ DefaultValue }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VariableType
        value: '{{ VariableType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.frauddetector.variables
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>variables</code> resource, the following permissions are required:

### Create
```json
frauddetector:GetVariables,
frauddetector:CreateVariable,
frauddetector:ListTagsForResource,
frauddetector:TagResource
```

### Read
```json
frauddetector:GetVariables,
frauddetector:ListTagsForResource
```

### Update
```json
frauddetector:GetVariables,
frauddetector:UpdateVariable,
frauddetector:ListTagsForResource,
frauddetector:TagResource,
frauddetector:UntagResource
```

### Delete
```json
frauddetector:GetVariables,
frauddetector:DeleteVariable
```

### List
```json
frauddetector:GetVariables,
frauddetector:ListTagsForResource
```
