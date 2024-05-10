---
title: approved_origins
hide_title: false
hide_table_of_contents: false
keywords:
  - approved_origins
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


Used to retrieve a list of <code>approved_origins</code> in a region or to create or delete a <code>approved_origins</code> resource, use <code>approved_origin</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>approved_origins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::ApprovedOrigin</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.approved_origins" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="origin" /></td><td><code>undefined</code></td><td></td></tr>
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
instance_id,
origin
FROM aws.connect.approved_origins
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>approved_origin</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- approved_origin.iql (required properties only)
INSERT INTO aws.connect.approved_origins (
 Origin,
 InstanceId,
 region
)
SELECT 
'{{ Origin }}',
 '{{ InstanceId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- approved_origin.iql (all properties)
INSERT INTO aws.connect.approved_origins (
 Origin,
 InstanceId,
 region
)
SELECT 
 '{{ Origin }}',
 '{{ InstanceId }}',
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
  - name: approved_origin
    props:
      - name: Origin
        value: '{{ Origin }}'
      - name: InstanceId
        value: '{{ InstanceId }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.connect.approved_origins
WHERE data__Identifier = '<InstanceId|Origin>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>approved_origins</code> resource, the following permissions are required:

### Create
```json
connect:AssociateApprovedOrigin,
connect:ListApprovedOrigins
```

### Delete
```json
connect:DisassociateApprovedOrigin,
connect:ListApprovedOrigins
```

### List
```json
connect:ListApprovedOrigins
```

