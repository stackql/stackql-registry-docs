---
title: inputs
hide_title: false
hide_table_of_contents: false
keywords:
  - inputs
  - iotevents
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

Creates, updates, deletes or gets an <code>input</code> resource or lists <code>inputs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into ITE. This is done by sending messages as *inputs* to ITE. For more information, see &#91;How to Use&#93;(https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.inputs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="input_definition" /></td><td><code>object</code></td><td>The definition of the input.</td></tr>
<tr><td><CopyableCode code="input_description" /></td><td><code>string</code></td><td>A brief description of the input.</td></tr>
<tr><td><CopyableCode code="input_name" /></td><td><code>string</code></td><td>The name of the input.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.<br />For more information, see &#91;Tag&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html"><code>AWS::IoTEvents::Input</code></a>.

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
    <td><CopyableCode code="InputDefinition, region" /></td>
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
Gets all <code>inputs</code> in a region.
```sql
SELECT
region,
input_definition,
input_description,
input_name,
tags
FROM aws.iotevents.inputs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>input</code>.
```sql
SELECT
region,
input_definition,
input_description,
input_name,
tags
FROM aws.iotevents.inputs
WHERE region = 'us-east-1' AND data__Identifier = '<InputName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>input</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotevents.inputs (
 InputDefinition,
 region
)
SELECT 
'{{ InputDefinition }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotevents.inputs (
 InputDefinition,
 InputDescription,
 InputName,
 Tags,
 region
)
SELECT 
 '{{ InputDefinition }}',
 '{{ InputDescription }}',
 '{{ InputName }}',
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
  - name: input
    props:
      - name: InputDefinition
        value:
          Attributes:
            - JsonPath: '{{ JsonPath }}'
      - name: InputDescription
        value: '{{ InputDescription }}'
      - name: InputName
        value: '{{ InputName }}'
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
DELETE FROM aws.iotevents.inputs
WHERE data__Identifier = '<InputName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>inputs</code> resource, the following permissions are required:

### Create
```json
iotevents:CreateInput,
iotevents:TagResource,
iotevents:DescribeInput,
iotevents:ListTagsForResource
```

### Read
```json
iotevents:DescribeInput,
iotevents:ListTagsForResource
```

### Update
```json
iotevents:UpdateInput,
iotevents:DescribeInput,
iotevents:ListTagsForResource,
iotevents:UntagResource,
iotevents:TagResource
```

### Delete
```json
iotevents:DeleteInput,
iotevents:DescribeInput
```

### List
```json
iotevents:ListInputs
```
