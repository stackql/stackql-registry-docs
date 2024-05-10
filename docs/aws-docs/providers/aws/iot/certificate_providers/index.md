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


Used to retrieve a list of <code>certificate_providers</code> in a region or to create or delete a <code>certificate_providers</code> resource, use <code>certificate_provider</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Use the AWS::IoT::CertificateProvider resource to declare an AWS IoT Certificate Provider.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.certificate_providers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="certificate_provider_name" /></td><td><code>string</code></td><td></td></tr>
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
certificate_provider_name
FROM aws.iot.certificate_providers
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- certificate_provider.iql (required properties only)
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
-- certificate_provider.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
iot:DeleteCertificateProvider,
iot:DescribeCertificateProvider
```

### List
```json
iot:ListCertificateProviders
```

