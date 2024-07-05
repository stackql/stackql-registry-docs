---
title: contact_flow_modules
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_flow_modules
  - connect
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

Creates, updates, deletes or gets a <code>contact_flow_module</code> resource or lists <code>contact_flow_modules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_flow_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::ContactFlowModule.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.contact_flow_modules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance (ARN).</td></tr>
<tr><td><CopyableCode code="contact_flow_module_arn" /></td><td><code>string</code></td><td>The identifier of the contact flow module (ARN).</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the contact flow module.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>string</code></td><td>The content of the contact flow module in JSON format.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the contact flow module.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the contact flow module.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the contact flow module.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
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
    <td><CopyableCode code="InstanceArn, Name, Content, region" /></td>
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
Gets all <code>contact_flow_modules</code> in a region.
```sql
SELECT
region,
instance_arn,
contact_flow_module_arn,
name,
content,
description,
state,
status,
tags
FROM aws.connect.contact_flow_modules
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>contact_flow_module</code>.
```sql
SELECT
region,
instance_arn,
contact_flow_module_arn,
name,
content,
description,
state,
status,
tags
FROM aws.connect.contact_flow_modules
WHERE region = 'us-east-1' AND data__Identifier = '<ContactFlowModuleArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>contact_flow_module</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.contact_flow_modules (
 InstanceArn,
 Name,
 Content,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ Name }}',
 '{{ Content }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.contact_flow_modules (
 InstanceArn,
 Name,
 Content,
 Description,
 State,
 Tags,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ Name }}',
 '{{ Content }}',
 '{{ Description }}',
 '{{ State }}',
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
  - name: contact_flow_module
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: Content
        value: '{{ Content }}'
      - name: Description
        value: '{{ Description }}'
      - name: State
        value: '{{ State }}'
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
DELETE FROM aws.connect.contact_flow_modules
WHERE data__Identifier = '<ContactFlowModuleArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>contact_flow_modules</code> resource, the following permissions are required:

### Create
```json
connect:CreateContactFlowModule,
connect:TagResource
```

### Read
```json
connect:DescribeContactFlowModule
```

### Delete
```json
connect:DeleteContactFlowModule,
connect:UntagResource
```

### Update
```json
connect:UpdateContactFlowModuleMetadata,
connect:UpdateContactFlowModuleContent,
connect:TagResource,
connect:UntagResource
```

### List
```json
connect:ListContactFlowModules
```

