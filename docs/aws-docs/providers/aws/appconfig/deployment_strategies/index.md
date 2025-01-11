---
title: deployment_strategies
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_strategies
  - appconfig
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

Creates, updates, deletes or gets a <code>deployment_strategy</code> resource or lists <code>deployment_strategies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_strategies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppConfig::DeploymentStrategy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.deployment_strategies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="deployment_duration_in_minutes" /></td><td><code>number</code></td><td>Total amount of time for a deployment to last.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the deployment strategy.</td></tr>
<tr><td><CopyableCode code="final_bake_time_in_minutes" /></td><td><code>number</code></td><td>Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. You must configure permissions for AWS AppConfig to roll back based on CloudWatch alarms. For more information, see Configuring permissions for rollback based on Amazon CloudWatch alarms in the AWS AppConfig User Guide.</td></tr>
<tr><td><CopyableCode code="growth_factor" /></td><td><code>number</code></td><td>The percentage of targets to receive a deployed configuration during each interval.</td></tr>
<tr><td><CopyableCode code="growth_type" /></td><td><code>string</code></td><td>The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types:<br />Linear: For this type, AWS AppConfig processes the deployment by dividing the total number of targets by the value specified for Step percentage. For example, a linear deployment that uses a Step percentage of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration.<br />Exponential: For this type, AWS AppConfig processes the deployment exponentially using the following formula: G*(2^N). In this formula, G is the growth factor specified by the user and N is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows:<br />2*(2^0)<br />2*(2^1)<br />2*(2^2)<br />Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the deployment strategy.</td></tr>
<tr><td><CopyableCode code="replicate_to" /></td><td><code>string</code></td><td>Save the deployment strategy to a Systems Manager (SSM) document.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Assigns metadata to an AWS AppConfig resource. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The deployment strategy ID.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html"><code>AWS::AppConfig::DeploymentStrategy</code></a>.

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
    <td><CopyableCode code="DeploymentDurationInMinutes, GrowthFactor, Name, ReplicateTo, region" /></td>
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
Gets all <code>deployment_strategies</code> in a region.
```sql
SELECT
region,
deployment_duration_in_minutes,
description,
final_bake_time_in_minutes,
growth_factor,
growth_type,
name,
replicate_to,
tags,
id
FROM aws.appconfig.deployment_strategies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>deployment_strategy</code>.
```sql
SELECT
region,
deployment_duration_in_minutes,
description,
final_bake_time_in_minutes,
growth_factor,
growth_type,
name,
replicate_to,
tags,
id
FROM aws.appconfig.deployment_strategies
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployment_strategy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appconfig.deployment_strategies (
 DeploymentDurationInMinutes,
 GrowthFactor,
 Name,
 ReplicateTo,
 region
)
SELECT 
'{{ DeploymentDurationInMinutes }}',
 '{{ GrowthFactor }}',
 '{{ Name }}',
 '{{ ReplicateTo }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appconfig.deployment_strategies (
 DeploymentDurationInMinutes,
 Description,
 FinalBakeTimeInMinutes,
 GrowthFactor,
 GrowthType,
 Name,
 ReplicateTo,
 Tags,
 region
)
SELECT 
 '{{ DeploymentDurationInMinutes }}',
 '{{ Description }}',
 '{{ FinalBakeTimeInMinutes }}',
 '{{ GrowthFactor }}',
 '{{ GrowthType }}',
 '{{ Name }}',
 '{{ ReplicateTo }}',
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
  - name: deployment_strategy
    props:
      - name: DeploymentDurationInMinutes
        value: null
      - name: Description
        value: '{{ Description }}'
      - name: FinalBakeTimeInMinutes
        value: null
      - name: GrowthFactor
        value: null
      - name: GrowthType
        value: '{{ GrowthType }}'
      - name: Name
        value: '{{ Name }}'
      - name: ReplicateTo
        value: '{{ ReplicateTo }}'
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
DELETE FROM aws.appconfig.deployment_strategies
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>deployment_strategies</code> resource, the following permissions are required:

### Create
```json
appconfig:CreateDeploymentStrategy,
appconfig:TagResource
```

### Read
```json
appconfig:GetDeploymentStrategy,
appconfig:ListTagsForResource
```

### Update
```json
appconfig:UpdateDeploymentStrategy,
appconfig:TagResource,
appconfig:UntagResource
```

### Delete
```json
appconfig:DeleteDeploymentStrategy
```

### List
```json
appconfig:ListDeploymentStrategies
```
