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


Used to retrieve a list of <code>inputs</code> in a region or to create or delete a <code>inputs</code> resource, use <code>input</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into AWS IoT Events. This is done by sending messages as *inputs* to AWS IoT Events. For more information, see &#91;How to Use AWS IoT Events&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;iotevents&#x2F;latest&#x2F;developerguide&#x2F;how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.inputs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="input_name" /></td><td><code>string</code></td><td>The name of the input.</td></tr>
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
input_name
FROM aws.iotevents.inputs
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>input</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- input.iql (required properties only)
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
-- input.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
iotevents:DeleteInput,
iotevents:DescribeInput
```

### List
```json
iotevents:ListInputs
```

