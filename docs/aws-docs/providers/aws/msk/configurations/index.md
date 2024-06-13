---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - msk
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

Creates, updates, deletes or gets a <code>configuration</code> resource or lists <code>configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::Configuration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="server_properties" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="kafka_versions_list" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="latest_revision" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="ServerProperties, Name, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>configurations</code> in a region.
```sql
SELECT
region,
arn
FROM aws.msk.configurations
WHERE region = 'us-east-1';
```
Gets all properties from a <code>configuration</code>.
```sql
SELECT
region,
name,
description,
server_properties,
kafka_versions_list,
arn,
latest_revision
FROM aws.msk.configurations
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.msk.configurations (
 Name,
 ServerProperties,
 region
)
SELECT 
'{{ Name }}',
 '{{ ServerProperties }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.msk.configurations (
 Name,
 Description,
 ServerProperties,
 KafkaVersionsList,
 LatestRevision,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ ServerProperties }}',
 '{{ KafkaVersionsList }}',
 '{{ LatestRevision }}',
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
  - name: configuration
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: ServerProperties
        value: '{{ ServerProperties }}'
      - name: KafkaVersionsList
        value:
          - '{{ KafkaVersionsList[0] }}'
      - name: LatestRevision
        value:
          CreationTime: '{{ CreationTime }}'
          Description: '{{ Description }}'
          Revision: '{{ Revision }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.msk.configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configurations</code> resource, the following permissions are required:

### Create
```json
kafka:CreateConfiguration,
Kafka:DescribeConfiguration
```

### Delete
```json
kafka:DeleteConfiguration,
kafka:DescribeConfiguration
```

### List
```json
kafka:ListConfigurations
```

### Read
```json
kafka:DescribeConfiguration
```

### Update
```json
kafka:UpdateConfiguration,
kafka:DescribeConfiguration
```

