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


Used to retrieve a list of <code>applications</code> in a region or to create or delete a <code>applications</code> resource, use <code>application</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an Amazon Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see &#91;Creating an Application&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kinesisanalytics&#x2F;latest&#x2F;java&#x2F;getting-started.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesisanalyticsv2.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the application.</td></tr>
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
application_name
FROM aws.kinesisanalyticsv2.applications
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>application</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- application.iql (required properties only)
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
-- application.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
kinesisanalytics:DescribeApplication,
kinesisanalytics:DeleteApplication
```

### List
```json
kinesisanalytics:ListApplications
```

