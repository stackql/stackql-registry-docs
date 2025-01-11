---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - rbin
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

Creates, updates, deletes or gets a <code>rule</code> resource or lists <code>rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Rbin::Rule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rbin.rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Rule Arn is unique for each rule.</td></tr>
<tr><td><CopyableCode code="identifier" /></td><td><code>string</code></td><td>The unique ID of the retention rule.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the retention rule.</td></tr>
<tr><td><CopyableCode code="resource_tags" /></td><td><code>array</code></td><td>Information about the resource tags used to identify resources that are retained by the retention rule.</td></tr>
<tr><td><CopyableCode code="exclude_resource_tags" /></td><td><code>array</code></td><td>Information about the exclude resource tags used to identify resources that are excluded by the retention rule.</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>The resource type retained by the retention rule.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Information about the tags assigned to the retention rule.</td></tr>
<tr><td><CopyableCode code="retention_period" /></td><td><code>object</code></td><td>Information about the retention period for which the retention rule is to retain resources.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The state of the retention rule. Only retention rules that are in the available state retain resources.</td></tr>
<tr><td><CopyableCode code="lock_configuration" /></td><td><code>object</code></td><td>Information about the retention rule lock configuration.</td></tr>
<tr><td><CopyableCode code="lock_state" /></td><td><code>string</code></td><td>The lock state for the retention rule.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rbin-rule.html"><code>AWS::Rbin::Rule</code></a>.

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
    <td><CopyableCode code="RetentionPeriod, ResourceType, region" /></td>
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
Gets all <code>rules</code> in a region.
```sql
SELECT
region,
arn,
identifier,
description,
resource_tags,
exclude_resource_tags,
resource_type,
tags,
retention_period,
status,
lock_configuration,
lock_state
FROM aws.rbin.rules
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>rule</code>.
```sql
SELECT
region,
arn,
identifier,
description,
resource_tags,
exclude_resource_tags,
resource_type,
tags,
retention_period,
status,
lock_configuration,
lock_state
FROM aws.rbin.rules
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.rbin.rules (
 ResourceType,
 RetentionPeriod,
 region
)
SELECT 
'{{ ResourceType }}',
 '{{ RetentionPeriod }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rbin.rules (
 Description,
 ResourceTags,
 ExcludeResourceTags,
 ResourceType,
 Tags,
 RetentionPeriod,
 Status,
 LockConfiguration,
 region
)
SELECT 
 '{{ Description }}',
 '{{ ResourceTags }}',
 '{{ ExcludeResourceTags }}',
 '{{ ResourceType }}',
 '{{ Tags }}',
 '{{ RetentionPeriod }}',
 '{{ Status }}',
 '{{ LockConfiguration }}',
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
  - name: rule
    props:
      - name: Description
        value: '{{ Description }}'
      - name: ResourceTags
        value:
          - ResourceTagKey: '{{ ResourceTagKey }}'
            ResourceTagValue: '{{ ResourceTagValue }}'
      - name: ExcludeResourceTags
        value:
          - null
      - name: ResourceType
        value: '{{ ResourceType }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: RetentionPeriod
        value:
          RetentionPeriodValue: '{{ RetentionPeriodValue }}'
          RetentionPeriodUnit: '{{ RetentionPeriodUnit }}'
      - name: Status
        value: '{{ Status }}'
      - name: LockConfiguration
        value:
          UnlockDelayValue: '{{ UnlockDelayValue }}'
          UnlockDelayUnit: '{{ UnlockDelayUnit }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.rbin.rules
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rules</code> resource, the following permissions are required:

### Create
```json
rbin:CreateRule,
rbin:GetRule,
rbin:LockRule,
rbin:TagResource,
iam:PassRole
```

### Read
```json
rbin:GetRule,
rbin:ListTagsForResource,
iam:PassRole
```

### Update
```json
rbin:GetRule,
rbin:UpdateRule,
rbin:LockRule,
rbin:UnlockRule,
rbin:TagResource,
rbin:UntagResource,
rbin:ListTagsForResource,
iam:PassRole
```

### Delete
```json
rbin:GetRule,
rbin:DeleteRule,
iam:PassRole
```

### List
```json
rbin:ListRules,
rbin:ListTagsForResource,
iam:PassRole
```
