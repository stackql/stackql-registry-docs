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


Used to retrieve a list of <code>task_definitions</code> in a region or to create or delete a <code>task_definitions</code> resource, use <code>task_definition</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a gateway task definition.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.task_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the new wireless gateway task definition</td></tr>
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
id
FROM aws.iotwireless.task_definitions
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>task_definition</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- task_definition.iql (required properties only)
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
-- task_definition.iql (all properties)
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

## `DELETE` Example

```sql
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
iotwireless:ListTagsForResource,
iam:GetRole,
iam:PassRole
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

