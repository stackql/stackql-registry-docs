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

Creates, updates, deletes or gets a <code>data_source</code> resource or lists <code>data_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::DataSource Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.data_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alternate_data_source_parameters" /></td><td><code>array</code></td><td><p>A set of alternate data source parameters that you want to share for the credentials<br />stored with this data source. The credentials are applied in tandem with the data source<br />parameters when you copy a data source by using a create or update request. The API<br />operation compares the <code>DataSourceParameters</code> structure that's in the request<br />with the structures in the <code>AlternateDataSourceParameters</code> allow list. If the<br />structures are an exact match, the request is allowed to use the credentials from this<br />existing data source. If the <code>AlternateDataSourceParameters</code> list is null,<br />the <code>Credentials</code> originally used with this <code>DataSourceParameters</code><br />are automatically allowed.</p></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) of the data source.</p></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td><p>The time that this data source was created.</p></td></tr>
<tr><td><CopyableCode code="credentials" /></td><td><code>object</code></td><td><p>Data source credentials. This is a variant type structure. For this structure to be<br />valid, only one of the attributes can be non-null.</p></td></tr>
<tr><td><CopyableCode code="data_source_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_source_parameters" /></td><td><code>object</code></td><td><p>The parameters that Amazon QuickSight uses to connect to your underlying data source.<br />This is a variant type structure. For this structure to be valid, only one of the<br />attributes can be non-null.</p></td></tr>
<tr><td><CopyableCode code="error_info" /></td><td><code>object</code></td><td><p>Error information for the data source creation or update.</p></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td><p>The last time that this data source was updated.</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="ssl_properties" /></td><td><code>object</code></td><td><p>Secure Socket Layer (SSL) properties that apply when Amazon QuickSight connects to your<br />underlying data source.</p></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_connection_properties" /></td><td><code>object</code></td><td><p>VPC connection properties.</p></td></tr>
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
    <td><CopyableCode code="Name, Type, region" /></td>
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
List all <code>data_sources</code> in a region.
```sql
SELECT
region,
aws_account_id,
data_source_id
FROM aws.quicksight.data_sources
WHERE region = 'us-east-1';
```
Gets all properties from a <code>data_source</code>.
```sql
SELECT
region,
alternate_data_source_parameters,
arn,
aws_account_id,
created_time,
credentials,
data_source_id,
data_source_parameters,
error_info,
last_updated_time,
name,
permissions,
ssl_properties,
status,
tags,
type,
vpc_connection_properties
FROM aws.quicksight.data_sources
WHERE region = 'us-east-1' AND data__Identifier = '<AwsAccountId>|<DataSourceId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_source</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.quicksight.data_sources (
 Name,
 Type,
 region
)
SELECT 
'{{ Name }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ AlternateDataSourceParameters }}',
 '{{ AwsAccountId }}',
 '{{ Credentials }}',
 '{{ DataSourceId }}',
 '{{ DataSourceParameters }}',
 '{{ ErrorInfo }}',
 '{{ Name }}',
 '{{ Permissions }}',
 '{{ SslProperties }}',
 '{{ Tags }}',
 '{{ Type }}',
 '{{ VpcConnectionProperties }}',
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
  - name: data_source
    props:
      - name: AlternateDataSourceParameters
        value:
          - AmazonElasticsearchParameters:
              Domain: '{{ Domain }}'
            AthenaParameters:
              WorkGroup: '{{ WorkGroup }}'
              RoleArn: '{{ RoleArn }}'
            AuroraParameters:
              Host: '{{ Host }}'
              Port: null
              Database: '{{ Database }}'
            AuroraPostgreSqlParameters:
              Host: '{{ Host }}'
              Port: null
              Database: '{{ Database }}'
            MariaDbParameters:
              Host: '{{ Host }}'
              Port: null
              Database: '{{ Database }}'
            MySqlParameters:
              Host: '{{ Host }}'
              Port: null
              Database: '{{ Database }}'
            OracleParameters:
              Host: '{{ Host }}'
              Port: null
              Database: '{{ Database }}'
            PostgreSqlParameters:
              Host: '{{ Host }}'
              Port: null
              Database: '{{ Database }}'
            PrestoParameters:
              Host: '{{ Host }}'
              Port: null
              Catalog: '{{ Catalog }}'
            RdsParameters:
              InstanceId: '{{ InstanceId }}'
              Database: '{{ Database }}'
            RedshiftParameters:
              Host: '{{ Host }}'
              Port: null
              Database: '{{ Database }}'
              ClusterId: '{{ ClusterId }}'
              IAMParameters:
                RoleArn: '{{ RoleArn }}'
                DatabaseUser: '{{ DatabaseUser }}'
                DatabaseGroups:
                  - '{{ DatabaseGroups[0] }}'
                AutoCreateDatabaseUser: '{{ AutoCreateDatabaseUser }}'
              IdentityCenterConfiguration:
                EnableIdentityPropagation: '{{ EnableIdentityPropagation }}'
            S3Parameters:
              ManifestFileLocation:
                Bucket: '{{ Bucket }}'
                Key: '{{ Key }}'
              RoleArn: '{{ RoleArn }}'
            SnowflakeParameters:
              Host: '{{ Host }}'
              Database: '{{ Database }}'
              Warehouse: '{{ Warehouse }}'
            SparkParameters:
              Host: '{{ Host }}'
              Port: null
            SqlServerParameters:
              Host: '{{ Host }}'
              Port: null
              Database: '{{ Database }}'
            TeradataParameters:
              Host: '{{ Host }}'
              Port: null
              Database: '{{ Database }}'
            AmazonOpenSearchParameters:
              Domain: '{{ Domain }}'
            DatabricksParameters:
              Host: '{{ Host }}'
              Port: null
              SqlEndpointPath: '{{ SqlEndpointPath }}'
            StarburstParameters:
              Host: '{{ Host }}'
              Port: null
              Catalog: '{{ Catalog }}'
              ProductType: '{{ ProductType }}'
            TrinoParameters:
              Host: '{{ Host }}'
              Port: null
              Catalog: '{{ Catalog }}'
      - name: AwsAccountId
        value: '{{ AwsAccountId }}'
      - name: Credentials
        value:
          CredentialPair:
            Username: '{{ Username }}'
            Password: '{{ Password }}'
            AlternateDataSourceParameters:
              - null
          CopySourceArn: '{{ CopySourceArn }}'
          SecretArn: '{{ SecretArn }}'
      - name: DataSourceId
        value: '{{ DataSourceId }}'
      - name: DataSourceParameters
        value: null
      - name: ErrorInfo
        value:
          Type: '{{ Type }}'
          Message: '{{ Message }}'
      - name: Name
        value: '{{ Name }}'
      - name: Permissions
        value:
          - Principal: '{{ Principal }}'
            Actions:
              - '{{ Actions[0] }}'
      - name: SslProperties
        value:
          DisableSsl: '{{ DisableSsl }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Type
        value: '{{ Type }}'
      - name: VpcConnectionProperties
        value:
          VpcConnectionArn: '{{ VpcConnectionArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.quicksight.data_sources
WHERE data__Identifier = '<AwsAccountId|DataSourceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_sources</code> resource, the following permissions are required:

### Read
```json
quicksight:DescribeDataSource,
quicksight:DescribeDataSourcePermissions,
quicksight:ListTagsForResource
```

### Create
```json
quicksight:CreateDataSource,
quicksight:DescribeDataSource,
quicksight:DescribeDataSourcePermissions,
quicksight:TagResource,
quicksight:ListTagsForResource
```

### Update
```json
quicksight:DescribeDataSource,
quicksight:DescribeDataSourcePermissions,
quicksight:UpdateDataSource,
quicksight:UpdateDataSourcePermissions,
quicksight:TagResource,
quicksight:UntagResource,
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

