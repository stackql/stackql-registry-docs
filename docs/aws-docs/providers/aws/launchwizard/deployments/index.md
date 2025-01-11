---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - launchwizard
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

Creates, updates, deletes or gets a <code>deployment</code> resource or lists <code>deployments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::LaunchWizard::Deployment Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.launchwizard.deployments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN of the LaunchWizard deployment</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Timestamp of LaunchWizard deployment creation</td></tr>
<tr><td><CopyableCode code="deleted_at" /></td><td><code>string</code></td><td>Timestamp of LaunchWizard deployment deletion</td></tr>
<tr><td><CopyableCode code="deployment_id" /></td><td><code>string</code></td><td>Deployment ID of the LaunchWizard deployment</td></tr>
<tr><td><CopyableCode code="deployment_pattern_name" /></td><td><code>string</code></td><td>Workload deployment pattern name</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of LaunchWizard deployment</td></tr>
<tr><td><CopyableCode code="resource_group" /></td><td><code>string</code></td><td>Resource Group Name created for LaunchWizard deployment</td></tr>
<tr><td><CopyableCode code="specifications" /></td><td><code>object</code></td><td>LaunchWizard deployment specifications</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Status of LaunchWizard deployment</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags for LaunchWizard deployment</td></tr>
<tr><td><CopyableCode code="workload_name" /></td><td><code>string</code></td><td>Workload Name for LaunchWizard deployment</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html"><code>AWS::LaunchWizard::Deployment</code></a>.

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
    <td><CopyableCode code="DeploymentPatternName, Name, Specifications, WorkloadName, region" /></td>
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
Gets all <code>deployments</code> in a region.
```sql
SELECT
region,
arn,
created_at,
deleted_at,
deployment_id,
deployment_pattern_name,
name,
resource_group,
specifications,
status,
tags,
workload_name
FROM aws.launchwizard.deployments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>deployment</code>.
```sql
SELECT
region,
arn,
created_at,
deleted_at,
deployment_id,
deployment_pattern_name,
name,
resource_group,
specifications,
status,
tags,
workload_name
FROM aws.launchwizard.deployments
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.launchwizard.deployments (
 DeploymentPatternName,
 Name,
 Specifications,
 WorkloadName,
 region
)
SELECT 
'{{ DeploymentPatternName }}',
 '{{ Name }}',
 '{{ Specifications }}',
 '{{ WorkloadName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.launchwizard.deployments (
 DeploymentPatternName,
 Name,
 Specifications,
 Tags,
 WorkloadName,
 region
)
SELECT 
 '{{ DeploymentPatternName }}',
 '{{ Name }}',
 '{{ Specifications }}',
 '{{ Tags }}',
 '{{ WorkloadName }}',
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
  - name: deployment
    props:
      - name: DeploymentPatternName
        value: '{{ DeploymentPatternName }}'
      - name: Name
        value: '{{ Name }}'
      - name: Specifications
        value: {}
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: WorkloadName
        value: '{{ WorkloadName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.launchwizard.deployments
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>deployments</code> resource, the following permissions are required:

### Create
```json
launchwizard:CreateDeployment,
launchwizard:GetDeployment,
launchwizard:ListDeploymentEvents,
launchwizard:ListTagsForResource,
launchwizard:TagResource,
ssm:GetParameter,
ssm:PutParameter,
ssm:DescribeParameters,
ssm:AddTagsToResource,
ssm:DeleteParameter,
secretsmanager:DescribeSecret,
secretsmanager:PutSecretValue,
secretsmanager:CreateSecret,
secretsmanager:TagResource,
secretsmanager:UpdateSecret,
resource-groups:CreateGroup,
resource-groups:DeleteGroup,
cloudformation:DeleteStack,
cloudformation:DescribeStackResources,
cloudformation:DescribeStackResource,
cloudformation:DescribeStacks,
cloudformation:DescribeStackEvents,
cloudformation:CreateStack,
cloudformation:TagResource,
s3:PutObject,
s3:GetObject,
s3:CreateBucket,
sns:ListSubscriptionsByTopic,
sns:Publish,
sns:ListSubscriptions,
sns:ListTopics,
sns:CreateTopic,
sns:Subscribe,
sns:Unsubscribe,
sqs:TagQueue,
sqs:GetQueueUrl,
sqs:AddPermission,
sqs:ListQueues,
sqs:GetQueueAttributes,
sqs:ListQueueTags,
sqs:CreateQueue,
sqs:SetQueueAttributes
```

### Read
```json
launchwizard:GetDeployment,
launchwizard:ListDeploymentEvents,
launchwizard:ListTagsForResource
```

### Delete
```json
launchwizard:GetDeployment,
launchwizard:DeleteDeployment,
launchwizard:UntagResource,
ssm:DeleteParameter,
secretsmanager:DeleteSecret,
resource-groups:DeleteGroup,
cloudformation:DeleteStack,
cloudformation:DescribeStacks,
ssm:GetParameter,
sns:ListSubscriptionsByTopic,
sns:Publish,
sns:ListSubscriptions,
sns:ListTopics,
sns:CreateTopic,
sns:DeleteTopic,
sns:Subscribe,
sns:Unsubscribe,
sqs:GetQueueUrl,
sqs:ListQueues,
sqs:DeleteQueue,
sqs:GetQueueAttributes,
sqs:ListQueueTags
```

### Update
```json
launchwizard:GetDeployment,
launchwizard:ListTagsForResource,
launchwizard:TagResource,
launchwizard:UntagResource
```

### List
```json
launchwizard:ListDeployments,
launchwizard:ListTagsForResource
```
