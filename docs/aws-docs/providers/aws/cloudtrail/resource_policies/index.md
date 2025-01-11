---
title: resource_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policies
  - cloudtrail
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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudTrail::ResourcePolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudtrail.resource_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The ARN of the AWS CloudTrail resource to which the policy applies.</td></tr>
<tr><td><CopyableCode code="resource_policy" /></td><td><code>object</code></td><td>A policy document containing permissions to add to the specified resource. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-resourcepolicy.html"><code>AWS::CloudTrail::ResourcePolicy</code></a>.

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
    <td><CopyableCode code="ResourceArn, ResourcePolicy, region" /></td>
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

Gets all properties from an individual <code>resource_policy</code>.
```sql
SELECT
region,
resource_arn,
resource_policy
FROM aws.cloudtrail.resource_policies
WHERE region = 'us-east-1' AND data__Identifier = '<ResourceArn>';
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
INSERT INTO aws.cloudtrail.resource_policies (
 ResourceArn,
 ResourcePolicy,
 region
)
SELECT 
'{{ ResourceArn }}',
 '{{ ResourcePolicy }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudtrail.resource_policies (
 ResourceArn,
 ResourcePolicy,
 region
)
SELECT 
 '{{ ResourceArn }}',
 '{{ ResourcePolicy }}',
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
      - name: ResourcePolicy
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cloudtrail.resource_policies
WHERE data__Identifier = '<ResourceArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_policies</code> resource, the following permissions are required:

### Create
```json
CloudTrail:PutResourcePolicy,
CloudTrail:GetResourcePolicy
```

### Read
```json
CloudTrail:GetResourcePolicy
```

### Update
```json
CloudTrail:PutResourcePolicy,
CloudTrail:GetResourcePolicy
```

### Delete
```json
CloudTrail:DeleteResourcePolicy
```
