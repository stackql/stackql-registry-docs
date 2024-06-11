---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - kinesisanalyticsv2
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

Creates, updates, deletes or gets an <code>application</code> resource or lists <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an Amazon Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see &#91;Creating an Application&#93;(https://docs.aws.amazon.com/kinesisanalytics/latest/java/getting-started.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesisanalyticsv2.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_configuration" /></td><td><code>object</code></td><td>Use this parameter to configure the application.</td></tr>
<tr><td><CopyableCode code="application_description" /></td><td><code>string</code></td><td>The description of the application.</td></tr>
<tr><td><CopyableCode code="application_mode" /></td><td><code>string</code></td><td>To create a Kinesis Data Analytics Studio notebook, you must set the mode to `INTERACTIVE`. However, for a Kinesis Data Analytics for Apache Flink application, the mode is optional.</td></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the application.</td></tr>
<tr><td><CopyableCode code="runtime_environment" /></td><td><code>string</code></td><td>The runtime environment for the application.</td></tr>
<tr><td><CopyableCode code="service_execution_role" /></td><td><code>string</code></td><td>Specifies the IAM role that the application uses to access external resources.</td></tr>
<tr><td><CopyableCode code="run_configuration" /></td><td><code>object</code></td><td>Specifies run configuration (start parameters) of a Kinesis Data Analytics application. Evaluated on update for RUNNING applications an only.</td></tr>
<tr><td><CopyableCode code="application_maintenance_configuration" /></td><td><code>object</code></td><td>Used to configure start of maintenance window.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.</td></tr>
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
    <td><CopyableCode code="RuntimeEnvironment, ServiceExecutionRole, region" /></td>
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
List all <code>applications</code> in a region.
```sql
SELECT
region,
application_name
FROM aws.kinesisanalyticsv2.applications
WHERE region = 'us-east-1';
```
Gets all properties from an <code>application</code>.
```sql
SELECT
region,
application_configuration,
application_description,
application_mode,
application_name,
runtime_environment,
service_execution_role,
run_configuration,
application_maintenance_configuration,
tags
FROM aws.kinesisanalyticsv2.applications
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.kinesisanalyticsv2.applications (
 RuntimeEnvironment,
 ServiceExecutionRole,
 region
)
SELECT 
'{{ RuntimeEnvironment }}',
 '{{ ServiceExecutionRole }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.kinesisanalyticsv2.applications (
 ApplicationConfiguration,
 ApplicationDescription,
 ApplicationMode,
 ApplicationName,
 RuntimeEnvironment,
 ServiceExecutionRole,
 RunConfiguration,
 ApplicationMaintenanceConfiguration,
 Tags,
 region
)
SELECT 
 '{{ ApplicationConfiguration }}',
 '{{ ApplicationDescription }}',
 '{{ ApplicationMode }}',
 '{{ ApplicationName }}',
 '{{ RuntimeEnvironment }}',
 '{{ ServiceExecutionRole }}',
 '{{ RunConfiguration }}',
 '{{ ApplicationMaintenanceConfiguration }}',
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
  - name: application
    props:
      - name: ApplicationConfiguration
        value:
          ApplicationCodeConfiguration:
            CodeContent:
              ZipFileContent: '{{ ZipFileContent }}'
              S3ContentLocation:
                BucketARN: '{{ BucketARN }}'
                FileKey: '{{ FileKey }}'
                ObjectVersion: '{{ ObjectVersion }}'
              TextContent: '{{ TextContent }}'
            CodeContentType: '{{ CodeContentType }}'
          ApplicationSnapshotConfiguration:
            SnapshotsEnabled: '{{ SnapshotsEnabled }}'
          EnvironmentProperties:
            PropertyGroups:
              - PropertyGroupId: '{{ PropertyGroupId }}'
                PropertyMap: {}
          FlinkApplicationConfiguration:
            CheckpointConfiguration:
              ConfigurationType: '{{ ConfigurationType }}'
              CheckpointingEnabled: '{{ CheckpointingEnabled }}'
              CheckpointInterval: '{{ CheckpointInterval }}'
              MinPauseBetweenCheckpoints: '{{ MinPauseBetweenCheckpoints }}'
            MonitoringConfiguration:
              ConfigurationType: '{{ ConfigurationType }}'
              MetricsLevel: '{{ MetricsLevel }}'
              LogLevel: '{{ LogLevel }}'
            ParallelismConfiguration:
              ConfigurationType: '{{ ConfigurationType }}'
              ParallelismPerKPU: '{{ ParallelismPerKPU }}'
              Parallelism: '{{ Parallelism }}'
              AutoScalingEnabled: '{{ AutoScalingEnabled }}'
          SqlApplicationConfiguration:
            Inputs:
              - NamePrefix: '{{ NamePrefix }}'
                InputSchema:
                  RecordEncoding: '{{ RecordEncoding }}'
                  RecordColumns:
                    - Mapping: '{{ Mapping }}'
                      Name: '{{ Name }}'
                      SqlType: '{{ SqlType }}'
                  RecordFormat:
                    RecordFormatType: '{{ RecordFormatType }}'
                    MappingParameters:
                      CSVMappingParameters:
                        RecordColumnDelimiter: '{{ RecordColumnDelimiter }}'
                        RecordRowDelimiter: '{{ RecordRowDelimiter }}'
                      JSONMappingParameters:
                        RecordRowPath: '{{ RecordRowPath }}'
                KinesisStreamsInput:
                  ResourceARN: null
                KinesisFirehoseInput:
                  ResourceARN: null
                InputProcessingConfiguration:
                  InputLambdaProcessor:
                    ResourceARN: null
                InputParallelism:
                  Count: '{{ Count }}'
          ZeppelinApplicationConfiguration:
            CatalogConfiguration:
              GlueDataCatalogConfiguration:
                DatabaseARN: null
            MonitoringConfiguration:
              LogLevel: '{{ LogLevel }}'
            DeployAsApplicationConfiguration:
              S3ContentLocation:
                BucketARN: null
                BasePath: '{{ BasePath }}'
            CustomArtifactsConfiguration:
              - ArtifactType: '{{ ArtifactType }}'
                MavenReference:
                  ArtifactId: '{{ ArtifactId }}'
                  GroupId: '{{ GroupId }}'
                  Version: '{{ Version }}'
                S3ContentLocation: null
          VpcConfigurations:
            - SecurityGroupIds:
                - '{{ SecurityGroupIds[0] }}'
              SubnetIds:
                - '{{ SubnetIds[0] }}'
      - name: ApplicationDescription
        value: '{{ ApplicationDescription }}'
      - name: ApplicationMode
        value: '{{ ApplicationMode }}'
      - name: ApplicationName
        value: '{{ ApplicationName }}'
      - name: RuntimeEnvironment
        value: '{{ RuntimeEnvironment }}'
      - name: ServiceExecutionRole
        value: null
      - name: RunConfiguration
        value:
          ApplicationRestoreConfiguration:
            ApplicationRestoreType: '{{ ApplicationRestoreType }}'
            SnapshotName: '{{ SnapshotName }}'
          FlinkRunConfiguration:
            AllowNonRestoredState: '{{ AllowNonRestoredState }}'
      - name: ApplicationMaintenanceConfiguration
        value:
          ApplicationMaintenanceWindowStartTime: '{{ ApplicationMaintenanceWindowStartTime }}'
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
DELETE FROM aws.kinesisanalyticsv2.applications
WHERE data__Identifier = '<ApplicationName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
kinesisanalytics:CreateApplication,
kinesisanalytics:DescribeApplication,
kinesisanalytics:ListTagsForResource,
kinesisanalytics:UpdateApplicationMaintenanceConfiguration
```

### Read
```json
kinesisanalytics:DescribeApplication,
kinesisanalytics:ListTagsForResource
```

### Update
```json
kinesisanalytics:UpdateApplication,
kinesisanalytics:DescribeApplication,
kinesisanalytics:TagResource,
kinesisanalytics:UntagResource,
kinesisanalytics:AddApplicationVpcConfiguration,
kinesisanalytics:DeleteApplicationVpcConfiguration,
kinesisanalytics:UpdateApplicationMaintenanceConfiguration,
kinesisanalytics:ListTagsForResource
```

### Delete
```json
kinesisanalytics:DescribeApplication,
kinesisanalytics:DeleteApplication
```

### List
```json
kinesisanalytics:ListApplications
```

