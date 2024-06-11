---
title: data_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - data_providers
  - dms
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

Creates, updates, deletes or gets a <code>data_provider</code> resource or lists <code>data_providers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DMS::DataProvider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.data_providers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="data_provider_name" /></td><td><code>string</code></td><td>The property describes a name to identify the data provider.</td></tr>
<tr><td><CopyableCode code="data_provider_identifier" /></td><td><code>string</code></td><td>The property describes an identifier for the data provider. It is used for describing/deleting/modifying can be name/arn</td></tr>
<tr><td><CopyableCode code="data_provider_arn" /></td><td><code>string</code></td><td>The data provider ARN.</td></tr>
<tr><td><CopyableCode code="data_provider_creation_time" /></td><td><code>string</code></td><td>The data provider creation time.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The optional description of the data provider.</td></tr>
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>The property describes a data engine for the data provider.</td></tr>
<tr><td><CopyableCode code="exact_settings" /></td><td><code>boolean</code></td><td>The property describes the exact settings which can be modified</td></tr>
<tr><td><CopyableCode code="settings" /></td><td><code>object</code></td><td>The property identifies the exact type of settings for the data provider.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="Engine, region" /></td>
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
List all <code>data_providers</code> in a region.
```sql
SELECT
region,
data_provider_arn
FROM aws.dms.data_providers
WHERE region = 'us-east-1';
```
Gets all properties from a <code>data_provider</code>.
```sql
SELECT
region,
data_provider_name,
data_provider_identifier,
data_provider_arn,
data_provider_creation_time,
description,
engine,
exact_settings,
settings,
tags
FROM aws.dms.data_providers
WHERE region = 'us-east-1' AND data__Identifier = '<DataProviderArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_provider</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.dms.data_providers (
 Engine,
 region
)
SELECT 
'{{ Engine }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.dms.data_providers (
 DataProviderName,
 DataProviderIdentifier,
 Description,
 Engine,
 ExactSettings,
 Settings,
 Tags,
 region
)
SELECT 
 '{{ DataProviderName }}',
 '{{ DataProviderIdentifier }}',
 '{{ Description }}',
 '{{ Engine }}',
 '{{ ExactSettings }}',
 '{{ Settings }}',
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
  - name: data_provider
    props:
      - name: DataProviderName
        value: '{{ DataProviderName }}'
      - name: DataProviderIdentifier
        value: '{{ DataProviderIdentifier }}'
      - name: Description
        value: '{{ Description }}'
      - name: Engine
        value: '{{ Engine }}'
      - name: ExactSettings
        value: '{{ ExactSettings }}'
      - name: Settings
        value:
          PostgreSqlSettings:
            ServerName: '{{ ServerName }}'
            Port: '{{ Port }}'
            DatabaseName: '{{ DatabaseName }}'
            SslMode: '{{ SslMode }}'
            CertificateArn: '{{ CertificateArn }}'
          MySqlSettings:
            ServerName: '{{ ServerName }}'
            Port: '{{ Port }}'
            SslMode: null
            CertificateArn: '{{ CertificateArn }}'
          OracleSettings:
            ServerName: '{{ ServerName }}'
            Port: '{{ Port }}'
            DatabaseName: '{{ DatabaseName }}'
            SslMode: null
            CertificateArn: '{{ CertificateArn }}'
            AsmServer: '{{ AsmServer }}'
            SecretsManagerOracleAsmSecretId: '{{ SecretsManagerOracleAsmSecretId }}'
            SecretsManagerOracleAsmAccessRoleArn: '{{ SecretsManagerOracleAsmAccessRoleArn }}'
            SecretsManagerSecurityDbEncryptionSecretId: '{{ SecretsManagerSecurityDbEncryptionSecretId }}'
            SecretsManagerSecurityDbEncryptionAccessRoleArn: '{{ SecretsManagerSecurityDbEncryptionAccessRoleArn }}'
          MicrosoftSqlServerSettings:
            ServerName: '{{ ServerName }}'
            Port: '{{ Port }}'
            DatabaseName: '{{ DatabaseName }}'
            SslMode: null
            CertificateArn: '{{ CertificateArn }}'
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
DELETE FROM aws.dms.data_providers
WHERE data__Identifier = '<DataProviderArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_providers</code> resource, the following permissions are required:

### Create
```json
dms:CreateDataProvider,
dms:ListDataProviders,
dms:DescribeDataProviders,
dms:AddTagsToResource,
dms:ListTagsForResource
```

### Read
```json
dms:ListDataProviders,
dms:DescribeDataProviders,
dms:ListTagsForResource
```

### Update
```json
dms:UpdateDataProvider,
dms:ModifyDataProvider,
dms:AddTagsToResource,
dms:RemoveTagsToResource,
dms:ListTagsForResource
```

### Delete
```json
dms:DeleteDataProvider
```

### List
```json
dms:ListDataProviders,
dms:DescribeDataProviders,
dms:ListTagsForResource
```

