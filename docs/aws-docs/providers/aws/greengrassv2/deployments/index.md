---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - greengrassv2
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
<tr><td><b>Description</b></td><td>Resource for Greengrass V2 deployment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.greengrassv2.deployments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="target_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="parent_target_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deployment_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deployment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="components" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="iot_job_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="deployment_policies" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="TargetArn, region" /></td>
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
target_arn,
parent_target_arn,
deployment_id,
deployment_name,
components,
iot_job_configuration,
deployment_policies,
tags
FROM aws.greengrassv2.deployments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>deployment</code>.
```sql
SELECT
region,
target_arn,
parent_target_arn,
deployment_id,
deployment_name,
components,
iot_job_configuration,
deployment_policies,
tags
FROM aws.greengrassv2.deployments
WHERE region = 'us-east-1' AND data__Identifier = '<DeploymentId>';
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
INSERT INTO aws.greengrassv2.deployments (
 TargetArn,
 region
)
SELECT 
'{{ TargetArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.greengrassv2.deployments (
 TargetArn,
 ParentTargetArn,
 DeploymentName,
 Components,
 IotJobConfiguration,
 DeploymentPolicies,
 Tags,
 region
)
SELECT 
 '{{ TargetArn }}',
 '{{ ParentTargetArn }}',
 '{{ DeploymentName }}',
 '{{ Components }}',
 '{{ IotJobConfiguration }}',
 '{{ DeploymentPolicies }}',
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
  - name: deployment
    props:
      - name: TargetArn
        value: '{{ TargetArn }}'
      - name: ParentTargetArn
        value: '{{ ParentTargetArn }}'
      - name: DeploymentName
        value: '{{ DeploymentName }}'
      - name: Components
        value: {}
      - name: IotJobConfiguration
        value:
          JobExecutionsRolloutConfig:
            ExponentialRate:
              BaseRatePerMinute: '{{ BaseRatePerMinute }}'
              IncrementFactor: null
              RateIncreaseCriteria: {}
            MaximumPerMinute: '{{ MaximumPerMinute }}'
          AbortConfig:
            CriteriaList:
              - FailureType: '{{ FailureType }}'
                Action: '{{ Action }}'
                ThresholdPercentage: null
                MinNumberOfExecutedThings: '{{ MinNumberOfExecutedThings }}'
          TimeoutConfig:
            InProgressTimeoutInMinutes: '{{ InProgressTimeoutInMinutes }}'
      - name: DeploymentPolicies
        value:
          FailureHandlingPolicy: '{{ FailureHandlingPolicy }}'
          ComponentUpdatePolicy:
            TimeoutInSeconds: '{{ TimeoutInSeconds }}'
            Action: '{{ Action }}'
          ConfigurationValidationPolicy:
            TimeoutInSeconds: '{{ TimeoutInSeconds }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.greengrassv2.deployments
WHERE data__Identifier = '<DeploymentId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>deployments</code> resource, the following permissions are required:

### Create
```json
greengrass:CreateDeployment,
greengrass:GetDeployment,
greengrass:TagResource,
iot:CancelJob,
iot:CreateJob,
iot:DeleteThingShadow,
iot:DescribeJob,
iot:DescribeThing,
iot:DescribeThingGroup,
iot:GetThingShadow,
iot:UpdateJob,
iot:UpdateThingShadow
```

### Read
```json
greengrass:GetDeployment,
iot:DescribeJob,
iot:DescribeThing,
iot:DescribeThingGroup,
iot:GetThingShadow
```

### Update
```json
greengrass:GetDeployment,
greengrass:TagResource,
greengrass:UntagResource,
iot:DescribeJob
```

### Delete
```json
greengrass:DeleteDeployment,
greengrass:CancelDeployment,
iot:CancelJob,
iot:DeleteJob,
iot:DescribeJob
```

### List
```json
greengrass:ListDeployments,
iot:DescribeJob,
iot:DescribeThing,
iot:DescribeThingGroup,
iot:GetThingShadow
```

