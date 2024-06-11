---
title: features
hide_title: false
hide_table_of_contents: false
keywords:
  - features
  - evidently
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

Creates, updates, deletes or gets a <code>feature</code> resource or lists <code>features</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Evidently::Feature.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.evidently.features" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="project" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="evaluation_strategy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="variations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="default_variation" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="entity_overrides" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="Name, Project, Variations, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from a <code>feature</code>.
```sql
SELECT
region,
arn,
project,
name,
description,
evaluation_strategy,
variations,
default_variation,
entity_overrides,
tags
FROM aws.evidently.features
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>feature</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.evidently.features (
 Project,
 Name,
 Variations,
 region
)
SELECT 
'{{ Project }}',
 '{{ Name }}',
 '{{ Variations }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.evidently.features (
 Project,
 Name,
 Description,
 EvaluationStrategy,
 Variations,
 DefaultVariation,
 EntityOverrides,
 Tags,
 region
)
SELECT 
 '{{ Project }}',
 '{{ Name }}',
 '{{ Description }}',
 '{{ EvaluationStrategy }}',
 '{{ Variations }}',
 '{{ DefaultVariation }}',
 '{{ EntityOverrides }}',
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
  - name: feature
    props:
      - name: Project
        value: '{{ Project }}'
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: EvaluationStrategy
        value: '{{ EvaluationStrategy }}'
      - name: Variations
        value:
          - VariationName: '{{ VariationName }}'
            BooleanValue: '{{ BooleanValue }}'
            StringValue: '{{ StringValue }}'
            LongValue: null
            DoubleValue: null
      - name: DefaultVariation
        value: '{{ DefaultVariation }}'
      - name: EntityOverrides
        value:
          - EntityId: '{{ EntityId }}'
            Variation: '{{ Variation }}'
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
DELETE FROM aws.evidently.features
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>features</code> resource, the following permissions are required:

### Create
```json
evidently:CreateFeature,
evidently:TagResource,
evidently:GetFeature
```

### Read
```json
evidently:GetFeature,
evidently:ListTagsForResource
```

### Update
```json
evidently:UpdateFeature,
evidently:ListTagsForResource,
evidently:TagResource,
evidently:UntagResource,
evidently:GetFeature
```

### Delete
```json
evidently:DeleteFeature,
evidently:UntagResource,
evidently:GetFeature
```

