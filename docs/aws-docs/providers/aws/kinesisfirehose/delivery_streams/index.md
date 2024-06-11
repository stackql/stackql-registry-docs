---
title: delivery_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_streams
  - kinesisfirehose
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

Creates, updates, deletes or gets a <code>delivery_stream</code> resource or lists <code>delivery_streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::KinesisFirehose::DeliveryStream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesisfirehose.delivery_streams" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="delivery_stream_encryption_configuration_input" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="delivery_stream_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="delivery_stream_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="elasticsearch_destination_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="amazonopensearchservice_destination_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="amazon_open_search_serverless_destination_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="extended_s3_destination_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="kinesis_stream_source_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="msk_source_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="redshift_destination_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="s3_destination_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="splunk_destination_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="http_endpoint_destination_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="snowflake_destination_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>delivery_streams</code> in a region.
```sql
SELECT
region,
delivery_stream_name
FROM aws.kinesisfirehose.delivery_streams
WHERE region = 'us-east-1';
```
Gets all properties from a <code>delivery_stream</code>.
```sql
SELECT
region,
arn,
delivery_stream_encryption_configuration_input,
delivery_stream_name,
delivery_stream_type,
elasticsearch_destination_configuration,
amazonopensearchservice_destination_configuration,
amazon_open_search_serverless_destination_configuration,
extended_s3_destination_configuration,
kinesis_stream_source_configuration,
msk_source_configuration,
redshift_destination_configuration,
s3_destination_configuration,
splunk_destination_configuration,
http_endpoint_destination_configuration,
snowflake_destination_configuration,
tags
FROM aws.kinesisfirehose.delivery_streams
WHERE region = 'us-east-1' AND data__Identifier = '<DeliveryStreamName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>delivery_stream</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.kinesisfirehose.delivery_streams (
 DeliveryStreamEncryptionConfigurationInput,
 DeliveryStreamName,
 DeliveryStreamType,
 ElasticsearchDestinationConfiguration,
 AmazonopensearchserviceDestinationConfiguration,
 AmazonOpenSearchServerlessDestinationConfiguration,
 ExtendedS3DestinationConfiguration,
 KinesisStreamSourceConfiguration,
 MSKSourceConfiguration,
 RedshiftDestinationConfiguration,
 S3DestinationConfiguration,
 SplunkDestinationConfiguration,
 HttpEndpointDestinationConfiguration,
 SnowflakeDestinationConfiguration,
 Tags,
 region
)
SELECT 
'{{ DeliveryStreamEncryptionConfigurationInput }}',
 '{{ DeliveryStreamName }}',
 '{{ DeliveryStreamType }}',
 '{{ ElasticsearchDestinationConfiguration }}',
 '{{ AmazonopensearchserviceDestinationConfiguration }}',
 '{{ AmazonOpenSearchServerlessDestinationConfiguration }}',
 '{{ ExtendedS3DestinationConfiguration }}',
 '{{ KinesisStreamSourceConfiguration }}',
 '{{ MSKSourceConfiguration }}',
 '{{ RedshiftDestinationConfiguration }}',
 '{{ S3DestinationConfiguration }}',
 '{{ SplunkDestinationConfiguration }}',
 '{{ HttpEndpointDestinationConfiguration }}',
 '{{ SnowflakeDestinationConfiguration }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.kinesisfirehose.delivery_streams (
 DeliveryStreamEncryptionConfigurationInput,
 DeliveryStreamName,
 DeliveryStreamType,
 ElasticsearchDestinationConfiguration,
 AmazonopensearchserviceDestinationConfiguration,
 AmazonOpenSearchServerlessDestinationConfiguration,
 ExtendedS3DestinationConfiguration,
 KinesisStreamSourceConfiguration,
 MSKSourceConfiguration,
 RedshiftDestinationConfiguration,
 S3DestinationConfiguration,
 SplunkDestinationConfiguration,
 HttpEndpointDestinationConfiguration,
 SnowflakeDestinationConfiguration,
 Tags,
 region
)
SELECT 
 '{{ DeliveryStreamEncryptionConfigurationInput }}',
 '{{ DeliveryStreamName }}',
 '{{ DeliveryStreamType }}',
 '{{ ElasticsearchDestinationConfiguration }}',
 '{{ AmazonopensearchserviceDestinationConfiguration }}',
 '{{ AmazonOpenSearchServerlessDestinationConfiguration }}',
 '{{ ExtendedS3DestinationConfiguration }}',
 '{{ KinesisStreamSourceConfiguration }}',
 '{{ MSKSourceConfiguration }}',
 '{{ RedshiftDestinationConfiguration }}',
 '{{ S3DestinationConfiguration }}',
 '{{ SplunkDestinationConfiguration }}',
 '{{ HttpEndpointDestinationConfiguration }}',
 '{{ SnowflakeDestinationConfiguration }}',
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
  - name: delivery_stream
    props:
      - name: DeliveryStreamEncryptionConfigurationInput
        value:
          KeyARN: '{{ KeyARN }}'
          KeyType: '{{ KeyType }}'
      - name: DeliveryStreamName
        value: '{{ DeliveryStreamName }}'
      - name: DeliveryStreamType
        value: '{{ DeliveryStreamType }}'
      - name: ElasticsearchDestinationConfiguration
        value:
          BufferingHints:
            IntervalInSeconds: '{{ IntervalInSeconds }}'
            SizeInMBs: '{{ SizeInMBs }}'
          CloudWatchLoggingOptions:
            Enabled: '{{ Enabled }}'
            LogGroupName: '{{ LogGroupName }}'
            LogStreamName: '{{ LogStreamName }}'
          DomainARN: '{{ DomainARN }}'
          IndexName: '{{ IndexName }}'
          IndexRotationPeriod: '{{ IndexRotationPeriod }}'
          ProcessingConfiguration:
            Enabled: '{{ Enabled }}'
            Processors:
              - Parameters:
                  - ParameterName: '{{ ParameterName }}'
                    ParameterValue: '{{ ParameterValue }}'
                Type: '{{ Type }}'
          RetryOptions:
            DurationInSeconds: '{{ DurationInSeconds }}'
          RoleARN: '{{ RoleARN }}'
          S3BackupMode: '{{ S3BackupMode }}'
          S3Configuration:
            BucketARN: '{{ BucketARN }}'
            BufferingHints:
              IntervalInSeconds: '{{ IntervalInSeconds }}'
              SizeInMBs: '{{ SizeInMBs }}'
            CloudWatchLoggingOptions: null
            CompressionFormat: '{{ CompressionFormat }}'
            EncryptionConfiguration:
              KMSEncryptionConfig:
                AWSKMSKeyARN: '{{ AWSKMSKeyARN }}'
              NoEncryptionConfig: '{{ NoEncryptionConfig }}'
            ErrorOutputPrefix: '{{ ErrorOutputPrefix }}'
            Prefix: '{{ Prefix }}'
            RoleARN: '{{ RoleARN }}'
          ClusterEndpoint: '{{ ClusterEndpoint }}'
          TypeName: '{{ TypeName }}'
          VpcConfiguration:
            RoleARN: '{{ RoleARN }}'
            SubnetIds:
              - '{{ SubnetIds[0] }}'
            SecurityGroupIds:
              - '{{ SecurityGroupIds[0] }}'
          DocumentIdOptions:
            DefaultDocumentIdFormat: '{{ DefaultDocumentIdFormat }}'
      - name: AmazonopensearchserviceDestinationConfiguration
        value:
          BufferingHints:
            IntervalInSeconds: '{{ IntervalInSeconds }}'
            SizeInMBs: '{{ SizeInMBs }}'
          CloudWatchLoggingOptions: null
          DomainARN: '{{ DomainARN }}'
          IndexName: '{{ IndexName }}'
          IndexRotationPeriod: '{{ IndexRotationPeriod }}'
          ProcessingConfiguration: null
          RetryOptions:
            DurationInSeconds: '{{ DurationInSeconds }}'
          RoleARN: '{{ RoleARN }}'
          S3BackupMode: '{{ S3BackupMode }}'
          S3Configuration: null
          ClusterEndpoint: '{{ ClusterEndpoint }}'
          TypeName: '{{ TypeName }}'
          VpcConfiguration: null
          DocumentIdOptions: null
      - name: AmazonOpenSearchServerlessDestinationConfiguration
        value:
          BufferingHints:
            IntervalInSeconds: '{{ IntervalInSeconds }}'
            SizeInMBs: '{{ SizeInMBs }}'
          CloudWatchLoggingOptions: null
          IndexName: '{{ IndexName }}'
          ProcessingConfiguration: null
          RetryOptions:
            DurationInSeconds: '{{ DurationInSeconds }}'
          RoleARN: '{{ RoleARN }}'
          S3BackupMode: '{{ S3BackupMode }}'
          S3Configuration: null
          CollectionEndpoint: '{{ CollectionEndpoint }}'
          VpcConfiguration: null
      - name: ExtendedS3DestinationConfiguration
        value:
          BucketARN: '{{ BucketARN }}'
          BufferingHints: null
          CloudWatchLoggingOptions: null
          CompressionFormat: '{{ CompressionFormat }}'
          CustomTimeZone: '{{ CustomTimeZone }}'
          DataFormatConversionConfiguration:
            Enabled: '{{ Enabled }}'
            InputFormatConfiguration:
              Deserializer:
                HiveJsonSerDe:
                  TimestampFormats:
                    - '{{ TimestampFormats[0] }}'
                OpenXJsonSerDe:
                  CaseInsensitive: '{{ CaseInsensitive }}'
                  ColumnToJsonKeyMappings: {}
                  ConvertDotsInJsonKeysToUnderscores: '{{ ConvertDotsInJsonKeysToUnderscores }}'
            OutputFormatConfiguration:
              Serializer:
                OrcSerDe:
                  BlockSizeBytes: '{{ BlockSizeBytes }}'
                  BloomFilterColumns:
                    - '{{ BloomFilterColumns[0] }}'
                  BloomFilterFalsePositiveProbability: null
                  Compression: '{{ Compression }}'
                  DictionaryKeyThreshold: null
                  EnablePadding: '{{ EnablePadding }}'
                  FormatVersion: '{{ FormatVersion }}'
                  PaddingTolerance: null
                  RowIndexStride: '{{ RowIndexStride }}'
                  StripeSizeBytes: '{{ StripeSizeBytes }}'
                ParquetSerDe:
                  BlockSizeBytes: '{{ BlockSizeBytes }}'
                  Compression: '{{ Compression }}'
                  EnableDictionaryCompression: '{{ EnableDictionaryCompression }}'
                  MaxPaddingBytes: '{{ MaxPaddingBytes }}'
                  PageSizeBytes: '{{ PageSizeBytes }}'
                  WriterVersion: '{{ WriterVersion }}'
            SchemaConfiguration:
              CatalogId: '{{ CatalogId }}'
              DatabaseName: '{{ DatabaseName }}'
              Region: '{{ Region }}'
              RoleARN: '{{ RoleARN }}'
              TableName: '{{ TableName }}'
              VersionId: '{{ VersionId }}'
          DynamicPartitioningConfiguration:
            Enabled: '{{ Enabled }}'
            RetryOptions:
              DurationInSeconds: '{{ DurationInSeconds }}'
          EncryptionConfiguration: null
          ErrorOutputPrefix: '{{ ErrorOutputPrefix }}'
          FileExtension: '{{ FileExtension }}'
          Prefix: '{{ Prefix }}'
          ProcessingConfiguration: null
          RoleARN: '{{ RoleARN }}'
          S3BackupConfiguration: null
          S3BackupMode: '{{ S3BackupMode }}'
      - name: KinesisStreamSourceConfiguration
        value:
          KinesisStreamARN: '{{ KinesisStreamARN }}'
          RoleARN: '{{ RoleARN }}'
      - name: MSKSourceConfiguration
        value:
          MSKClusterARN: '{{ MSKClusterARN }}'
          TopicName: '{{ TopicName }}'
          AuthenticationConfiguration:
            RoleARN: '{{ RoleARN }}'
            Connectivity: '{{ Connectivity }}'
      - name: RedshiftDestinationConfiguration
        value:
          CloudWatchLoggingOptions: null
          ClusterJDBCURL: '{{ ClusterJDBCURL }}'
          CopyCommand:
            CopyOptions: '{{ CopyOptions }}'
            DataTableColumns: '{{ DataTableColumns }}'
            DataTableName: '{{ DataTableName }}'
          Password: '{{ Password }}'
          ProcessingConfiguration: null
          RetryOptions:
            DurationInSeconds: '{{ DurationInSeconds }}'
          RoleARN: '{{ RoleARN }}'
          S3BackupConfiguration: null
          S3BackupMode: '{{ S3BackupMode }}'
          S3Configuration: null
          Username: '{{ Username }}'
      - name: S3DestinationConfiguration
        value: null
      - name: SplunkDestinationConfiguration
        value:
          CloudWatchLoggingOptions: null
          HECAcknowledgmentTimeoutInSeconds: '{{ HECAcknowledgmentTimeoutInSeconds }}'
          HECEndpoint: '{{ HECEndpoint }}'
          HECEndpointType: '{{ HECEndpointType }}'
          HECToken: '{{ HECToken }}'
          ProcessingConfiguration: null
          RetryOptions:
            DurationInSeconds: '{{ DurationInSeconds }}'
          S3BackupMode: '{{ S3BackupMode }}'
          S3Configuration: null
          BufferingHints:
            IntervalInSeconds: '{{ IntervalInSeconds }}'
            SizeInMBs: '{{ SizeInMBs }}'
      - name: HttpEndpointDestinationConfiguration
        value:
          RoleARN: '{{ RoleARN }}'
          EndpointConfiguration:
            Url: '{{ Url }}'
            AccessKey: '{{ AccessKey }}'
            Name: '{{ Name }}'
          RequestConfiguration:
            ContentEncoding: '{{ ContentEncoding }}'
            CommonAttributes:
              - AttributeName: '{{ AttributeName }}'
                AttributeValue: '{{ AttributeValue }}'
          BufferingHints: null
          CloudWatchLoggingOptions: null
          ProcessingConfiguration: null
          RetryOptions: null
          S3BackupMode: '{{ S3BackupMode }}'
          S3Configuration: null
      - name: SnowflakeDestinationConfiguration
        value:
          AccountUrl: '{{ AccountUrl }}'
          PrivateKey: '{{ PrivateKey }}'
          KeyPassphrase: '{{ KeyPassphrase }}'
          User: '{{ User }}'
          Database: '{{ Database }}'
          Schema: '{{ Schema }}'
          Table: '{{ Table }}'
          SnowflakeRoleConfiguration:
            Enabled: '{{ Enabled }}'
            SnowflakeRole: '{{ SnowflakeRole }}'
          DataLoadingOption: '{{ DataLoadingOption }}'
          MetaDataColumnName: '{{ MetaDataColumnName }}'
          ContentColumnName: '{{ ContentColumnName }}'
          SnowflakeVpcConfiguration:
            PrivateLinkVpceId: '{{ PrivateLinkVpceId }}'
          CloudWatchLoggingOptions: null
          ProcessingConfiguration: null
          RoleARN: '{{ RoleARN }}'
          RetryOptions:
            DurationInSeconds: '{{ DurationInSeconds }}'
          S3BackupMode: '{{ S3BackupMode }}'
          S3Configuration: null
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
DELETE FROM aws.kinesisfirehose.delivery_streams
WHERE data__Identifier = '<DeliveryStreamName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>delivery_streams</code> resource, the following permissions are required:

### Create
```json
firehose:CreateDeliveryStream,
firehose:DescribeDeliveryStream,
iam:GetRole,
iam:PassRole,
kms:CreateGrant,
kms:DescribeKey
```

### Read
```json
firehose:DescribeDeliveryStream,
firehose:ListTagsForDeliveryStream
```

### Update
```json
firehose:UpdateDestination,
firehose:DescribeDeliveryStream,
firehose:StartDeliveryStreamEncryption,
firehose:StopDeliveryStreamEncryption,
firehose:ListTagsForDeliveryStream,
firehose:TagDeliveryStream,
firehose:UntagDeliveryStream,
kms:CreateGrant,
kms:RevokeGrant,
kms:DescribeKey
```

### Delete
```json
firehose:DeleteDeliveryStream,
firehose:DescribeDeliveryStream,
kms:RevokeGrant,
kms:DescribeKey
```

### List
```json
firehose:ListDeliveryStreams
```

