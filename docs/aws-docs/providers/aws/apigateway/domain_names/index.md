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
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="mutual_tls_authentication" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="ownership_verification_certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="regional_hosted_zone_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="regional_domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="security_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="distribution_hosted_zone_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_configuration" /></td><td><code>object</code></td><td>The <code>EndpointConfiguration</code> property type specifies the endpoint types of a REST API.<br /><code>EndpointConfiguration</code> is a property of the &#91;AWS::ApiGateway::RestApi&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html) resource.</td></tr>
<tr><td><CopyableCode code="distribution_domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="regional_certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html"><code>AWS::ApiGateway::DomainName</code></a>.

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
Gets all <code>domain_names</code> in a region.
```sql
SELECT
region,
mutual_tls_authentication,
ownership_verification_certificate_arn,
regional_hosted_zone_id,
regional_domain_name,
domain_name,
security_policy,
distribution_hosted_zone_id,
endpoint_configuration,
distribution_domain_name,
regional_certificate_arn,
tags,
certificate_arn
FROM aws.apigateway.domain_names
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>domain_name</code>.
```sql
SELECT
region,
mutual_tls_authentication,
ownership_verification_certificate_arn,
regional_hosted_zone_id,
regional_domain_name,
domain_name,
security_policy,
distribution_hosted_zone_id,
endpoint_configuration,
distribution_domain_name,
regional_certificate_arn,
tags,
certificate_arn
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
 MutualTlsAuthentication,
 OwnershipVerificationCertificateArn,
 DomainName,
 SecurityPolicy,
 EndpointConfiguration,
 RegionalCertificateArn,
 Tags,
 CertificateArn,
 region
)
SELECT 
'{{ MutualTlsAuthentication }}',
 '{{ OwnershipVerificationCertificateArn }}',
 '{{ DomainName }}',
 '{{ SecurityPolicy }}',
 '{{ EndpointConfiguration }}',
 '{{ RegionalCertificateArn }}',
 '{{ Tags }}',
 '{{ CertificateArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.domain_names (
 MutualTlsAuthentication,
 OwnershipVerificationCertificateArn,
 DomainName,
 SecurityPolicy,
 EndpointConfiguration,
 RegionalCertificateArn,
 Tags,
 CertificateArn,
 region
)
SELECT 
 '{{ MutualTlsAuthentication }}',
 '{{ OwnershipVerificationCertificateArn }}',
 '{{ DomainName }}',
 '{{ SecurityPolicy }}',
 '{{ EndpointConfiguration }}',
 '{{ RegionalCertificateArn }}',
 '{{ Tags }}',
 '{{ CertificateArn }}',
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
      - name: MutualTlsAuthentication
        value:
          TruststoreVersion: '{{ TruststoreVersion }}'
          TruststoreUri: '{{ TruststoreUri }}'
      - name: OwnershipVerificationCertificateArn
        value: '{{ OwnershipVerificationCertificateArn }}'
      - name: DomainName
        value: '{{ DomainName }}'
      - name: SecurityPolicy
        value: '{{ SecurityPolicy }}'
      - name: EndpointConfiguration
        value:
          Types:
            - '{{ Types[0] }}'
          VpcEndpointIds:
            - '{{ VpcEndpointIds[0] }}'
      - name: RegionalCertificateArn
        value: '{{ RegionalCertificateArn }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: CertificateArn
        value: '{{ CertificateArn }}'

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

### Read
```json
apigateway:*
```

### Create
```json
apigateway:*
```

### Update
```json
apigateway:*
```

### List
```json
apigateway:*
```

### Delete
```json
apigateway:*
```
