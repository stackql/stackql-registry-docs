---
title: signal_catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_catalogs
  - iotfleetwise
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

Creates, updates, deletes or gets a <code>signal_catalog</code> resource or lists <code>signal_catalogs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signal_catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::SignalCatalog Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleetwise.signal_catalogs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modification_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="node_counts" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="nodes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
List all <code>signal_catalogs</code> in a region.
```sql
SELECT
region,
name
FROM aws.iotfleetwise.signal_catalogs
WHERE region = 'us-east-1';
```
Gets all properties from a <code>signal_catalog</code>.
```sql
SELECT
region,
arn,
creation_time,
description,
last_modification_time,
name,
node_counts,
nodes,
tags
FROM aws.iotfleetwise.signal_catalogs
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>signal_catalog</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotfleetwise.signal_catalogs (
 Description,
 Name,
 NodeCounts,
 Nodes,
 Tags,
 region
)
SELECT 
'{{ Description }}',
 '{{ Name }}',
 '{{ NodeCounts }}',
 '{{ Nodes }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotfleetwise.signal_catalogs (
 Description,
 Name,
 NodeCounts,
 Nodes,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Name }}',
 '{{ NodeCounts }}',
 '{{ Nodes }}',
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
  - name: signal_catalog
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: NodeCounts
        value:
          TotalNodes: null
          TotalBranches: null
          TotalSensors: null
          TotalAttributes: null
          TotalActuators: null
      - name: Nodes
        value:
          - null
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
DELETE FROM aws.iotfleetwise.signal_catalogs
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>signal_catalogs</code> resource, the following permissions are required:

### Create
```json
iotfleetwise:GetSignalCatalog,
iotfleetwise:CreateSignalCatalog,
iotfleetwise:ListSignalCatalogNodes,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource
```

### Read
```json
iotfleetwise:GetSignalCatalog,
iotfleetwise:ListSignalCatalogNodes,
iotfleetwise:ListTagsForResource
```

### Update
```json
iotfleetwise:GetSignalCatalog,
iotfleetwise:UpdateSignalCatalog,
iotfleetwise:ListSignalCatalogNodes,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource,
iotfleetwise:UntagResource
```

### Delete
```json
iotfleetwise:GetSignalCatalog,
iotfleetwise:DeleteSignalCatalog
```

### List
```json
iotfleetwise:ListSignalCatalogs
```

