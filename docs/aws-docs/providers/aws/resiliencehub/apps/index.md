---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - resiliencehub
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


Used to retrieve a list of <code>apps</code> in a region or to create or delete a <code>apps</code> resource, use <code>app</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::ResilienceHub::App.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.resiliencehub.apps" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="app_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the App.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
app_arn
FROM aws.resiliencehub.apps
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>app</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- app.iql (required properties only)
INSERT INTO aws.resiliencehub.apps (
 Name,
 AppTemplateBody,
 ResourceMappings,
 region
)
SELECT 
'{{ Name }}',
 '{{ AppTemplateBody }}',
 '{{ ResourceMappings }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- app.iql (all properties)
INSERT INTO aws.resiliencehub.apps (
 Name,
 Description,
 ResiliencyPolicyArn,
 Tags,
 AppTemplateBody,
 ResourceMappings,
 AppAssessmentSchedule,
 PermissionModel,
 EventSubscriptions,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ ResiliencyPolicyArn }}',
 '{{ Tags }}',
 '{{ AppTemplateBody }}',
 '{{ ResourceMappings }}',
 '{{ AppAssessmentSchedule }}',
 '{{ PermissionModel }}',
 '{{ EventSubscriptions }}',
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
  - name: app
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: ResiliencyPolicyArn
        value: '{{ ResiliencyPolicyArn }}'
      - name: Tags
        value: {}
      - name: AppTemplateBody
        value: '{{ AppTemplateBody }}'
      - name: ResourceMappings
        value:
          - LogicalStackName: '{{ LogicalStackName }}'
            MappingType: '{{ MappingType }}'
            ResourceName: '{{ ResourceName }}'
            TerraformSourceName: '{{ TerraformSourceName }}'
            EksSourceName: '{{ EksSourceName }}'
            PhysicalResourceId:
              AwsAccountId: '{{ AwsAccountId }}'
              AwsRegion: '{{ AwsRegion }}'
              Identifier: '{{ Identifier }}'
              Type: '{{ Type }}'
      - name: AppAssessmentSchedule
        value: '{{ AppAssessmentSchedule }}'
      - name: PermissionModel
        value:
          Type: '{{ Type }}'
          InvokerRoleName: '{{ InvokerRoleName }}'
          CrossAccountRoleArns:
            - '{{ CrossAccountRoleArns[0] }}'
      - name: EventSubscriptions
        value:
          - Name: '{{ Name }}'
            EventType: '{{ EventType }}'
            SnsTopicArn: '{{ SnsTopicArn }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.resiliencehub.apps
WHERE data__Identifier = '<AppArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>apps</code> resource, the following permissions are required:

### Create
```json
cloudformation:DescribeStacks,
cloudformation:ListStackResources,
s3:GetBucketLocation,
s3:GetObject,
s3:ListAllMyBuckets,
autoscaling:DescribeAutoScalingGroups,
apigateway:GET,
ec2:Describe*,
ecs:DescribeServices,
eks:DescribeCluster,
elasticfilesystem:DescribeFileSystems,
elasticloadbalancing:DescribeLoadBalancers,
lambda:GetFunction*,
rds:Describe*,
dynamodb:Describe*,
sqs:GetQueueAttributes,
sns:GetTopicAttributes,
route53:List*,
iam:PassRole,
resiliencehub:*
```

### Delete
```json
resiliencehub:DeleteApp,
resiliencehub:UntagResource,
resiliencehub:ListApps
```

### List
```json
resiliencehub:ListApps
```

