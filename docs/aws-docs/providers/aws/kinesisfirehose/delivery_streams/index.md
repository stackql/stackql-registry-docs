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


Used to retrieve a list of <code>delivery_streams</code> in a region or to create or delete a <code>delivery_streams</code> resource, use <code>delivery_stream</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::KinesisFirehose::DeliveryStream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesisfirehose.delivery_streams" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="delivery_stream_name" /></td><td><code>string</code></td><td></td></tr>
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
delivery_stream_name
FROM aws.kinesisfirehose.delivery_streams
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
 "DeliveryStreamEncryptionConfigurationInput": {
  "KeyARN": "{{ KeyARN }}",
  "KeyType": "{{ KeyType }}"
 },
 "DeliveryStreamName": "{{ DeliveryStreamName }}",
 "DeliveryStreamType": "{{ DeliveryStreamType }}",
 "ElasticsearchDestinationConfiguration": {
  "BufferingHints": {
   "IntervalInSeconds": "{{ IntervalInSeconds }}",
   "SizeInMBs": "{{ SizeInMBs }}"
  },
  "CloudWatchLoggingOptions": {
   "Enabled": "{{ Enabled }}",
   "LogGroupName": "{{ LogGroupName }}",
   "LogStreamName": "{{ LogStreamName }}"
  },
  "DomainARN": "{{ DomainARN }}",
  "IndexName": "{{ IndexName }}",
  "IndexRotationPeriod": "{{ IndexRotationPeriod }}",
  "ProcessingConfiguration": {
   "Enabled": "{{ Enabled }}",
   "Processors": [
    {
     "Parameters": [
      {
       "ParameterName": "{{ ParameterName }}",
       "ParameterValue": "{{ ParameterValue }}"
      }
     ],
     "Type": "{{ Type }}"
    }
   ]
  },
  "RetryOptions": {
   "DurationInSeconds": "{{ DurationInSeconds }}"
  },
  "RoleARN": "{{ RoleARN }}",
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": {
   "BucketARN": "{{ BucketARN }}",
   "BufferingHints": {
    "IntervalInSeconds": "{{ IntervalInSeconds }}",
    "SizeInMBs": "{{ SizeInMBs }}"
   },
   "CloudWatchLoggingOptions": null,
   "CompressionFormat": "{{ CompressionFormat }}",
   "EncryptionConfiguration": {
    "KMSEncryptionConfig": {
     "AWSKMSKeyARN": "{{ AWSKMSKeyARN }}"
    },
    "NoEncryptionConfig": "{{ NoEncryptionConfig }}"
   },
   "ErrorOutputPrefix": "{{ ErrorOutputPrefix }}",
   "Prefix": "{{ Prefix }}",
   "RoleARN": "{{ RoleARN }}"
  },
  "ClusterEndpoint": "{{ ClusterEndpoint }}",
  "TypeName": "{{ TypeName }}",
  "VpcConfiguration": {
   "RoleARN": "{{ RoleARN }}",
   "SubnetIds": [
    "{{ SubnetIds[0] }}"
   ],
   "SecurityGroupIds": [
    "{{ SecurityGroupIds[0] }}"
   ]
  },
  "DocumentIdOptions": {
   "DefaultDocumentIdFormat": "{{ DefaultDocumentIdFormat }}"
  }
 },
 "AmazonopensearchserviceDestinationConfiguration": {
  "BufferingHints": {
   "IntervalInSeconds": "{{ IntervalInSeconds }}",
   "SizeInMBs": "{{ SizeInMBs }}"
  },
  "CloudWatchLoggingOptions": null,
  "DomainARN": "{{ DomainARN }}",
  "IndexName": "{{ IndexName }}",
  "IndexRotationPeriod": "{{ IndexRotationPeriod }}",
  "ProcessingConfiguration": null,
  "RetryOptions": {
   "DurationInSeconds": "{{ DurationInSeconds }}"
  },
  "RoleARN": "{{ RoleARN }}",
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": null,
  "ClusterEndpoint": "{{ ClusterEndpoint }}",
  "TypeName": "{{ TypeName }}",
  "VpcConfiguration": null,
  "DocumentIdOptions": null
 },
 "AmazonOpenSearchServerlessDestinationConfiguration": {
  "BufferingHints": {
   "IntervalInSeconds": "{{ IntervalInSeconds }}",
   "SizeInMBs": "{{ SizeInMBs }}"
  },
  "CloudWatchLoggingOptions": null,
  "IndexName": "{{ IndexName }}",
  "ProcessingConfiguration": null,
  "RetryOptions": {
   "DurationInSeconds": "{{ DurationInSeconds }}"
  },
  "RoleARN": "{{ RoleARN }}",
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": null,
  "CollectionEndpoint": "{{ CollectionEndpoint }}",
  "VpcConfiguration": null
 },
 "ExtendedS3DestinationConfiguration": {
  "BucketARN": "{{ BucketARN }}",
  "BufferingHints": null,
  "CloudWatchLoggingOptions": null,
  "CompressionFormat": "{{ CompressionFormat }}",
  "CustomTimeZone": "{{ CustomTimeZone }}",
  "DataFormatConversionConfiguration": {
   "Enabled": "{{ Enabled }}",
   "InputFormatConfiguration": {
    "Deserializer": {
     "HiveJsonSerDe": {
      "TimestampFormats": [
       "{{ TimestampFormats[0] }}"
      ]
     },
     "OpenXJsonSerDe": {
      "CaseInsensitive": "{{ CaseInsensitive }}",
      "ColumnToJsonKeyMappings": {},
      "ConvertDotsInJsonKeysToUnderscores": "{{ ConvertDotsInJsonKeysToUnderscores }}"
     }
    }
   },
   "OutputFormatConfiguration": {
    "Serializer": {
     "OrcSerDe": {
      "BlockSizeBytes": "{{ BlockSizeBytes }}",
      "BloomFilterColumns": [
       "{{ BloomFilterColumns[0] }}"
      ],
      "BloomFilterFalsePositiveProbability": null,
      "Compression": "{{ Compression }}",
      "DictionaryKeyThreshold": null,
      "EnablePadding": "{{ EnablePadding }}",
      "FormatVersion": "{{ FormatVersion }}",
      "PaddingTolerance": null,
      "RowIndexStride": "{{ RowIndexStride }}",
      "StripeSizeBytes": "{{ StripeSizeBytes }}"
     },
     "ParquetSerDe": {
      "BlockSizeBytes": "{{ BlockSizeBytes }}",
      "Compression": "{{ Compression }}",
      "EnableDictionaryCompression": "{{ EnableDictionaryCompression }}",
      "MaxPaddingBytes": "{{ MaxPaddingBytes }}",
      "PageSizeBytes": "{{ PageSizeBytes }}",
      "WriterVersion": "{{ WriterVersion }}"
     }
    }
   },
   "SchemaConfiguration": {
    "CatalogId": "{{ CatalogId }}",
    "DatabaseName": "{{ DatabaseName }}",
    "Region": "{{ Region }}",
    "RoleARN": "{{ RoleARN }}",
    "TableName": "{{ TableName }}",
    "VersionId": "{{ VersionId }}"
   }
  },
  "DynamicPartitioningConfiguration": {
   "Enabled": "{{ Enabled }}",
   "RetryOptions": {
    "DurationInSeconds": "{{ DurationInSeconds }}"
   }
  },
  "EncryptionConfiguration": null,
  "ErrorOutputPrefix": "{{ ErrorOutputPrefix }}",
  "FileExtension": "{{ FileExtension }}",
  "Prefix": "{{ Prefix }}",
  "ProcessingConfiguration": null,
  "RoleARN": "{{ RoleARN }}",
  "S3BackupConfiguration": null,
  "S3BackupMode": "{{ S3BackupMode }}"
 },
 "KinesisStreamSourceConfiguration": {
  "KinesisStreamARN": "{{ KinesisStreamARN }}",
  "RoleARN": "{{ RoleARN }}"
 },
 "MSKSourceConfiguration": {
  "MSKClusterARN": "{{ MSKClusterARN }}",
  "TopicName": "{{ TopicName }}",
  "AuthenticationConfiguration": {
   "RoleARN": "{{ RoleARN }}",
   "Connectivity": "{{ Connectivity }}"
  }
 },
 "RedshiftDestinationConfiguration": {
  "CloudWatchLoggingOptions": null,
  "ClusterJDBCURL": "{{ ClusterJDBCURL }}",
  "CopyCommand": {
   "CopyOptions": "{{ CopyOptions }}",
   "DataTableColumns": "{{ DataTableColumns }}",
   "DataTableName": "{{ DataTableName }}"
  },
  "Password": "{{ Password }}",
  "ProcessingConfiguration": null,
  "RetryOptions": {
   "DurationInSeconds": "{{ DurationInSeconds }}"
  },
  "RoleARN": "{{ RoleARN }}",
  "S3BackupConfiguration": null,
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": null,
  "Username": "{{ Username }}"
 },
 "S3DestinationConfiguration": null,
 "SplunkDestinationConfiguration": {
  "CloudWatchLoggingOptions": null,
  "HECAcknowledgmentTimeoutInSeconds": "{{ HECAcknowledgmentTimeoutInSeconds }}",
  "HECEndpoint": "{{ HECEndpoint }}",
  "HECEndpointType": "{{ HECEndpointType }}",
  "HECToken": "{{ HECToken }}",
  "ProcessingConfiguration": null,
  "RetryOptions": {
   "DurationInSeconds": "{{ DurationInSeconds }}"
  },
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": null,
  "BufferingHints": {
   "IntervalInSeconds": "{{ IntervalInSeconds }}",
   "SizeInMBs": "{{ SizeInMBs }}"
  }
 },
 "HttpEndpointDestinationConfiguration": {
  "RoleARN": "{{ RoleARN }}",
  "EndpointConfiguration": {
   "Url": "{{ Url }}",
   "AccessKey": "{{ AccessKey }}",
   "Name": "{{ Name }}"
  },
  "RequestConfiguration": {
   "ContentEncoding": "{{ ContentEncoding }}",
   "CommonAttributes": [
    {
     "AttributeName": "{{ AttributeName }}",
     "AttributeValue": "{{ AttributeValue }}"
    }
   ]
  },
  "BufferingHints": null,
  "CloudWatchLoggingOptions": null,
  "ProcessingConfiguration": null,
  "RetryOptions": null,
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": null
 },
 "SnowflakeDestinationConfiguration": {
  "AccountUrl": "{{ AccountUrl }}",
  "PrivateKey": "{{ PrivateKey }}",
  "KeyPassphrase": "{{ KeyPassphrase }}",
  "User": "{{ User }}",
  "Database": "{{ Database }}",
  "Schema": "{{ Schema }}",
  "Table": "{{ Table }}",
  "SnowflakeRoleConfiguration": {
   "Enabled": "{{ Enabled }}",
   "SnowflakeRole": "{{ SnowflakeRole }}"
  },
  "DataLoadingOption": "{{ DataLoadingOption }}",
  "MetaDataColumnName": "{{ MetaDataColumnName }}",
  "ContentColumnName": "{{ ContentColumnName }}",
  "SnowflakeVpcConfiguration": {
   "PrivateLinkVpceId": "{{ PrivateLinkVpceId }}"
  },
  "CloudWatchLoggingOptions": null,
  "ProcessingConfiguration": null,
  "RoleARN": "{{ RoleARN }}",
  "RetryOptions": {
   "DurationInSeconds": "{{ DurationInSeconds }}"
  },
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": null
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
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
{{ DeliveryStreamEncryptionConfigurationInput }},
 {{ DeliveryStreamName }},
 {{ DeliveryStreamType }},
 {{ ElasticsearchDestinationConfiguration }},
 {{ AmazonopensearchserviceDestinationConfiguration }},
 {{ AmazonOpenSearchServerlessDestinationConfiguration }},
 {{ ExtendedS3DestinationConfiguration }},
 {{ KinesisStreamSourceConfiguration }},
 {{ MSKSourceConfiguration }},
 {{ RedshiftDestinationConfiguration }},
 {{ S3DestinationConfiguration }},
 {{ SplunkDestinationConfiguration }},
 {{ HttpEndpointDestinationConfiguration }},
 {{ SnowflakeDestinationConfiguration }},
 {{ Tags }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DeliveryStreamEncryptionConfigurationInput": {
  "KeyARN": "{{ KeyARN }}",
  "KeyType": "{{ KeyType }}"
 },
 "DeliveryStreamName": "{{ DeliveryStreamName }}",
 "DeliveryStreamType": "{{ DeliveryStreamType }}",
 "ElasticsearchDestinationConfiguration": {
  "BufferingHints": {
   "IntervalInSeconds": "{{ IntervalInSeconds }}",
   "SizeInMBs": "{{ SizeInMBs }}"
  },
  "CloudWatchLoggingOptions": {
   "Enabled": "{{ Enabled }}",
   "LogGroupName": "{{ LogGroupName }}",
   "LogStreamName": "{{ LogStreamName }}"
  },
  "DomainARN": "{{ DomainARN }}",
  "IndexName": "{{ IndexName }}",
  "IndexRotationPeriod": "{{ IndexRotationPeriod }}",
  "ProcessingConfiguration": {
   "Enabled": "{{ Enabled }}",
   "Processors": [
    {
     "Parameters": [
      {
       "ParameterName": "{{ ParameterName }}",
       "ParameterValue": "{{ ParameterValue }}"
      }
     ],
     "Type": "{{ Type }}"
    }
   ]
  },
  "RetryOptions": {
   "DurationInSeconds": "{{ DurationInSeconds }}"
  },
  "RoleARN": "{{ RoleARN }}",
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": {
   "BucketARN": "{{ BucketARN }}",
   "BufferingHints": {
    "IntervalInSeconds": "{{ IntervalInSeconds }}",
    "SizeInMBs": "{{ SizeInMBs }}"
   },
   "CloudWatchLoggingOptions": null,
   "CompressionFormat": "{{ CompressionFormat }}",
   "EncryptionConfiguration": {
    "KMSEncryptionConfig": {
     "AWSKMSKeyARN": "{{ AWSKMSKeyARN }}"
    },
    "NoEncryptionConfig": "{{ NoEncryptionConfig }}"
   },
   "ErrorOutputPrefix": "{{ ErrorOutputPrefix }}",
   "Prefix": "{{ Prefix }}",
   "RoleARN": "{{ RoleARN }}"
  },
  "ClusterEndpoint": "{{ ClusterEndpoint }}",
  "TypeName": "{{ TypeName }}",
  "VpcConfiguration": {
   "RoleARN": "{{ RoleARN }}",
   "SubnetIds": [
    "{{ SubnetIds[0] }}"
   ],
   "SecurityGroupIds": [
    "{{ SecurityGroupIds[0] }}"
   ]
  },
  "DocumentIdOptions": {
   "DefaultDocumentIdFormat": "{{ DefaultDocumentIdFormat }}"
  }
 },
 "AmazonopensearchserviceDestinationConfiguration": {
  "BufferingHints": {
   "IntervalInSeconds": "{{ IntervalInSeconds }}",
   "SizeInMBs": "{{ SizeInMBs }}"
  },
  "CloudWatchLoggingOptions": null,
  "DomainARN": "{{ DomainARN }}",
  "IndexName": "{{ IndexName }}",
  "IndexRotationPeriod": "{{ IndexRotationPeriod }}",
  "ProcessingConfiguration": null,
  "RetryOptions": {
   "DurationInSeconds": "{{ DurationInSeconds }}"
  },
  "RoleARN": "{{ RoleARN }}",
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": null,
  "ClusterEndpoint": "{{ ClusterEndpoint }}",
  "TypeName": "{{ TypeName }}",
  "VpcConfiguration": null,
  "DocumentIdOptions": null
 },
 "AmazonOpenSearchServerlessDestinationConfiguration": {
  "BufferingHints": {
   "IntervalInSeconds": "{{ IntervalInSeconds }}",
   "SizeInMBs": "{{ SizeInMBs }}"
  },
  "CloudWatchLoggingOptions": null,
  "IndexName": "{{ IndexName }}",
  "ProcessingConfiguration": null,
  "RetryOptions": {
   "DurationInSeconds": "{{ DurationInSeconds }}"
  },
  "RoleARN": "{{ RoleARN }}",
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": null,
  "CollectionEndpoint": "{{ CollectionEndpoint }}",
  "VpcConfiguration": null
 },
 "ExtendedS3DestinationConfiguration": {
  "BucketARN": "{{ BucketARN }}",
  "BufferingHints": null,
  "CloudWatchLoggingOptions": null,
  "CompressionFormat": "{{ CompressionFormat }}",
  "CustomTimeZone": "{{ CustomTimeZone }}",
  "DataFormatConversionConfiguration": {
   "Enabled": "{{ Enabled }}",
   "InputFormatConfiguration": {
    "Deserializer": {
     "HiveJsonSerDe": {
      "TimestampFormats": [
       "{{ TimestampFormats[0] }}"
      ]
     },
     "OpenXJsonSerDe": {
      "CaseInsensitive": "{{ CaseInsensitive }}",
      "ColumnToJsonKeyMappings": {},
      "ConvertDotsInJsonKeysToUnderscores": "{{ ConvertDotsInJsonKeysToUnderscores }}"
     }
    }
   },
   "OutputFormatConfiguration": {
    "Serializer": {
     "OrcSerDe": {
      "BlockSizeBytes": "{{ BlockSizeBytes }}",
      "BloomFilterColumns": [
       "{{ BloomFilterColumns[0] }}"
      ],
      "BloomFilterFalsePositiveProbability": null,
      "Compression": "{{ Compression }}",
      "DictionaryKeyThreshold": null,
      "EnablePadding": "{{ EnablePadding }}",
      "FormatVersion": "{{ FormatVersion }}",
      "PaddingTolerance": null,
      "RowIndexStride": "{{ RowIndexStride }}",
      "StripeSizeBytes": "{{ StripeSizeBytes }}"
     },
     "ParquetSerDe": {
      "BlockSizeBytes": "{{ BlockSizeBytes }}",
      "Compression": "{{ Compression }}",
      "EnableDictionaryCompression": "{{ EnableDictionaryCompression }}",
      "MaxPaddingBytes": "{{ MaxPaddingBytes }}",
      "PageSizeBytes": "{{ PageSizeBytes }}",
      "WriterVersion": "{{ WriterVersion }}"
     }
    }
   },
   "SchemaConfiguration": {
    "CatalogId": "{{ CatalogId }}",
    "DatabaseName": "{{ DatabaseName }}",
    "Region": "{{ Region }}",
    "RoleARN": "{{ RoleARN }}",
    "TableName": "{{ TableName }}",
    "VersionId": "{{ VersionId }}"
   }
  },
  "DynamicPartitioningConfiguration": {
   "Enabled": "{{ Enabled }}",
   "RetryOptions": {
    "DurationInSeconds": "{{ DurationInSeconds }}"
   }
  },
  "EncryptionConfiguration": null,
  "ErrorOutputPrefix": "{{ ErrorOutputPrefix }}",
  "FileExtension": "{{ FileExtension }}",
  "Prefix": "{{ Prefix }}",
  "ProcessingConfiguration": null,
  "RoleARN": "{{ RoleARN }}",
  "S3BackupConfiguration": null,
  "S3BackupMode": "{{ S3BackupMode }}"
 },
 "KinesisStreamSourceConfiguration": {
  "KinesisStreamARN": "{{ KinesisStreamARN }}",
  "RoleARN": "{{ RoleARN }}"
 },
 "MSKSourceConfiguration": {
  "MSKClusterARN": "{{ MSKClusterARN }}",
  "TopicName": "{{ TopicName }}",
  "AuthenticationConfiguration": {
   "RoleARN": "{{ RoleARN }}",
   "Connectivity": "{{ Connectivity }}"
  }
 },
 "RedshiftDestinationConfiguration": {
  "CloudWatchLoggingOptions": null,
  "ClusterJDBCURL": "{{ ClusterJDBCURL }}",
  "CopyCommand": {
   "CopyOptions": "{{ CopyOptions }}",
   "DataTableColumns": "{{ DataTableColumns }}",
   "DataTableName": "{{ DataTableName }}"
  },
  "Password": "{{ Password }}",
  "ProcessingConfiguration": null,
  "RetryOptions": {
   "DurationInSeconds": "{{ DurationInSeconds }}"
  },
  "RoleARN": "{{ RoleARN }}",
  "S3BackupConfiguration": null,
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": null,
  "Username": "{{ Username }}"
 },
 "S3DestinationConfiguration": null,
 "SplunkDestinationConfiguration": {
  "CloudWatchLoggingOptions": null,
  "HECAcknowledgmentTimeoutInSeconds": "{{ HECAcknowledgmentTimeoutInSeconds }}",
  "HECEndpoint": "{{ HECEndpoint }}",
  "HECEndpointType": "{{ HECEndpointType }}",
  "HECToken": "{{ HECToken }}",
  "ProcessingConfiguration": null,
  "RetryOptions": {
   "DurationInSeconds": "{{ DurationInSeconds }}"
  },
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": null,
  "BufferingHints": {
   "IntervalInSeconds": "{{ IntervalInSeconds }}",
   "SizeInMBs": "{{ SizeInMBs }}"
  }
 },
 "HttpEndpointDestinationConfiguration": {
  "RoleARN": "{{ RoleARN }}",
  "EndpointConfiguration": {
   "Url": "{{ Url }}",
   "AccessKey": "{{ AccessKey }}",
   "Name": "{{ Name }}"
  },
  "RequestConfiguration": {
   "ContentEncoding": "{{ ContentEncoding }}",
   "CommonAttributes": [
    {
     "AttributeName": "{{ AttributeName }}",
     "AttributeValue": "{{ AttributeValue }}"
    }
   ]
  },
  "BufferingHints": null,
  "CloudWatchLoggingOptions": null,
  "ProcessingConfiguration": null,
  "RetryOptions": null,
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": null
 },
 "SnowflakeDestinationConfiguration": {
  "AccountUrl": "{{ AccountUrl }}",
  "PrivateKey": "{{ PrivateKey }}",
  "KeyPassphrase": "{{ KeyPassphrase }}",
  "User": "{{ User }}",
  "Database": "{{ Database }}",
  "Schema": "{{ Schema }}",
  "Table": "{{ Table }}",
  "SnowflakeRoleConfiguration": {
   "Enabled": "{{ Enabled }}",
   "SnowflakeRole": "{{ SnowflakeRole }}"
  },
  "DataLoadingOption": "{{ DataLoadingOption }}",
  "MetaDataColumnName": "{{ MetaDataColumnName }}",
  "ContentColumnName": "{{ ContentColumnName }}",
  "SnowflakeVpcConfiguration": {
   "PrivateLinkVpceId": "{{ PrivateLinkVpceId }}"
  },
  "CloudWatchLoggingOptions": null,
  "ProcessingConfiguration": null,
  "RoleARN": "{{ RoleARN }}",
  "RetryOptions": {
   "DurationInSeconds": "{{ DurationInSeconds }}"
  },
  "S3BackupMode": "{{ S3BackupMode }}",
  "S3Configuration": null
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ DeliveryStreamEncryptionConfigurationInput }},
 {{ DeliveryStreamName }},
 {{ DeliveryStreamType }},
 {{ ElasticsearchDestinationConfiguration }},
 {{ AmazonopensearchserviceDestinationConfiguration }},
 {{ AmazonOpenSearchServerlessDestinationConfiguration }},
 {{ ExtendedS3DestinationConfiguration }},
 {{ KinesisStreamSourceConfiguration }},
 {{ MSKSourceConfiguration }},
 {{ RedshiftDestinationConfiguration }},
 {{ S3DestinationConfiguration }},
 {{ SplunkDestinationConfiguration }},
 {{ HttpEndpointDestinationConfiguration }},
 {{ SnowflakeDestinationConfiguration }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

