---
title: domain_name_v2s
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_name_v2s
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

Creates, updates, deletes or gets a <code>domain_name_v2</code> resource or lists <code>domain_name_v2s</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_name_v2s</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ApiGateway::DomainNameV2.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.domain_name_v2s" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_configuration" /></td><td><code>object</code></td><td>The <code>EndpointConfiguration</code> property type specifies the endpoint types of a REST API.<br /><code>EndpointConfiguration</code> is a property of the &#91;AWS::ApiGateway::RestApi&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html) resource.</td></tr>
<tr><td><CopyableCode code="security_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name_arn" /></td><td><code>string</code></td><td>The amazon resource name (ARN) of the domain name resource.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2.html"><code>AWS::ApiGateway::DomainNameV2</code></a>.

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
Gets all <code>domain_name_v2s</code> in a region.
```sql
SELECT
region,
certificate_arn,
domain_name,
endpoint_configuration,
security_policy,
policy,
domain_name_id,
domain_name_arn,
tags
FROM aws.apigateway.domain_name_v2s
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>domain_name_v2</code>.
```sql
SELECT
region,
certificate_arn,
domain_name,
endpoint_configuration,
security_policy,
policy,
domain_name_id,
domain_name_arn,
tags
FROM aws.apigateway.domain_name_v2s
WHERE region = 'us-east-1' AND data__Identifier = '<DomainNameArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domain_name_v2</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.domain_name_v2s (
 CertificateArn,
 DomainName,
 EndpointConfiguration,
 SecurityPolicy,
 Policy,
 Tags,
 region
)
SELECT 
'{{ CertificateArn }}',
 '{{ DomainName }}',
 '{{ EndpointConfiguration }}',
 '{{ SecurityPolicy }}',
 '{{ Policy }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.domain_name_v2s (
 CertificateArn,
 DomainName,
 EndpointConfiguration,
 SecurityPolicy,
 Policy,
 Tags,
 region
)
SELECT 
 '{{ CertificateArn }}',
 '{{ DomainName }}',
 '{{ EndpointConfiguration }}',
 '{{ SecurityPolicy }}',
 '{{ Policy }}',
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
  - name: domain_name_v2
    props:
      - name: CertificateArn
        value: '{{ CertificateArn }}'
      - name: DomainName
        value: '{{ DomainName }}'
      - name: EndpointConfiguration
        value:
          Types:
            - '{{ Types[0] }}'
          VpcEndpointIds:
            - '{{ VpcEndpointIds[0] }}'
      - name: SecurityPolicy
        value: '{{ SecurityPolicy }}'
      - name: Policy
        value: {}
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
DELETE FROM aws.apigateway.domain_name_v2s
WHERE data__Identifier = '<DomainNameArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>domain_name_v2s</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:GET,
apigateway:UpdateDomainNamePolicy
```

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:PUT,
apigateway:PATCH,
apigateway:UpdateDomainNamePolicy
```

### Delete
```json
apigateway:DELETE,
apigateway:GET,
apigateway:UpdateDomainNamePolicy
```

### List
```json
apigateway:GET
```
