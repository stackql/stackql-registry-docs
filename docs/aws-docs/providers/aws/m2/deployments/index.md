---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - m2
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
<tr><td><b>Description</b></td><td>Represents a deployment resource of an AWS Mainframe Modernization (M2) application to a specified environment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.m2.deployments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The environment ID.</td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><CopyableCode code="application_version" /></td><td><code>integer</code></td><td>The version number of the application to deploy</td></tr>
<tr><td><CopyableCode code="deployment_id" /></td><td><code>string</code></td><td>The deployment ID.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the deployment.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-deployment.html"><code>AWS::M2::Deployment</code></a>.

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
    <td><CopyableCode code="EnvironmentId, ApplicationId, ApplicationVersion, region" /></td>
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
environment_id,
application_id,
application_version,
deployment_id,
status
FROM aws.m2.deployments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>deployment</code>.
```sql
SELECT
region,
environment_id,
application_id,
application_version,
deployment_id,
status
FROM aws.m2.deployments
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>';
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
INSERT INTO aws.m2.deployments (
 EnvironmentId,
 ApplicationId,
 ApplicationVersion,
 region
)
SELECT 
'{{ EnvironmentId }}',
 '{{ ApplicationId }}',
 '{{ ApplicationVersion }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.m2.deployments (
 EnvironmentId,
 ApplicationId,
 ApplicationVersion,
 region
)
SELECT 
 '{{ EnvironmentId }}',
 '{{ ApplicationId }}',
 '{{ ApplicationVersion }}',
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
      - name: EnvironmentId
        value: '{{ EnvironmentId }}'
      - name: ApplicationId
        value: '{{ ApplicationId }}'
      - name: ApplicationVersion
        value: '{{ ApplicationVersion }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.m2.deployments
WHERE data__Identifier = '<ApplicationId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>deployments</code> resource, the following permissions are required:

### Create
```json
m2:CreateDeployment,
m2:ListDeployments,
m2:GetDeployment,
iam:PassRole,
ec2:DescribeNetworkInterfaces,
elasticloadbalancing:CreateListener,
elasticloadbalancing:CreateLoadBalancer,
elasticloadbalancing:CreateTargetGroup,
elasticloadbalancing:AddTags,
elasticloadbalancing:RegisterTargets,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
logs:CreateLogGroup,
logs:PutResourcePolicy
```

### Read
```json
m2:ListDeployments,
m2:GetDeployment
```

### Update
```json
m2:CreateDeployment,
m2:ListDeployments,
m2:GetDeployment,
elasticloadbalancing:CreateListener,
elasticloadbalancing:CreateLoadBalancer,
elasticloadbalancing:CreateTargetGroup,
elasticloadbalancing:DeleteListener,
elasticloadbalancing:DeleteTargetGroup,
elasticloadbalancing:DeregisterTargets,
elasticloadbalancing:DeleteLoadBalancer,
elasticloadbalancing:AddTags,
elasticloadbalancing:RegisterTargets,
ec2:DescribeNetworkInterfaces
```

### Delete
```json
elasticloadbalancing:DeleteListener,
elasticloadbalancing:DeleteTargetGroup,
elasticloadbalancing:DeregisterTargets,
elasticloadbalancing:DeleteLoadBalancer,
logs:DeleteLogDelivery,
m2:ListDeployments,
m2:GetDeployment,
m2:DeleteApplicationFromEnvironment
```

### List
```json
m2:ListDeployments
```
