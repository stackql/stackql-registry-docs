---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - mwaa
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


Used to retrieve a list of <code>environments</code> in a region or to create or delete a <code>environments</code> resource, use <code>environment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MWAA::Environment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mwaa.environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>undefined</code></td><td></td></tr>
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
name
FROM aws.mwaa.environments
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
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.mwaa.environments (
 Name,
 region
)
SELECT 
{{ Name }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "ExecutionRoleArn": "{{ ExecutionRoleArn }}",
 "KmsKey": "{{ KmsKey }}",
 "AirflowVersion": "{{ AirflowVersion }}",
 "SourceBucketArn": "{{ SourceBucketArn }}",
 "DagS3Path": "{{ DagS3Path }}",
 "PluginsS3Path": null,
 "PluginsS3ObjectVersion": "{{ PluginsS3ObjectVersion }}",
 "RequirementsS3Path": null,
 "RequirementsS3ObjectVersion": null,
 "StartupScriptS3Path": null,
 "StartupScriptS3ObjectVersion": null,
 "AirflowConfigurationOptions": {},
 "EnvironmentClass": "{{ EnvironmentClass }}",
 "MaxWorkers": "{{ MaxWorkers }}",
 "MinWorkers": "{{ MinWorkers }}",
 "Schedulers": "{{ Schedulers }}",
 "NetworkConfiguration": {
  "SubnetIds": [
   "{{ SubnetIds[0] }}"
  ],
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ]
 },
 "LoggingConfiguration": {
  "DagProcessingLogs": {
   "Enabled": "{{ Enabled }}",
   "LogLevel": "{{ LogLevel }}",
   "CloudWatchLogGroupArn": "{{ CloudWatchLogGroupArn }}"
  },
  "SchedulerLogs": null,
  "WebserverLogs": null,
  "WorkerLogs": null,
  "TaskLogs": null
 },
 "WeeklyMaintenanceWindowStart": "{{ WeeklyMaintenanceWindowStart }}",
 "Tags": {},
 "WebserverAccessMode": "{{ WebserverAccessMode }}",
 "EndpointManagement": "{{ EndpointManagement }}"
}
>>>
--all properties
INSERT INTO aws.mwaa.environments (
 Name,
 ExecutionRoleArn,
 KmsKey,
 AirflowVersion,
 SourceBucketArn,
 DagS3Path,
 PluginsS3Path,
 PluginsS3ObjectVersion,
 RequirementsS3Path,
 RequirementsS3ObjectVersion,
 StartupScriptS3Path,
 StartupScriptS3ObjectVersion,
 AirflowConfigurationOptions,
 EnvironmentClass,
 MaxWorkers,
 MinWorkers,
 Schedulers,
 NetworkConfiguration,
 LoggingConfiguration,
 WeeklyMaintenanceWindowStart,
 Tags,
 WebserverAccessMode,
 EndpointManagement,
 region
)
SELECT 
 {{ Name }},
 {{ ExecutionRoleArn }},
 {{ KmsKey }},
 {{ AirflowVersion }},
 {{ SourceBucketArn }},
 {{ DagS3Path }},
 {{ PluginsS3Path }},
 {{ PluginsS3ObjectVersion }},
 {{ RequirementsS3Path }},
 {{ RequirementsS3ObjectVersion }},
 {{ StartupScriptS3Path }},
 {{ StartupScriptS3ObjectVersion }},
 {{ AirflowConfigurationOptions }},
 {{ EnvironmentClass }},
 {{ MaxWorkers }},
 {{ MinWorkers }},
 {{ Schedulers }},
 {{ NetworkConfiguration }},
 {{ LoggingConfiguration }},
 {{ WeeklyMaintenanceWindowStart }},
 {{ Tags }},
 {{ WebserverAccessMode }},
 {{ EndpointManagement }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.mwaa.environments
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environments</code> resource, the following permissions are required:

### Create
```json
airflow:CreateEnvironment
```

### Delete
```json
airflow:DeleteEnvironment
```

### List
```json
airflow:ListEnvironments
```

