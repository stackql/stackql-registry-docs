---
title: domain_names
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_names
  - apigateway
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

Creates, updates, deletes or gets a <code>domain_name</code> resource or lists <code>domain_names</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ApiGateway::DomainName.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.domain_names" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="distribution_domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="distribution_hosted_zone_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_configuration" /></td><td><code>The ``EndpointConfiguration`` property type specifies the endpoint types of a REST API.
 ``EndpointConfiguration`` is a property of the [AWS::ApiGateway::RestApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html) resource.</code></td><td></td></tr>
<tr><td><CopyableCode code="mutual_tls_authentication" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="regional_domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="regional_hosted_zone_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="regional_certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ownership_verification_certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="security_policy" /></td><td><code>string</code></td><td></td></tr>
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
List all <code>domain_names</code> in a region.
```sql
SELECT
region,
domain_name
FROM aws.apigateway.domain_names
WHERE region = 'us-east-1';
```
Gets all properties from a <code>domain_name</code>.
```sql
SELECT
region,
domain_name,
distribution_domain_name,
distribution_hosted_zone_id,
endpoint_configuration,
mutual_tls_authentication,
regional_domain_name,
regional_hosted_zone_id,
certificate_arn,
regional_certificate_arn,
ownership_verification_certificate_arn,
security_policy,
tags
FROM aws.apigateway.domain_names
WHERE region = 'us-east-1' AND data__Identifier = '<DomainName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domain_name</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.domain_names (
 DomainName,
 EndpointConfiguration,
 MutualTlsAuthentication,
 CertificateArn,
 RegionalCertificateArn,
 OwnershipVerificationCertificateArn,
 SecurityPolicy,
 Tags,
 region
)
SELECT 
'{{ DomainName }}',
 '{{ EndpointConfiguration }}',
 '{{ MutualTlsAuthentication }}',
 '{{ CertificateArn }}',
 '{{ RegionalCertificateArn }}',
 '{{ OwnershipVerificationCertificateArn }}',
 '{{ SecurityPolicy }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.domain_names (
 DomainName,
 EndpointConfiguration,
 MutualTlsAuthentication,
 CertificateArn,
 RegionalCertificateArn,
 OwnershipVerificationCertificateArn,
 SecurityPolicy,
 Tags,
 region
)
SELECT 
 '{{ DomainName }}',
 '{{ EndpointConfiguration }}',
 '{{ MutualTlsAuthentication }}',
 '{{ CertificateArn }}',
 '{{ RegionalCertificateArn }}',
 '{{ OwnershipVerificationCertificateArn }}',
 '{{ SecurityPolicy }}',
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
  - name: domain_name
    props:
      - name: DomainName
        value: '{{ DomainName }}'
      - name: EndpointConfiguration
        value:
          Types:
            - '{{ Types[0] }}'
          VpcEndpointIds:
            - '{{ VpcEndpointIds[0] }}'
      - name: MutualTlsAuthentication
        value:
          TruststoreUri: '{{ TruststoreUri }}'
          TruststoreVersion: '{{ TruststoreVersion }}'
      - name: CertificateArn
        value: '{{ CertificateArn }}'
      - name: RegionalCertificateArn
        value: '{{ RegionalCertificateArn }}'
      - name: OwnershipVerificationCertificateArn
        value: '{{ OwnershipVerificationCertificateArn }}'
      - name: SecurityPolicy
        value: '{{ SecurityPolicy }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.domain_names
WHERE data__Identifier = '<DomainName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>domain_names</code> resource, the following permissions are required:

### Create
```json
apigateway:*
```

### Read
```json
apigateway:*
```

### Update
```json
apigateway:*
```

### Delete
```json
apigateway:*
```

### List
```json
apigateway:*
```

