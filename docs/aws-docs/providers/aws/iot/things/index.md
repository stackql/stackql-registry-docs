---
title: things
hide_title: false
hide_table_of_contents: false
keywords:
  - things
  - iot
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

Creates, updates, deletes or gets a <code>thing</code> resource or lists <code>things</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>things</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoT::Thing</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.things" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="attribute_payload" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="thing_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>things</code> in a region.
```sql
SELECT
region,
thing_name
FROM aws.iot.things
WHERE region = 'us-east-1';
```
Gets all properties from a <code>thing</code>.
```sql
SELECT
region,
id,
arn,
attribute_payload,
thing_name
FROM aws.iot.things
WHERE region = 'us-east-1' AND data__Identifier = '<ThingName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>thing</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.things (
 AttributePayload,
 ThingName,
 region
)
SELECT 
'{{ AttributePayload }}',
 '{{ ThingName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.things (
 AttributePayload,
 ThingName,
 region
)
SELECT 
 '{{ AttributePayload }}',
 '{{ ThingName }}',
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
  - name: thing
    props:
      - name: AttributePayload
        value:
          Attributes: {}
      - name: ThingName
        value: '{{ ThingName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iot.things
WHERE data__Identifier = '<ThingName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>things</code> resource, the following permissions are required:

### Create
```json
iot:CreateThing,
iot:DescribeThing
```

### Delete
```json
iot:DeleteThing,
iot:DescribeThing
```

### List
```json
iot:ListThings
```

### Read
```json
iot:DescribeThing
```

### Update
```json
iot:UpdateThing,
iot:DescribeThing
```

