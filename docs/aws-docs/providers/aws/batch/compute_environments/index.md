---
title: compute_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - compute_environments
  - batch
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

Creates, updates, deletes or gets a <code>compute_environment</code> resource or lists <code>compute_environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compute_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Batch::ComputeEnvironment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.batch.compute_environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="compute_environment_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="compute_environment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="compute_resources" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="replace_compute_environment" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="service_role" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="update_policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="unmanagedv_cpus" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="eks_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="context" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html"><code>AWS::Batch::ComputeEnvironment</code></a>.

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
    <td><CopyableCode code="Type, region" /></td>
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
Gets all <code>compute_environments</code> in a region.
```sql
SELECT
region,
compute_environment_arn,
compute_environment_name,
compute_resources,
replace_compute_environment,
service_role,
state,
tags,
type,
update_policy,
unmanagedv_cpus,
eks_configuration,
context
FROM aws.batch.compute_environments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>compute_environment</code>.
```sql
SELECT
region,
compute_environment_arn,
compute_environment_name,
compute_resources,
replace_compute_environment,
service_role,
state,
tags,
type,
update_policy,
unmanagedv_cpus,
eks_configuration,
context
FROM aws.batch.compute_environments
WHERE region = 'us-east-1' AND data__Identifier = '<ComputeEnvironmentArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>compute_environment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.batch.compute_environments (
 Type,
 region
)
SELECT 
'{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.batch.compute_environments (
 ComputeEnvironmentName,
 ComputeResources,
 ReplaceComputeEnvironment,
 ServiceRole,
 State,
 Tags,
 Type,
 UpdatePolicy,
 UnmanagedvCpus,
 EksConfiguration,
 Context,
 region
)
SELECT 
 '{{ ComputeEnvironmentName }}',
 '{{ ComputeResources }}',
 '{{ ReplaceComputeEnvironment }}',
 '{{ ServiceRole }}',
 '{{ State }}',
 '{{ Tags }}',
 '{{ Type }}',
 '{{ UpdatePolicy }}',
 '{{ UnmanagedvCpus }}',
 '{{ EksConfiguration }}',
 '{{ Context }}',
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
  - name: compute_environment
    props:
      - name: ComputeEnvironmentName
        value: '{{ ComputeEnvironmentName }}'
      - name: ComputeResources
        value:
          AllocationStrategy: '{{ AllocationStrategy }}'
          BidPercentage: '{{ BidPercentage }}'
          DesiredvCpus: '{{ DesiredvCpus }}'
          Ec2Configuration:
            - ImageIdOverride: '{{ ImageIdOverride }}'
              ImageType: '{{ ImageType }}'
              ImageKubernetesVersion: '{{ ImageKubernetesVersion }}'
          Ec2KeyPair: '{{ Ec2KeyPair }}'
          ImageId: '{{ ImageId }}'
          InstanceRole: '{{ InstanceRole }}'
          InstanceTypes:
            - '{{ InstanceTypes[0] }}'
          LaunchTemplate:
            LaunchTemplateId: '{{ LaunchTemplateId }}'
            LaunchTemplateName: '{{ LaunchTemplateName }}'
            Version: '{{ Version }}'
            Overrides:
              - LaunchTemplateId: '{{ LaunchTemplateId }}'
                LaunchTemplateName: '{{ LaunchTemplateName }}'
                Version: '{{ Version }}'
                TargetInstanceTypes:
                  - '{{ TargetInstanceTypes[0] }}'
          MaxvCpus: '{{ MaxvCpus }}'
          MinvCpus: '{{ MinvCpus }}'
          PlacementGroup: '{{ PlacementGroup }}'
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
          SpotIamFleetRole: '{{ SpotIamFleetRole }}'
          Subnets:
            - '{{ Subnets[0] }}'
          Tags: {}
          Type: '{{ Type }}'
          UpdateToLatestImageVersion: '{{ UpdateToLatestImageVersion }}'
      - name: ReplaceComputeEnvironment
        value: '{{ ReplaceComputeEnvironment }}'
      - name: ServiceRole
        value: '{{ ServiceRole }}'
      - name: State
        value: '{{ State }}'
      - name: Tags
        value: {}
      - name: Type
        value: '{{ Type }}'
      - name: UpdatePolicy
        value:
          TerminateJobsOnUpdate: '{{ TerminateJobsOnUpdate }}'
          JobExecutionTimeoutMinutes: '{{ JobExecutionTimeoutMinutes }}'
      - name: UnmanagedvCpus
        value: '{{ UnmanagedvCpus }}'
      - name: EksConfiguration
        value:
          EksClusterArn: '{{ EksClusterArn }}'
          KubernetesNamespace: '{{ KubernetesNamespace }}'
      - name: Context
        value: '{{ Context }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.batch.compute_environments
WHERE data__Identifier = '<ComputeEnvironmentArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>compute_environments</code> resource, the following permissions are required:

### Create
```json
Batch:CreateComputeEnvironment,
Batch:TagResource,
Batch:DescribeComputeEnvironments,
iam:CreateServiceLinkedRole,
Iam:PassRole,
Eks:DescribeCluster
```

### Read
```json
Batch:DescribeComputeEnvironments
```

### Update
```json
Batch:UpdateComputeEnvironment,
Batch:DescribeComputeEnvironments,
Batch:TagResource,
Batch:UnTagResource,
Iam:PassRole,
Eks:DescribeCluster
```

### Delete
```json
Batch:DeleteComputeEnvironment,
Batch:DescribeComputeEnvironments,
Batch:UpdateComputeEnvironment,
Iam:PassRole,
Eks:DescribeCluster
```

### List
```json
Batch:DescribeComputeEnvironments
```
