---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
  - resourceexplorer2
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

Creates, updates, deletes or gets a <code>view</code> resource or lists <code>views</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ResourceExplorer2::View Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.resourceexplorer2.views" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="filters" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="included_properties" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="view_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="view_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="ViewName, region" /></td>
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
List all <code>views</code> in a region.
```sql
SELECT
region,
view_arn
FROM aws.resourceexplorer2.views
WHERE region = 'us-east-1';
```
Gets all properties from a <code>view</code>.
```sql
SELECT
region,
filters,
included_properties,
scope,
tags,
view_arn,
view_name
FROM aws.resourceexplorer2.views
WHERE region = 'us-east-1' AND data__Identifier = '<ViewArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>view</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.resourceexplorer2.views (
 ViewName,
 region
)
SELECT 
'{{ ViewName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.resourceexplorer2.views (
 Filters,
 IncludedProperties,
 Scope,
 Tags,
 ViewName,
 region
)
SELECT 
 '{{ Filters }}',
 '{{ IncludedProperties }}',
 '{{ Scope }}',
 '{{ Tags }}',
 '{{ ViewName }}',
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
  - name: view
    props:
      - name: Filters
        value:
          FilterString: '{{ FilterString }}'
      - name: IncludedProperties
        value:
          - Name: '{{ Name }}'
      - name: Scope
        value: '{{ Scope }}'
      - name: Tags
        value: {}
      - name: ViewName
        value: '{{ ViewName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.resourceexplorer2.views
WHERE data__Identifier = '<ViewArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>views</code> resource, the following permissions are required:

### Create
```json
resource-explorer-2:CreateView,
resource-explorer-2:TagResource
```

### Read
```json
resource-explorer-2:GetView
```

### Update
```json
resource-explorer-2:UpdateView,
resource-explorer-2:TagResource,
resource-explorer-2:UntagResource,
resource-explorer-2:ListTagsForResource
```

### Delete
```json
resource-explorer-2:DeleteView,
resource-explorer-2:GetView,
resource-explorer-2:UntagResource
```

### List
```json
resource-explorer-2:ListViews
```

