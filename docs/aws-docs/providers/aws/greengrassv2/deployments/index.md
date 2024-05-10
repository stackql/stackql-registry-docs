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


Used to retrieve a list of <code>deployments</code> in a region or to create or delete a <code>deployments</code> resource, use <code>deployment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource for Greengrass V2 deployment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.greengrassv2.deployments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="deployment_id" /></td><td><code>string</code></td><td></td></tr>
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
deployment_id
FROM aws.greengrassv2.deployments
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "TargetArn": "{{ TargetArn }}"
}
>>>
--required properties only
INSERT INTO aws.greengrassv2.deployments (
 TargetArn,
 region
)
SELECT 
{{ .TargetArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "TargetArn": "{{ TargetArn }}",
 "ParentTargetArn": "{{ ParentTargetArn }}",
 "DeploymentName": "{{ DeploymentName }}",
 "Components": {},
 "IotJobConfiguration": {
  "JobExecutionsRolloutConfig": {
   "ExponentialRate": {
    "BaseRatePerMinute": "{{ BaseRatePerMinute }}",
    "IncrementFactor": null,
    "RateIncreaseCriteria": {}
   },
   "MaximumPerMinute": "{{ MaximumPerMinute }}"
  },
  "AbortConfig": {
   "CriteriaList": [
    {
     "FailureType": "{{ FailureType }}",
     "Action": "{{ Action }}",
     "ThresholdPercentage": null,
     "MinNumberOfExecutedThings": "{{ MinNumberOfExecutedThings }}"
    }
   ]
  },
  "TimeoutConfig": {
   "InProgressTimeoutInMinutes": "{{ InProgressTimeoutInMinutes }}"
  }
 },
 "DeploymentPolicies": {
  "FailureHandlingPolicy": "{{ FailureHandlingPolicy }}",
  "ComponentUpdatePolicy": {
   "TimeoutInSeconds": "{{ TimeoutInSeconds }}",
   "Action": "{{ Action }}"
  },
  "ConfigurationValidationPolicy": {
   "TimeoutInSeconds": "{{ TimeoutInSeconds }}"
  }
 },
 "Tags": {}
}
>>>
--all properties
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
 {{ .TargetArn }},
 {{ .ParentTargetArn }},
 {{ .DeploymentName }},
 {{ .Components }},
 {{ .IotJobConfiguration }},
 {{ .DeploymentPolicies }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

