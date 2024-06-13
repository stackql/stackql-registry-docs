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

Creates, updates, deletes or gets an <code>app</code> resource or lists <code>apps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::ResilienceHub::App.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.resiliencehub.apps" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the app.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>App description.</td></tr>
<tr><td><CopyableCode code="app_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the App.</td></tr>
<tr><td><CopyableCode code="resiliency_policy_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the Resiliency Policy.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="app_template_body" /></td><td><code>string</code></td><td>A string containing full ResilienceHub app template body.</td></tr>
<tr><td><CopyableCode code="resource_mappings" /></td><td><code>array</code></td><td>An array of ResourceMapping objects.</td></tr>
<tr><td><CopyableCode code="app_assessment_schedule" /></td><td><code>string</code></td><td>Assessment execution schedule.</td></tr>
<tr><td><CopyableCode code="permission_model" /></td><td><code>object</code></td><td>Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.</td></tr>
<tr><td><CopyableCode code="event_subscriptions" /></td><td><code>array</code></td><td>The list of events you would like to subscribe and get notification for.</td></tr>
<tr><td><CopyableCode code="drift_status" /></td><td><code>string</code></td><td>Indicates if compliance drifts (deviations) were detected while running an assessment for your application.</td></tr>
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
    <td><CopyableCode code="Name, AppTemplateBody, ResourceMappings, region" /></td>
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
List all <code>apps</code> in a region.
```sql
SELECT
region,
app_arn
FROM aws.resiliencehub.apps
WHERE region = 'us-east-1';
```
Gets all properties from an <code>app</code>.
```sql
SELECT
region,
name,
description,
app_arn,
resiliency_policy_arn,
tags,
app_template_body,
resource_mappings,
app_assessment_schedule,
permission_model,
event_subscriptions,
drift_status
FROM aws.resiliencehub.apps
WHERE region = 'us-east-1' AND data__Identifier = '<AppArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>app</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
resiliencehub:DescribeApp,
resiliencehub:DescribeAppVersionTemplate,
resiliencehub:ListAppVersionResourceMappings,
resiliencehub:ListTagsForResource
```

### Update
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

