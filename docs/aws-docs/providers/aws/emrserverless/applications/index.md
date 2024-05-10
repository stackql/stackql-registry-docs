---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - emrserverless
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


Used to retrieve a list of <code>applications</code> in a region or to create or delete a <code>applications</code> resource, use <code>application</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EMRServerless::Application Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emrserverless.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The ID of the EMR Serverless Application.</td></tr>
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
application_id
FROM aws.emrserverless.applications
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
 "ReleaseLabel": "{{ ReleaseLabel }}",
 "Type": "{{ Type }}"
}
>>>
--required properties only
INSERT INTO aws.emrserverless.applications (
 ReleaseLabel,
 Type,
 region
)
SELECT 
{{ ReleaseLabel }},
 {{ Type }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Architecture": "{{ Architecture }}",
 "Name": "{{ Name }}",
 "ReleaseLabel": "{{ ReleaseLabel }}",
 "Type": "{{ Type }}",
 "InitialCapacity": [
  {
   "Key": "{{ Key }}",
   "Value": {
    "WorkerCount": "{{ WorkerCount }}",
    "WorkerConfiguration": {
     "Cpu": "{{ Cpu }}",
     "Memory": "{{ Memory }}",
     "Disk": "{{ Disk }}"
    }
   }
  }
 ],
 "MaximumCapacity": {
  "Cpu": null,
  "Memory": null,
  "Disk": null
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "AutoStartConfiguration": {
  "Enabled": "{{ Enabled }}"
 },
 "AutoStopConfiguration": {
  "Enabled": "{{ Enabled }}",
  "IdleTimeoutMinutes": "{{ IdleTimeoutMinutes }}"
 },
 "ImageConfiguration": {
  "ImageUri": "{{ ImageUri }}"
 },
 "MonitoringConfiguration": {
  "S3MonitoringConfiguration": null,
  "ManagedPersistenceMonitoringConfiguration": null,
  "CloudWatchLoggingConfiguration": null
 },
 "RuntimeConfiguration": [
  {
   "Classification": "{{ Classification }}",
   "Properties": {},
   "Configurations": [
    null
   ]
  }
 ],
 "NetworkConfiguration": {
  "SubnetIds": [
   "{{ SubnetIds[0] }}"
  ],
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ]
 },
 "WorkerTypeSpecifications": {}
}
>>>
--all properties
INSERT INTO aws.emrserverless.applications (
 Architecture,
 Name,
 ReleaseLabel,
 Type,
 InitialCapacity,
 MaximumCapacity,
 Tags,
 AutoStartConfiguration,
 AutoStopConfiguration,
 ImageConfiguration,
 MonitoringConfiguration,
 RuntimeConfiguration,
 NetworkConfiguration,
 WorkerTypeSpecifications,
 region
)
SELECT 
 {{ Architecture }},
 {{ Name }},
 {{ ReleaseLabel }},
 {{ Type }},
 {{ InitialCapacity }},
 {{ MaximumCapacity }},
 {{ Tags }},
 {{ AutoStartConfiguration }},
 {{ AutoStopConfiguration }},
 {{ ImageConfiguration }},
 {{ MonitoringConfiguration }},
 {{ RuntimeConfiguration }},
 {{ NetworkConfiguration }},
 {{ WorkerTypeSpecifications }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.emrserverless.applications
WHERE data__Identifier = '<ApplicationId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
kms:Create*,
kms:Describe*,
kms:Enable*,
kms:List*,
kms:Put*,
kms:Update*,
kms:Revoke*,
kms:Disable*,
kms:Get*,
kms:Delete*,
kms:ScheduleKeyDeletion,
kms:CancelKeyDeletion,
kms:GenerateDataKey,
kms:TagResource,
kms:UntagResource,
kms:Decrypt,
emr-serverless:CreateApplication,
emr-serverless:TagResource,
emr-serverless:GetApplication,
iam:CreateServiceLinkedRole,
ec2:CreateNetworkInterface,
ecr:BatchGetImage,
ecr:DescribeImages,
ecr:GetDownloadUrlForLayer
```

### Delete
```json
emr-serverless:DeleteApplication,
emr-serverless:GetApplication
```

### List
```json
emr-serverless:ListApplications
```

