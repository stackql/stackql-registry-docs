---
title: resource_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policies
  - lex
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

Creates, updates, deletes or gets a <code>resource_policy</code> resource or lists <code>resource_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource policy with specified policy statements that attaches to a Lex bot or bot alias.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lex.resource_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.</td></tr>
<tr><td><CopyableCode code="revision_id" /></td><td><code>string</code></td><td>The current revision of the resource policy. Use the revision ID to make sure that you are updating the most current version of a resource policy when you add a policy statement to a resource, delete a resource, or update a resource.</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>A resource policy to add to the resource. The policy is a JSON structure following the IAM syntax that contains one or more statements that define the policy.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The Physical ID of the resource policy.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html"><code>AWS::Lex::ResourcePolicy</code></a>.

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
    <td><CopyableCode code="ResourceArn, Policy, region" /></td>
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
Gets all <code>resource_policies</code> in a region.
```sql
SELECT
region,
resource_arn,
revision_id,
policy,
id
FROM aws.lex.resource_policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>resource_policy</code>.
```sql
SELECT
region,
resource_arn,
revision_id,
policy,
id
FROM aws.lex.resource_policies
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.lex.resource_policies (
 ResourceArn,
 Policy,
 region
)
SELECT 
'{{ ResourceArn }}',
 '{{ Policy }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lex.resource_policies (
 ResourceArn,
 Policy,
 region
)
SELECT 
 '{{ ResourceArn }}',
 '{{ Policy }}',
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
  - name: resource_policy
    props:
      - name: ResourceArn
        value: '{{ ResourceArn }}'
      - name: Policy
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.lex.resource_policies
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_policies</code> resource, the following permissions are required:

### Create
```json
lex:CreateResourcePolicy,
lex:DescribeResourcePolicy
```

### Read
```json
lex:DescribeResourcePolicy
```

### Update
```json
lex:UpdateResourcePolicy,
lex:DescribeResourcePolicy
```

### Delete
```json
lex:DeleteResourcePolicy,
lex:DescribeResourcePolicy
```

### List
```json
lex:DescribeResourcePolicy
```
