---
title: matchmaking_rule_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - matchmaking_rule_sets
  - gamelift
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

Creates, updates, deletes or gets a <code>matchmaking_rule_set</code> resource or lists <code>matchmaking_rule_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>matchmaking_rule_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::MatchmakingRuleSet resource creates an Amazon GameLift (GameLift) matchmaking rule set.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.matchmaking_rule_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A unique identifier for the matchmaking rule set.</td></tr>
<tr><td><CopyableCode code="rule_set_body" /></td><td><code>string</code></td><td>A collection of matchmaking rules, formatted as a JSON string.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift matchmaking rule set resource and uniquely identifies it.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html"><code>AWS::GameLift::MatchmakingRuleSet</code></a>.

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
    <td><CopyableCode code="Name, RuleSetBody, region" /></td>
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
Gets all <code>matchmaking_rule_sets</code> in a region.
```sql
SELECT
region,
name,
rule_set_body,
creation_time,
arn,
tags
FROM aws.gamelift.matchmaking_rule_sets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>matchmaking_rule_set</code>.
```sql
SELECT
region,
name,
rule_set_body,
creation_time,
arn,
tags
FROM aws.gamelift.matchmaking_rule_sets
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>matchmaking_rule_set</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.gamelift.matchmaking_rule_sets (
 Name,
 RuleSetBody,
 region
)
SELECT 
'{{ Name }}',
 '{{ RuleSetBody }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.gamelift.matchmaking_rule_sets (
 Name,
 RuleSetBody,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ RuleSetBody }}',
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
  - name: matchmaking_rule_set
    props:
      - name: Name
        value: '{{ Name }}'
      - name: RuleSetBody
        value: '{{ RuleSetBody }}'
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
DELETE FROM aws.gamelift.matchmaking_rule_sets
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>matchmaking_rule_sets</code> resource, the following permissions are required:

### Create
```json
gamelift:CreateMatchmakingRuleSet,
gamelift:DescribeMatchmakingRuleSets,
gamelift:ValidateMatchmakingRuleSet,
gamelift:ListTagsForResource,
gamelift:TagResource
```

### Read
```json
gamelift:DescribeMatchmakingRuleSets,
gamelift:ValidateMatchmakingRuleSet,
gamelift:ListTagsForResource
```

### Delete
```json
gamelift:DeleteMatchmakingRuleSet
```

### Update
```json
gamelift:DescribeMatchmakingRuleSets,
gamelift:ListTagsForResource,
gamelift:TagResource,
gamelift:UntagResource
```

### List
```json
gamelift:DescribeMatchmakingRuleSets
```
