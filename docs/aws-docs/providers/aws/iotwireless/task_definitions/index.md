---
title: task_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - task_definitions
  - iotwireless
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

Creates, updates, deletes or gets a <code>task_definition</code> resource or lists <code>task_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a gateway task definition.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.task_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the new resource.</td></tr>
<tr><td><CopyableCode code="auto_create_tasks" /></td><td><code>boolean</code></td><td>Whether to automatically create tasks using this task definition for all gateways with the specified current version. If false, the task must me created by calling CreateWirelessGatewayTask.</td></tr>
<tr><td><CopyableCode code="update" /></td><td><code>object</code></td><td>Information about the gateways to update.</td></tr>
<tr><td><CopyableCode code="lo_ra_wan_update_gateway_task_entry" /></td><td><code>object</code></td><td>The list of task definitions.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the new wireless gateway task definition</td></tr>
<tr><td><CopyableCode code="task_definition_type" /></td><td><code>string</code></td><td>A filter to list only the wireless gateway task definitions that use this task definition type</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>TaskDefinition arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the destination.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html"><code>AWS::IoTWireless::TaskDefinition</code></a>.

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
    <td><CopyableCode code="AutoCreateTasks, region" /></td>
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
Gets all <code>task_definitions</code> in a region.
```sql
SELECT
region,
name,
auto_create_tasks,
update,
lo_ra_wan_update_gateway_task_entry,
id,
task_definition_type,
arn,
tags
FROM aws.iotwireless.task_definitions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>task_definition</code>.
```sql
SELECT
region,
name,
auto_create_tasks,
update,
lo_ra_wan_update_gateway_task_entry,
id,
task_definition_type,
arn,
tags
FROM aws.iotwireless.task_definitions
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>task_definition</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotwireless.task_definitions (
 AutoCreateTasks,
 region
)
SELECT 
'{{ AutoCreateTasks }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotwireless.task_definitions (
 Name,
 AutoCreateTasks,
 Update,
 LoRaWANUpdateGatewayTaskEntry,
 TaskDefinitionType,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ AutoCreateTasks }}',
 '{{ Update }}',
 '{{ LoRaWANUpdateGatewayTaskEntry }}',
 '{{ TaskDefinitionType }}',
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
  - name: task_definition
    props:
      - name: Name
        value: '{{ Name }}'
      - name: AutoCreateTasks
        value: '{{ AutoCreateTasks }}'
      - name: Update
        value:
          UpdateDataSource: '{{ UpdateDataSource }}'
          UpdateDataRole: '{{ UpdateDataRole }}'
          LoRaWAN:
            UpdateSignature: '{{ UpdateSignature }}'
            SigKeyCrc: '{{ SigKeyCrc }}'
            CurrentVersion:
              PackageVersion: '{{ PackageVersion }}'
              Model: '{{ Model }}'
              Station: '{{ Station }}'
            UpdateVersion: null
      - name: LoRaWANUpdateGatewayTaskEntry
        value:
          CurrentVersion: null
          UpdateVersion: null
      - name: TaskDefinitionType
        value: '{{ TaskDefinitionType }}'
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
DELETE FROM aws.iotwireless.task_definitions
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>task_definitions</code> resource, the following permissions are required:

### Create
```json
iotwireless:CreateWirelessGatewayTaskDefinition,
iotwireless:TagResource,
iam:GetRole,
iam:PassRole
```

### Update
```json
iotwireless:GetWirelessGatewayTaskDefinition,
iotwireless:TagResource,
iotwireless:UntagResource
```

### Read
```json
iotwireless:GetWirelessGatewayTaskDefinition,
iotwireless:ListTagsForResource
```

### Delete
```json
iotwireless:DeleteWirelessGatewayTaskDefinition
```

### List
```json
iotwireless:ListWirelessGatewayTaskDefinitions,
iotwireless:ListTagsForResource
```
