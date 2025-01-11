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
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Customer-defined identifier for the environment, unique per customer region.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN for the MWAA environment.</td></tr>
<tr><td><CopyableCode code="webserver_url" /></td><td><code>string</code></td><td>Url endpoint for the environment's Airflow UI.</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>IAM role to be used by tasks.</td></tr>
<tr><td><CopyableCode code="kms_key" /></td><td><code>string</code></td><td>The identifier of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use for MWAA data encryption.<br />You can specify the CMK using any of the following:<br />Key ID. For example, key/1234abcd-12ab-34cd-56ef-1234567890ab.<br />Key alias. For example, alias/ExampleAlias.<br />Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef.<br />Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.<br />AWS authenticates the CMK asynchronously. Therefore, if you specify an ID, alias, or ARN that is not valid, the action can appear to complete, but eventually fails.</td></tr>
<tr><td><CopyableCode code="airflow_version" /></td><td><code>string</code></td><td>Version of airflow to deploy to the environment.</td></tr>
<tr><td><CopyableCode code="source_bucket_arn" /></td><td><code>string</code></td><td>ARN for the AWS S3 bucket to use as the source of DAGs and plugins for the environment.</td></tr>
<tr><td><CopyableCode code="dag_s3_path" /></td><td><code>string</code></td><td>Represents an S3 prefix relative to the root of an S3 bucket.</td></tr>
<tr><td><CopyableCode code="plugins_s3_path" /></td><td><code>string</code></td><td>Represents an S3 prefix relative to the root of an S3 bucket.</td></tr>
<tr><td><CopyableCode code="plugins_s3_object_version" /></td><td><code>string</code></td><td>Represents an version ID for an S3 object.</td></tr>
<tr><td><CopyableCode code="requirements_s3_path" /></td><td><code>string</code></td><td>Represents an S3 prefix relative to the root of an S3 bucket.</td></tr>
<tr><td><CopyableCode code="requirements_s3_object_version" /></td><td><code>string</code></td><td>Represents an version ID for an S3 object.</td></tr>
<tr><td><CopyableCode code="startup_script_s3_path" /></td><td><code>string</code></td><td>Represents an S3 prefix relative to the root of an S3 bucket.</td></tr>
<tr><td><CopyableCode code="startup_script_s3_object_version" /></td><td><code>string</code></td><td>Represents an version ID for an S3 object.</td></tr>
<tr><td><CopyableCode code="airflow_configuration_options" /></td><td><code>object</code></td><td>Key/value pairs representing Airflow configuration variables.<br />Keys are prefixed by their section:<br />&#91;core&#93;<br />dags_folder=&#123;AIRFLOW_HOME&#125;/dags<br />Would be represented as<br />"core.dags_folder": "&#123;AIRFLOW_HOME&#125;/dags"</td></tr>
<tr><td><CopyableCode code="environment_class" /></td><td><code>string</code></td><td>Templated configuration for airflow processes and backing infrastructure.</td></tr>
<tr><td><CopyableCode code="max_workers" /></td><td><code>integer</code></td><td>Maximum worker compute units.</td></tr>
<tr><td><CopyableCode code="min_workers" /></td><td><code>integer</code></td><td>Minimum worker compute units.</td></tr>
<tr><td><CopyableCode code="max_webservers" /></td><td><code>integer</code></td><td>Maximum webserver compute units.</td></tr>
<tr><td><CopyableCode code="min_webservers" /></td><td><code>integer</code></td><td>Minimum webserver compute units.</td></tr>
<tr><td><CopyableCode code="schedulers" /></td><td><code>integer</code></td><td>Scheduler compute units.</td></tr>
<tr><td><CopyableCode code="network_configuration" /></td><td><code>object</code></td><td>Configures the network resources of the environment.</td></tr>
<tr><td><CopyableCode code="logging_configuration" /></td><td><code>object</code></td><td>Logging configuration for the environment.</td></tr>
<tr><td><CopyableCode code="weekly_maintenance_window_start" /></td><td><code>string</code></td><td>Start time for the weekly maintenance window.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of tags for the environment.</td></tr>
<tr><td><CopyableCode code="webserver_access_mode" /></td><td><code>string</code></td><td>Choice for mode of webserver access including over public internet or via private VPC endpoint.</td></tr>
<tr><td><CopyableCode code="endpoint_management" /></td><td><code>string</code></td><td>Defines whether the VPC endpoints configured for the environment are created, and managed, by the customer or by Amazon MWAA.</td></tr>
<tr><td><CopyableCode code="celery_executor_queue" /></td><td><code>string</code></td><td>The celery executor queue associated with the environment.</td></tr>
<tr><td><CopyableCode code="database_vpc_endpoint_service" /></td><td><code>string</code></td><td>The database VPC endpoint service name.</td></tr>
<tr><td><CopyableCode code="webserver_vpc_endpoint_service" /></td><td><code>string</code></td><td>The webserver VPC endpoint service name, applicable if private webserver access mode selected.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html"><code>AWS::MWAA::Environment</code></a>.

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
Gets all <code>environments</code> in a region.
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
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>environment</code>.
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
