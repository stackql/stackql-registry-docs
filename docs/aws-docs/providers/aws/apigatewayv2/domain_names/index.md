---
title: domain_names
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_names
  - apigatewayv2
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
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGatewayV2::DomainName</code> resource specifies a custom domain name for your API in Amazon API Gateway (API Gateway). <br />You can use a custom domain name to provide a URL that's more intuitive and easier to recall. For more information about using custom domain names, see &#91;Set up Custom Domain Name for an API in API Gateway&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.domain_names" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="mutual_tls_authentication" /></td><td><code>object</code></td><td>The mutual TLS authentication configuration for a custom domain name.</td></tr>
<tr><td><CopyableCode code="regional_hosted_zone_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="regional_domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The custom domain name for your API in Amazon API Gateway. Uppercase letters and the underscore (<code>_</code>) character are not supported.</td></tr>
<tr><td><CopyableCode code="domain_name_configurations" /></td><td><code>array</code></td><td>The domain name configurations.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The collection of tags associated with a domain name.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html"><code>AWS::ApiGatewayV2::DomainName</code></a>.

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
    <td><CopyableCode code="DomainName, region" /></td>
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
regional_hosted_zone_id,
regional_domain_name,
domain_name,
domain_name_configurations,
tags
FROM aws.apigatewayv2.domain_names
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>domain_name</code>.
```sql
SELECT
region,
mutual_tls_authentication,
regional_hosted_zone_id,
regional_domain_name,
domain_name,
domain_name_configurations,
tags
FROM aws.apigatewayv2.domain_names
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
INSERT INTO aws.apigatewayv2.domain_names (
 DomainName,
 region
)
SELECT 
'{{ DomainName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigatewayv2.domain_names (
 MutualTlsAuthentication,
 DomainName,
 DomainNameConfigurations,
 Tags,
 region
)
SELECT 
 '{{ MutualTlsAuthentication }}',
 '{{ DomainName }}',
 '{{ DomainNameConfigurations }}',
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
      - name: MutualTlsAuthentication
        value:
          TruststoreVersion: '{{ TruststoreVersion }}'
          TruststoreUri: '{{ TruststoreUri }}'
      - name: DomainName
        value: '{{ DomainName }}'
      - name: DomainNameConfigurations
        value:
          - OwnershipVerificationCertificateArn: '{{ OwnershipVerificationCertificateArn }}'
            EndpointType: '{{ EndpointType }}'
            CertificateName: '{{ CertificateName }}'
            SecurityPolicy: '{{ SecurityPolicy }}'
            CertificateArn: '{{ CertificateArn }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigatewayv2.domain_names
WHERE data__Identifier = '<DomainName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>domain_names</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:GET,
apigateway:PUT
```

### Update
```json
apigateway:PATCH,
apigateway:GET,
apigateway:PUT
```

### Read
```json
apigateway:GET
```

### Delete
```json
apigateway:GET,
apigateway:DELETE
```

### List
```json
apigateway:GET
```
