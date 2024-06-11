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

Creates, updates, deletes or gets an <code>environment</code> resource or lists <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MWAA::Environment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mwaa.environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>Customer-defined identifier for the environment, unique per customer region.</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>ARN for the MWAA environment.</code></td><td></td></tr>
<tr><td><CopyableCode code="webserver_url" /></td><td><code>Url endpoint for the environment's Airflow UI.</code></td><td></td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>IAM role to be used by tasks.</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key" /></td><td><code>The identifier of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use for MWAA data encryption. You can specify the CMK using any of the following: Key ID. For example, key/1234abcd-12ab-34cd-56ef-1234567890ab. Key alias. For example, alias/ExampleAlias. Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef. Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias. AWS authenticates the CMK asynchronously. Therefore, if you specify an ID, alias, or ARN that is not valid, the action can appear to complete, but eventually fails.</code></td><td></td></tr>
<tr><td><CopyableCode code="airflow_version" /></td><td><code>Version of airflow to deploy to the environment.</code></td><td></td></tr>
<tr><td><CopyableCode code="source_bucket_arn" /></td><td><code>ARN for the AWS S3 bucket to use as the source of DAGs and plugins for the environment.</code></td><td></td></tr>
<tr><td><CopyableCode code="dag_s3_path" /></td><td><code>Represents an S3 prefix relative to the root of an S3 bucket.</code></td><td></td></tr>
<tr><td><CopyableCode code="plugins_s3_path" /></td><td><code>Represents an S3 prefix relative to the root of an S3 bucket.</code></td><td></td></tr>
<tr><td><CopyableCode code="plugins_s3_object_version" /></td><td><code>Represents an version ID for an S3 object.</code></td><td></td></tr>
<tr><td><CopyableCode code="requirements_s3_path" /></td><td><code>Represents an S3 prefix relative to the root of an S3 bucket.</code></td><td></td></tr>
<tr><td><CopyableCode code="requirements_s3_object_version" /></td><td><code>Represents an version ID for an S3 object.</code></td><td></td></tr>
<tr><td><CopyableCode code="startup_script_s3_path" /></td><td><code>Represents an S3 prefix relative to the root of an S3 bucket.</code></td><td></td></tr>
<tr><td><CopyableCode code="startup_script_s3_object_version" /></td><td><code>Represents an version ID for an S3 object.</code></td><td></td></tr>
<tr><td><CopyableCode code="airflow_configuration_options" /></td><td><code>object</code></td><td>Key/value pairs representing Airflow configuration variables. Keys are prefixed by their section: &#91;core&#93; dags_folder=&#123;AIRFLOW_HOME&#125;/dags Would be represented as "core.dags_folder": "&#123;AIRFLOW_HOME&#125;/dags"</td></tr>
<tr><td><CopyableCode code="environment_class" /></td><td><code>Templated configuration for airflow processes and backing infrastructure.</code></td><td></td></tr>
<tr><td><CopyableCode code="max_workers" /></td><td><code>Maximum worker compute units.</code></td><td></td></tr>
<tr><td><CopyableCode code="min_workers" /></td><td><code>Minimum worker compute units.</code></td><td></td></tr>
<tr><td><CopyableCode code="max_webservers" /></td><td><code>Maximum webserver compute units.</code></td><td></td></tr>
<tr><td><CopyableCode code="min_webservers" /></td><td><code>Minimum webserver compute units.</code></td><td></td></tr>
<tr><td><CopyableCode code="schedulers" /></td><td><code>Scheduler compute units.</code></td><td></td></tr>
<tr><td><CopyableCode code="network_configuration" /></td><td><code>Configures the network resources of the environment.</code></td><td></td></tr>
<tr><td><CopyableCode code="logging_configuration" /></td><td><code>Logging configuration for the environment.</code></td><td></td></tr>
<tr><td><CopyableCode code="weekly_maintenance_window_start" /></td><td><code>Start time for the weekly maintenance window.</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of tags for the environment.</td></tr>
<tr><td><CopyableCode code="webserver_access_mode" /></td><td><code>Choice for mode of webserver access including over public internet or via private VPC endpoint.</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_management" /></td><td><code>Defines whether the VPC endpoints configured for the environment are created, and managed, by the customer or by Amazon MWAA.</code></td><td></td></tr>
<tr><td><CopyableCode code="celery_executor_queue" /></td><td><code>The celery executor queue associated with the environment.</code></td><td></td></tr>
<tr><td><CopyableCode code="database_vpc_endpoint_service" /></td><td><code>The database VPC endpoint service name.</code></td><td></td></tr>
<tr><td><CopyableCode code="webserver_vpc_endpoint_service" /></td><td><code>The webserver VPC endpoint service name, applicable if private webserver access mode selected.</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, region" /></td>
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
List all <code>environments</code> in a region.
```sql
SELECT
region,
name
FROM aws.mwaa.environments
WHERE region = 'us-east-1';
```
Gets all properties from an <code>environment</code>.
```sql
SELECT
region,
name,
arn,
webserver_url,
execution_role_arn,
kms_key,
airflow_version,
source_bucket_arn,
dag_s3_path,
plugins_s3_path,
plugins_s3_object_version,
requirements_s3_path,
requirements_s3_object_version,
startup_script_s3_path,
startup_script_s3_object_version,
airflow_configuration_options,
environment_class,
max_workers,
min_workers,
max_webservers,
min_webservers,
schedulers,
network_configuration,
logging_configuration,
weekly_maintenance_window_start,
tags,
webserver_access_mode,
endpoint_management,
celery_executor_queue,
database_vpc_endpoint_service,
webserver_vpc_endpoint_service
FROM aws.mwaa.environments
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mwaa.environments (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 MaxWebservers,
 MinWebservers,
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
 '{{ Name }}',
 '{{ ExecutionRoleArn }}',
 '{{ KmsKey }}',
 '{{ AirflowVersion }}',
 '{{ SourceBucketArn }}',
 '{{ DagS3Path }}',
 '{{ PluginsS3Path }}',
 '{{ PluginsS3ObjectVersion }}',
 '{{ RequirementsS3Path }}',
 '{{ RequirementsS3ObjectVersion }}',
 '{{ StartupScriptS3Path }}',
 '{{ StartupScriptS3ObjectVersion }}',
 '{{ AirflowConfigurationOptions }}',
 '{{ EnvironmentClass }}',
 '{{ MaxWorkers }}',
 '{{ MinWorkers }}',
 '{{ MaxWebservers }}',
 '{{ MinWebservers }}',
 '{{ Schedulers }}',
 '{{ NetworkConfiguration }}',
 '{{ LoggingConfiguration }}',
 '{{ WeeklyMaintenanceWindowStart }}',
 '{{ Tags }}',
 '{{ WebserverAccessMode }}',
 '{{ EndpointManagement }}',
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
  - name: environment
    props:
      - name: Name
        value: '{{ Name }}'
      - name: ExecutionRoleArn
        value: '{{ ExecutionRoleArn }}'
      - name: KmsKey
        value: '{{ KmsKey }}'
      - name: AirflowVersion
        value: '{{ AirflowVersion }}'
      - name: SourceBucketArn
        value: '{{ SourceBucketArn }}'
      - name: DagS3Path
        value: '{{ DagS3Path }}'
      - name: PluginsS3Path
        value: null
      - name: PluginsS3ObjectVersion
        value: '{{ PluginsS3ObjectVersion }}'
      - name: RequirementsS3Path
        value: null
      - name: RequirementsS3ObjectVersion
        value: null
      - name: StartupScriptS3Path
        value: null
      - name: StartupScriptS3ObjectVersion
        value: null
      - name: AirflowConfigurationOptions
        value: {}
      - name: EnvironmentClass
        value: '{{ EnvironmentClass }}'
      - name: MaxWorkers
        value: '{{ MaxWorkers }}'
      - name: MinWorkers
        value: '{{ MinWorkers }}'
      - name: MaxWebservers
        value: '{{ MaxWebservers }}'
      - name: MinWebservers
        value: '{{ MinWebservers }}'
      - name: Schedulers
        value: '{{ Schedulers }}'
      - name: NetworkConfiguration
        value:
          SubnetIds:
            - '{{ SubnetIds[0] }}'
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
      - name: LoggingConfiguration
        value:
          DagProcessingLogs:
            Enabled: '{{ Enabled }}'
            LogLevel: '{{ LogLevel }}'
            CloudWatchLogGroupArn: '{{ CloudWatchLogGroupArn }}'
          SchedulerLogs: null
          WebserverLogs: null
          WorkerLogs: null
          TaskLogs: null
      - name: WeeklyMaintenanceWindowStart
        value: '{{ WeeklyMaintenanceWindowStart }}'
      - name: Tags
        value: {}
      - name: WebserverAccessMode
        value: '{{ WebserverAccessMode }}'
      - name: EndpointManagement
        value: '{{ EndpointManagement }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
airflow:GetEnvironment
```

### Update
```json
airflow:UpdateEnvironment,
airflow:TagResource,
airflow:UntagResource
```

### Delete
```json
airflow:DeleteEnvironment
```

### List
```json
airflow:ListEnvironments
```

