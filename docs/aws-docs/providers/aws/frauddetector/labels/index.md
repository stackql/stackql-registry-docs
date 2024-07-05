---
title: labels
hide_title: false
hide_table_of_contents: false
keywords:
  - labels
  - frauddetector
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

Creates, updates, deletes or gets a <code>label</code> resource or lists <code>labels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An label for fraud detector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.frauddetector.labels" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the label.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags associated with this label.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The label description.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The label ARN.</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td>The timestamp when the label was created.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>The timestamp when the label was last updated.</td></tr>
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
    <td><CopyableCode code="Name, region" /></td>
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
Gets all <code>labels</code> in a region.
```sql
SELECT
region,
name,
tags,
description,
arn,
created_time,
last_updated_time
FROM aws.frauddetector.labels
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>label</code>.
```sql
SELECT
region,
name,
tags,
description,
arn,
created_time,
last_updated_time
FROM aws.frauddetector.labels
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>label</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.frauddetector.labels (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.frauddetector.labels (
 Name,
 Tags,
 Description,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Tags }}',
 '{{ Description }}',
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
  - name: label
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Description
        value: '{{ Description }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.frauddetector.labels
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>labels</code> resource, the following permissions are required:

### Create
```json
frauddetector:GetLabels,
frauddetector:PutLabel,
frauddetector:ListTagsForResource,
frauddetector:TagResource
```

### Read
```json
frauddetector:GetLabels,
frauddetector:ListTagsForResource
```

### Update
```json
frauddetector:GetLabels,
frauddetector:PutLabel,
frauddetector:ListTagsForResource,
frauddetector:TagResource,
frauddetector:UntagResource
```

### Delete
```json
frauddetector:GetLabels,
frauddetector:DeleteLabel
```

### List
```json
frauddetector:GetLabels,
frauddetector:ListTagsForResource
```

