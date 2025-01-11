---
title: flows
hide_title: false
hide_table_of_contents: false
keywords:
  - flows
  - appflow
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

Creates, updates, deletes or gets a <code>flow</code> resource or lists <code>flows</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::AppFlow::Flow.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appflow.flows" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>ARN identifier of the flow.</td></tr>
<tr><td><CopyableCode code="flow_name" /></td><td><code>string</code></td><td>Name of the flow.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the flow.</td></tr>
<tr><td><CopyableCode code="kms_arn" /></td><td><code>string</code></td><td>The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.</td></tr>
<tr><td><CopyableCode code="trigger_config" /></td><td><code>object</code></td><td>Trigger settings of the flow.</td></tr>
<tr><td><CopyableCode code="flow_status" /></td><td><code>string</code></td><td>Flow activation status for Scheduled- and Event-triggered flows</td></tr>
<tr><td><CopyableCode code="source_flow_config" /></td><td><code>object</code></td><td>Configurations of Source connector of the flow.</td></tr>
<tr><td><CopyableCode code="destination_flow_config_list" /></td><td><code>array</code></td><td>List of Destination connectors of the flow.</td></tr>
<tr><td><CopyableCode code="tasks" /></td><td><code>array</code></td><td>List of tasks for the flow.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>List of Tags.</td></tr>
<tr><td><CopyableCode code="metadata_catalog_config" /></td><td><code>object</code></td><td>Configurations of metadata catalog of the flow.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html"><code>AWS::AppFlow::Flow</code></a>.

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
    <td><CopyableCode code="FlowName, Tasks, SourceFlowConfig, DestinationFlowConfigList, TriggerConfig, region" /></td>
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
Gets all <code>flows</code> in a region.
```sql
SELECT
region,
flow_arn,
flow_name,
description,
kms_arn,
trigger_config,
flow_status,
source_flow_config,
destination_flow_config_list,
tasks,
tags,
metadata_catalog_config
FROM aws.appflow.flows
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>flow</code>.
```sql
SELECT
region,
flow_arn,
flow_name,
description,
kms_arn,
trigger_config,
flow_status,
source_flow_config,
destination_flow_config_list,
tasks,
tags,
metadata_catalog_config
FROM aws.appflow.flows
WHERE region = 'us-east-1' AND data__Identifier = '<FlowName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flow</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appflow.flows (
 FlowName,
 TriggerConfig,
 SourceFlowConfig,
 DestinationFlowConfigList,
 Tasks,
 region
)
SELECT 
'{{ FlowName }}',
 '{{ TriggerConfig }}',
 '{{ SourceFlowConfig }}',
 '{{ DestinationFlowConfigList }}',
 '{{ Tasks }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appflow.flows (
 FlowName,
 Description,
 KMSArn,
 TriggerConfig,
 FlowStatus,
 SourceFlowConfig,
 DestinationFlowConfigList,
 Tasks,
 Tags,
 MetadataCatalogConfig,
 region
)
SELECT 
 '{{ FlowName }}',
 '{{ Description }}',
 '{{ KMSArn }}',
 '{{ TriggerConfig }}',
 '{{ FlowStatus }}',
 '{{ SourceFlowConfig }}',
 '{{ DestinationFlowConfigList }}',
 '{{ Tasks }}',
 '{{ Tags }}',
 '{{ MetadataCatalogConfig }}',
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
  - name: flow
    props:
      - name: FlowName
        value: '{{ FlowName }}'
      - name: Description
        value: '{{ Description }}'
      - name: KMSArn
        value: '{{ KMSArn }}'
      - name: TriggerConfig
        value:
          TriggerType: '{{ TriggerType }}'
          TriggerProperties:
            ScheduleExpression: '{{ ScheduleExpression }}'
            DataPullMode: '{{ DataPullMode }}'
            ScheduleStartTime: null
            ScheduleEndTime: null
            FirstExecutionFrom: null
            TimeZone: '{{ TimeZone }}'
            ScheduleOffset: null
            FlowErrorDeactivationThreshold: '{{ FlowErrorDeactivationThreshold }}'
      - name: FlowStatus
        value: '{{ FlowStatus }}'
      - name: SourceFlowConfig
        value:
          ConnectorType: '{{ ConnectorType }}'
          ApiVersion: '{{ ApiVersion }}'
          ConnectorProfileName: '{{ ConnectorProfileName }}'
          SourceConnectorProperties:
            Amplitude:
              Object: '{{ Object }}'
            Datadog:
              Object: null
            Dynatrace:
              Object: null
            GoogleAnalytics:
              Object: null
            InforNexus:
              Object: null
            Marketo:
              Object: null
            S3:
              BucketName: '{{ BucketName }}'
              BucketPrefix: '{{ BucketPrefix }}'
              S3InputFormatConfig:
                S3InputFileType: '{{ S3InputFileType }}'
            SAPOData:
              ObjectPath: null
              parallelismConfig:
                maxParallelism: '{{ maxParallelism }}'
              paginationConfig:
                maxPageSize: '{{ maxPageSize }}'
            Salesforce:
              Object: null
              EnableDynamicFieldUpdate: '{{ EnableDynamicFieldUpdate }}'
              IncludeDeletedRecords: '{{ IncludeDeletedRecords }}'
              DataTransferApi: '{{ DataTransferApi }}'
            Pardot:
              Object: null
            ServiceNow:
              Object: null
            Singular:
              Object: null
            Slack:
              Object: null
            Trendmicro:
              Object: null
            Veeva:
              Object: null
              DocumentType: '{{ DocumentType }}'
              IncludeSourceFiles: '{{ IncludeSourceFiles }}'
              IncludeRenditions: '{{ IncludeRenditions }}'
              IncludeAllVersions: '{{ IncludeAllVersions }}'
            Zendesk:
              Object: null
            CustomConnector:
              EntityName: '{{ EntityName }}'
              CustomProperties: {}
              DataTransferApi:
                Name: '{{ Name }}'
                Type: '{{ Type }}'
          IncrementalPullConfig:
            DatetimeTypeFieldName: '{{ DatetimeTypeFieldName }}'
      - name: DestinationFlowConfigList
        value:
          - ConnectorType: null
            ApiVersion: null
            ConnectorProfileName: null
            DestinationConnectorProperties:
              Redshift:
                Object: null
                IntermediateBucketName: null
                BucketPrefix: null
                ErrorHandlingConfig:
                  FailOnFirstError: '{{ FailOnFirstError }}'
                  BucketPrefix: null
                  BucketName: null
              S3:
                BucketName: null
                BucketPrefix: null
                S3OutputFormatConfig:
                  FileType: '{{ FileType }}'
                  PrefixConfig:
                    PrefixType: '{{ PrefixType }}'
                    PrefixFormat: '{{ PrefixFormat }}'
                    PathPrefixHierarchy:
                      - '{{ PathPrefixHierarchy[0] }}'
                  AggregationConfig:
                    AggregationType: '{{ AggregationType }}'
                    TargetFileSize: '{{ TargetFileSize }}'
                  PreserveSourceDataTyping: '{{ PreserveSourceDataTyping }}'
              Salesforce:
                Object: null
                ErrorHandlingConfig: null
                IdFieldNames:
                  - '{{ IdFieldNames[0] }}'
                WriteOperationType: '{{ WriteOperationType }}'
                DataTransferApi: null
              Snowflake:
                Object: null
                IntermediateBucketName: null
                BucketPrefix: null
                ErrorHandlingConfig: null
              EventBridge:
                Object: null
                ErrorHandlingConfig: null
              Upsolver:
                BucketName: '{{ BucketName }}'
                BucketPrefix: null
                S3OutputFormatConfig:
                  FileType: null
                  PrefixConfig: null
                  AggregationConfig: null
              LookoutMetrics:
                Object: null
              Marketo:
                Object: null
                ErrorHandlingConfig: null
              Zendesk:
                Object: null
                ErrorHandlingConfig: null
                IdFieldNames:
                  - '{{ IdFieldNames[0] }}'
                WriteOperationType: null
              CustomConnector:
                EntityName: null
                ErrorHandlingConfig: null
                WriteOperationType: null
                IdFieldNames:
                  - '{{ IdFieldNames[0] }}'
                CustomProperties: null
              SAPOData:
                ObjectPath: null
                ErrorHandlingConfig: null
                SuccessResponseHandlingConfig:
                  BucketPrefix: null
                  BucketName: null
                IdFieldNames:
                  - '{{ IdFieldNames[0] }}'
                WriteOperationType: null
      - name: Tasks
        value:
          - SourceFields:
              - '{{ SourceFields[0] }}'
            ConnectorOperator:
              Amplitude: '{{ Amplitude }}'
              Datadog: '{{ Datadog }}'
              Dynatrace: '{{ Dynatrace }}'
              GoogleAnalytics: '{{ GoogleAnalytics }}'
              InforNexus: '{{ InforNexus }}'
              Marketo: '{{ Marketo }}'
              S3: '{{ S3 }}'
              SAPOData: '{{ SAPOData }}'
              Salesforce: '{{ Salesforce }}'
              Pardot: '{{ Pardot }}'
              ServiceNow: '{{ ServiceNow }}'
              Singular: '{{ Singular }}'
              Slack: '{{ Slack }}'
              Trendmicro: '{{ Trendmicro }}'
              Veeva: '{{ Veeva }}'
              Zendesk: '{{ Zendesk }}'
              CustomConnector: '{{ CustomConnector }}'
            DestinationField: '{{ DestinationField }}'
            TaskType: '{{ TaskType }}'
            TaskProperties:
              - Key: '{{ Key }}'
                Value: '{{ Value }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: MetadataCatalogConfig
        value:
          GlueDataCatalog:
            RoleArn: '{{ RoleArn }}'
            DatabaseName: '{{ DatabaseName }}'
            TablePrefix: '{{ TablePrefix }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appflow.flows
WHERE data__Identifier = '<FlowName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>flows</code> resource, the following permissions are required:

### Create
```json
appflow:CreateFlow,
appflow:StartFlow,
appflow:TagResource,
appflow:ListTagsForResource,
appflow:UseConnectorProfile,
iam:PassRole,
s3:ListAllMyBuckets,
s3:GetBucketLocation,
s3:GetBucketPolicy,
kms:ListGrants,
kms:ListKeys,
kms:DescribeKey,
kms:ListAliases,
kms:CreateGrant,
secretsmanager:CreateSecret,
secretsmanager:PutResourcePolicy
```

### Read
```json
appflow:DescribeFlow,
appflow:ListTagsForResource
```

### Update
```json
appflow:UpdateFlow,
appflow:StartFlow,
appflow:StopFlow,
appflow:TagResource,
appflow:UntagResource,
appflow:ListTagsForResource,
appflow:UseConnectorProfile,
iam:PassRole,
s3:ListAllMyBuckets,
s3:GetBucketLocation,
s3:GetBucketPolicy,
kms:ListGrants,
secretsmanager:CreateSecret,
secretsmanager:PutResourcePolicy
```

### Delete
```json
appflow:DeleteFlow
```

### List
```json
appflow:ListFlows
```
