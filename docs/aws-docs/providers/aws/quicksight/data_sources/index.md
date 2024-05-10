---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
  - quicksight
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


Used to retrieve a list of <code>data_sources</code> in a region or to create or delete a <code>data_sources</code> resource, use <code>data_source</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::DataSource Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.data_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_source_id" /></td><td><code>string</code></td><td></td></tr>
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
aws_account_id,
data_source_id
FROM aws.quicksight.data_sources
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
 "AlternateDataSourceParameters": [
  {
   "AuroraPostgreSqlParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "TeradataParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "RdsParameters": {
    "InstanceId": "{{ InstanceId }}",
    "Database": "{{ Database }}"
   },
   "AthenaParameters": {
    "WorkGroup": "{{ WorkGroup }}",
    "RoleArn": "{{ RoleArn }}"
   },
   "SparkParameters": {
    "Port": null,
    "Host": "{{ Host }}"
   },
   "MariaDbParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "OracleParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "PrestoParameters": {
    "Port": null,
    "Host": "{{ Host }}",
    "Catalog": "{{ Catalog }}"
   },
   "RedshiftParameters": {
    "ClusterId": "{{ ClusterId }}",
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "MySqlParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "SqlServerParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "SnowflakeParameters": {
    "Warehouse": "{{ Warehouse }}",
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "AmazonElasticsearchParameters": {
    "Domain": "{{ Domain }}"
   },
   "AmazonOpenSearchParameters": {
    "Domain": "{{ Domain }}"
   },
   "PostgreSqlParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "AuroraParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "S3Parameters": {
    "ManifestFileLocation": {
     "Bucket": "{{ Bucket }}",
     "Key": "{{ Key }}"
    },
    "RoleArn": "{{ RoleArn }}"
   },
   "DatabricksParameters": {
    "Host": "{{ Host }}",
    "Port": null,
    "SqlEndpointPath": "{{ SqlEndpointPath }}"
   },
   "StarburstParameters": {
    "Host": "{{ Host }}",
    "Port": null,
    "Catalog": "{{ Catalog }}",
    "ProductType": "{{ ProductType }}"
   },
   "TrinoParameters": {
    "Host": "{{ Host }}",
    "Port": null,
    "Catalog": "{{ Catalog }}"
   }
  }
 ],
 "AwsAccountId": "{{ AwsAccountId }}",
 "Credentials": {
  "CopySourceArn": "{{ CopySourceArn }}",
  "CredentialPair": {
   "AlternateDataSourceParameters": [
    null
   ],
   "Username": "{{ Username }}",
   "Password": "{{ Password }}"
  },
  "SecretArn": "{{ SecretArn }}"
 },
 "DataSourceId": "{{ DataSourceId }}",
 "DataSourceParameters": null,
 "ErrorInfo": {
  "Type": "{{ Type }}",
  "Message": "{{ Message }}"
 },
 "Name": "{{ Name }}",
 "Permissions": [
  {
   "Principal": "{{ Principal }}",
   "Actions": [
    "{{ Actions[0] }}"
   ]
  }
 ],
 "SslProperties": {
  "DisableSsl": "{{ DisableSsl }}"
 },
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "Type": "{{ Type }}",
 "VpcConnectionProperties": {
  "VpcConnectionArn": "{{ VpcConnectionArn }}"
 }
}
>>>
--required properties only
INSERT INTO aws.quicksight.data_sources (
 AlternateDataSourceParameters,
 AwsAccountId,
 Credentials,
 DataSourceId,
 DataSourceParameters,
 ErrorInfo,
 Name,
 Permissions,
 SslProperties,
 Tags,
 Type,
 VpcConnectionProperties,
 region
)
SELECT 
{{ AlternateDataSourceParameters }},
 {{ AwsAccountId }},
 {{ Credentials }},
 {{ DataSourceId }},
 {{ DataSourceParameters }},
 {{ ErrorInfo }},
 {{ Name }},
 {{ Permissions }},
 {{ SslProperties }},
 {{ Tags }},
 {{ Type }},
 {{ VpcConnectionProperties }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AlternateDataSourceParameters": [
  {
   "AuroraPostgreSqlParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "TeradataParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "RdsParameters": {
    "InstanceId": "{{ InstanceId }}",
    "Database": "{{ Database }}"
   },
   "AthenaParameters": {
    "WorkGroup": "{{ WorkGroup }}",
    "RoleArn": "{{ RoleArn }}"
   },
   "SparkParameters": {
    "Port": null,
    "Host": "{{ Host }}"
   },
   "MariaDbParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "OracleParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "PrestoParameters": {
    "Port": null,
    "Host": "{{ Host }}",
    "Catalog": "{{ Catalog }}"
   },
   "RedshiftParameters": {
    "ClusterId": "{{ ClusterId }}",
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "MySqlParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "SqlServerParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "SnowflakeParameters": {
    "Warehouse": "{{ Warehouse }}",
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "AmazonElasticsearchParameters": {
    "Domain": "{{ Domain }}"
   },
   "AmazonOpenSearchParameters": {
    "Domain": "{{ Domain }}"
   },
   "PostgreSqlParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "AuroraParameters": {
    "Port": null,
    "Database": "{{ Database }}",
    "Host": "{{ Host }}"
   },
   "S3Parameters": {
    "ManifestFileLocation": {
     "Bucket": "{{ Bucket }}",
     "Key": "{{ Key }}"
    },
    "RoleArn": "{{ RoleArn }}"
   },
   "DatabricksParameters": {
    "Host": "{{ Host }}",
    "Port": null,
    "SqlEndpointPath": "{{ SqlEndpointPath }}"
   },
   "StarburstParameters": {
    "Host": "{{ Host }}",
    "Port": null,
    "Catalog": "{{ Catalog }}",
    "ProductType": "{{ ProductType }}"
   },
   "TrinoParameters": {
    "Host": "{{ Host }}",
    "Port": null,
    "Catalog": "{{ Catalog }}"
   }
  }
 ],
 "AwsAccountId": "{{ AwsAccountId }}",
 "Credentials": {
  "CopySourceArn": "{{ CopySourceArn }}",
  "CredentialPair": {
   "AlternateDataSourceParameters": [
    null
   ],
   "Username": "{{ Username }}",
   "Password": "{{ Password }}"
  },
  "SecretArn": "{{ SecretArn }}"
 },
 "DataSourceId": "{{ DataSourceId }}",
 "DataSourceParameters": null,
 "ErrorInfo": {
  "Type": "{{ Type }}",
  "Message": "{{ Message }}"
 },
 "Name": "{{ Name }}",
 "Permissions": [
  {
   "Principal": "{{ Principal }}",
   "Actions": [
    "{{ Actions[0] }}"
   ]
  }
 ],
 "SslProperties": {
  "DisableSsl": "{{ DisableSsl }}"
 },
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "Type": "{{ Type }}",
 "VpcConnectionProperties": {
  "VpcConnectionArn": "{{ VpcConnectionArn }}"
 }
}
>>>
--all properties
INSERT INTO aws.quicksight.data_sources (
 AlternateDataSourceParameters,
 AwsAccountId,
 Credentials,
 DataSourceId,
 DataSourceParameters,
 ErrorInfo,
 Name,
 Permissions,
 SslProperties,
 Tags,
 Type,
 VpcConnectionProperties,
 region
)
SELECT 
 {{ AlternateDataSourceParameters }},
 {{ AwsAccountId }},
 {{ Credentials }},
 {{ DataSourceId }},
 {{ DataSourceParameters }},
 {{ ErrorInfo }},
 {{ Name }},
 {{ Permissions }},
 {{ SslProperties }},
 {{ Tags }},
 {{ Type }},
 {{ VpcConnectionProperties }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.quicksight.data_sources
WHERE data__Identifier = '<AwsAccountId|DataSourceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_sources</code> resource, the following permissions are required:

### Create
```json
quicksight:CreateDataSource,
quicksight:DescribeDataSource,
quicksight:DescribeDataSourcePermissions,
quicksight:TagResource,
quicksight:ListTagsForResource
```

### Delete
```json
quicksight:DescribeDataSource,
quicksight:DescribeDataSourcePermissions,
quicksight:DeleteDataSource,
quicksight:ListTagsForResource
```

### List
```json
quicksight:DescribeDataSource,
quicksight:ListDataSources
```

