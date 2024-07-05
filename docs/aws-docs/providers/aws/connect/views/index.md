---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
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

Creates, updates, deletes or gets a <code>view</code> resource or lists <code>views</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.views" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the instance.</td></tr>
<tr><td><CopyableCode code="view_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the view.</td></tr>
<tr><td><CopyableCode code="view_id" /></td><td><code>string</code></td><td>The view id of the view.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the view.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the view.</td></tr>
<tr><td><CopyableCode code="template" /></td><td><code>object</code></td><td>The template of the view as JSON.</td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>array</code></td><td>The actions of the view in an array.</td></tr>
<tr><td><CopyableCode code="view_content_sha256" /></td><td><code>string</code></td><td>The view content hash.</td></tr>
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
    <td><CopyableCode code="InstanceArn, Template, Actions, Name, region" /></td>
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
Gets all <code>views</code> in a region.
```sql
SELECT
region,
instance_arn,
view_arn,
view_id,
name,
description,
template,
actions,
view_content_sha256,
tags
FROM aws.connect.views
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>view</code>.
```sql
SELECT
region,
instance_arn,
view_arn,
view_id,
name,
description,
template,
actions,
view_content_sha256,
tags
FROM aws.connect.views
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
INSERT INTO aws.connect.views (
 InstanceArn,
 Name,
 Template,
 Actions,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ Name }}',
 '{{ Template }}',
 '{{ Actions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.views (
 InstanceArn,
 Name,
 Description,
 Template,
 Actions,
 Tags,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ Name }}',
 '{{ Description }}',
 '{{ Template }}',
 '{{ Actions }}',
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
  - name: view
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: Template
        value: {}
      - name: Actions
        value:
          - '{{ Actions[0] }}'
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
DELETE FROM aws.connect.views
WHERE data__Identifier = '<ViewArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>views</code> resource, the following permissions are required:

### Create
```json
connect:CreateView,
connect:TagResource
```

### Read
```json
connect:DescribeView
```

### Delete
```json
connect:DeleteView,
connect:UntagResource
```

### List
```json
connect:ListViews
```

### Update
```json
connect:UpdateViewMetadata,
connect:UpdateViewContent,
connect:TagResource,
connect:UntagResource
```

