---
title: certificate_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_providers
  - iot
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

Creates, updates, deletes or gets a <code>certificate_provider</code> resource or lists <code>certificate_providers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Use the AWS::IoT::CertificateProvider resource to declare an AWS IoT Certificate Provider.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.certificate_providers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="certificate_provider_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="lambda_function_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="account_default_for_operations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="LambdaFunctionArn, AccountDefaultForOperations, region" /></td>
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
List all <code>certificate_providers</code> in a region.
```sql
SELECT
region,
certificate_provider_name
FROM aws.iot.certificate_providers
WHERE region = 'us-east-1';
```
Gets all properties from a <code>certificate_provider</code>.
```sql
SELECT
region,
certificate_provider_name,
lambda_function_arn,
account_default_for_operations,
tags,
arn
FROM aws.iot.certificate_providers
WHERE region = 'us-east-1' AND data__Identifier = '<CertificateProviderName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate_provider</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.certificate_providers (
 LambdaFunctionArn,
 AccountDefaultForOperations,
 region
)
SELECT 
'{{ LambdaFunctionArn }}',
 '{{ AccountDefaultForOperations }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.certificate_providers (
 CertificateProviderName,
 LambdaFunctionArn,
 AccountDefaultForOperations,
 Tags,
 region
)
SELECT 
 '{{ CertificateProviderName }}',
 '{{ LambdaFunctionArn }}',
 '{{ AccountDefaultForOperations }}',
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
  - name: certificate_provider
    props:
      - name: CertificateProviderName
        value: '{{ CertificateProviderName }}'
      - name: LambdaFunctionArn
        value: '{{ LambdaFunctionArn }}'
      - name: AccountDefaultForOperations
        value:
          - '{{ AccountDefaultForOperations[0] }}'
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
DELETE FROM aws.iot.certificate_providers
WHERE data__Identifier = '<CertificateProviderName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>certificate_providers</code> resource, the following permissions are required:

### Create
```json
iot:CreateCertificateProvider,
iot:DescribeCertificateProvider,
iot:TagResource,
iot:ListTagsForResource
```

### Read
```json
iot:DescribeCertificateProvider,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateCertificateProvider,
iot:DescribeCertificateProvider,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

### Delete
```json
iot:DeleteCertificateProvider,
iot:DescribeCertificateProvider
```

### List
```json
iot:ListCertificateProviders
```

