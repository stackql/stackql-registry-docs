---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
  - dynamodb
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


Used to retrieve a list of <code>tables</code> in a region or to create or delete a <code>tables</code> resource, use <code>table</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::DynamoDB::Table`` resource creates a DDB table. For more information, see &#91;CreateTable&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;amazondynamodb&#x2F;latest&#x2F;APIReference&#x2F;API_CreateTable.html) in the *API Reference*.&lt;br&#x2F;&gt; You should be aware of the following behaviors when working with DDB tables:&lt;br&#x2F;&gt;  +   CFNlong typically creates DDB tables in parallel. However, if your template includes multiple DDB tables with indexes, you must declare dependencies so that the tables are created sequentially. DDBlong limits the number of tables with secondary indexes that are in the creating state. If you create multiple tables with indexes at the same time, DDB returns an error and the stack operation fails. For an example, see &#91;DynamoDB Table with a DependsOn Attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-dynamodb-table.html#aws-resource-dynamodb-table--examples--DynamoDB_Table_with_a_DependsOn_Attribute).&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt;   Our guidance is to use the latest schema documented here for your CFNlong templates. This schema supports the provisioning of all table settings below. When using this schema in your CFNlong templates, please ensure that your Identity and Access Management (IAM) policies are updated with appropriate permissions to allow for the authorization of these setting changes.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dynamodb.tables" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td>A name for the table. If you don't specify a name, CFNlong generates a unique physical ID and uses that ID for the table name. For more information, see &#91;Name Type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html).&lt;br&#x2F;&gt;  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
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
table_name
FROM aws.dynamodb.tables
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>table</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- table.iql (required properties only)
INSERT INTO aws.dynamodb.tables (
 KeySchema,
 region
)
SELECT 
'{{ KeySchema }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- table.iql (all properties)
INSERT INTO aws.dynamodb.tables (
 SSESpecification,
 KinesisStreamSpecification,
 StreamSpecification,
 ContributorInsightsSpecification,
 ImportSourceSpecification,
 PointInTimeRecoverySpecification,
 ProvisionedThroughput,
 TableName,
 AttributeDefinitions,
 BillingMode,
 GlobalSecondaryIndexes,
 ResourcePolicy,
 KeySchema,
 LocalSecondaryIndexes,
 DeletionProtectionEnabled,
 TableClass,
 Tags,
 TimeToLiveSpecification,
 region
)
SELECT 
 '{{ SSESpecification }}',
 '{{ KinesisStreamSpecification }}',
 '{{ StreamSpecification }}',
 '{{ ContributorInsightsSpecification }}',
 '{{ ImportSourceSpecification }}',
 '{{ PointInTimeRecoverySpecification }}',
 '{{ ProvisionedThroughput }}',
 '{{ TableName }}',
 '{{ AttributeDefinitions }}',
 '{{ BillingMode }}',
 '{{ GlobalSecondaryIndexes }}',
 '{{ ResourcePolicy }}',
 '{{ KeySchema }}',
 '{{ LocalSecondaryIndexes }}',
 '{{ DeletionProtectionEnabled }}',
 '{{ TableClass }}',
 '{{ Tags }}',
 '{{ TimeToLiveSpecification }}',
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
  - name: table
    props:
      - name: SSESpecification
        value:
          SSEEnabled: '{{ SSEEnabled }}'
          SSEType: '{{ SSEType }}'
          KMSMasterKeyId: '{{ KMSMasterKeyId }}'
      - name: KinesisStreamSpecification
        value:
          ApproximateCreationDateTimePrecision: '{{ ApproximateCreationDateTimePrecision }}'
          StreamArn: '{{ StreamArn }}'
      - name: StreamSpecification
        value:
          StreamViewType: '{{ StreamViewType }}'
          ResourcePolicy:
            PolicyDocument: {}
      - name: ContributorInsightsSpecification
        value:
          Enabled: '{{ Enabled }}'
      - name: ImportSourceSpecification
        value:
          S3BucketSource:
            S3Bucket: '{{ S3Bucket }}'
            S3KeyPrefix: '{{ S3KeyPrefix }}'
            S3BucketOwner: '{{ S3BucketOwner }}'
          InputFormat: '{{ InputFormat }}'
          InputFormatOptions:
            Csv:
              Delimiter: '{{ Delimiter }}'
              HeaderList:
                - '{{ HeaderList[0] }}'
          InputCompressionType: '{{ InputCompressionType }}'
      - name: PointInTimeRecoverySpecification
        value:
          PointInTimeRecoveryEnabled: '{{ PointInTimeRecoveryEnabled }}'
      - name: ProvisionedThroughput
        value:
          WriteCapacityUnits: '{{ WriteCapacityUnits }}'
          ReadCapacityUnits: '{{ ReadCapacityUnits }}'
      - name: TableName
        value: '{{ TableName }}'
      - name: AttributeDefinitions
        value:
          - AttributeType: '{{ AttributeType }}'
            AttributeName: '{{ AttributeName }}'
      - name: BillingMode
        value: '{{ BillingMode }}'
      - name: GlobalSecondaryIndexes
        value:
          - IndexName: '{{ IndexName }}'
            ContributorInsightsSpecification: null
            Projection:
              NonKeyAttributes:
                - '{{ NonKeyAttributes[0] }}'
              ProjectionType: '{{ ProjectionType }}'
            ProvisionedThroughput: null
            KeySchema:
              - KeyType: '{{ KeyType }}'
                AttributeName: '{{ AttributeName }}'
      - name: ResourcePolicy
        value: null
      - name: KeySchema
        value: null
      - name: LocalSecondaryIndexes
        value:
          - IndexName: '{{ IndexName }}'
            Projection: null
            KeySchema:
              - null
      - name: DeletionProtectionEnabled
        value: '{{ DeletionProtectionEnabled }}'
      - name: TableClass
        value: '{{ TableClass }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: TimeToLiveSpecification
        value:
          Enabled: '{{ Enabled }}'
          AttributeName: '{{ AttributeName }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.dynamodb.tables
WHERE data__Identifier = '<TableName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>tables</code> resource, the following permissions are required:

### Create
```json
dynamodb:CreateTable,
dynamodb:DescribeImport,
dynamodb:DescribeTable,
dynamodb:DescribeTimeToLive,
dynamodb:UpdateTimeToLive,
dynamodb:UpdateContributorInsights,
dynamodb:UpdateContinuousBackups,
dynamodb:DescribeContinuousBackups,
dynamodb:DescribeContributorInsights,
dynamodb:EnableKinesisStreamingDestination,
dynamodb:DisableKinesisStreamingDestination,
dynamodb:DescribeKinesisStreamingDestination,
dynamodb:ImportTable,
dynamodb:ListTagsOfResource,
dynamodb:TagResource,
dynamodb:UpdateTable,
dynamodb:GetResourcePolicy,
dynamodb:PutResourcePolicy,
kinesis:DescribeStream,
kinesis:PutRecords,
iam:CreateServiceLinkedRole,
kms:CreateGrant,
kms:Decrypt,
kms:DescribeKey,
kms:ListAliases,
kms:Encrypt,
kms:RevokeGrant,
logs:CreateLogGroup,
logs:CreateLogStream,
logs:DescribeLogGroups,
logs:DescribeLogStreams,
logs:PutLogEvents,
logs:PutRetentionPolicy,
s3:GetObject,
s3:GetObjectMetadata,
s3:ListBucket
```

### List
```json
dynamodb:ListTables
```

### Delete
```json
dynamodb:DeleteTable,
dynamodb:DescribeTable
```

