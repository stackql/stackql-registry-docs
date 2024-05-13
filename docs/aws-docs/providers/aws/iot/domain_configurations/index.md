---
title: domain_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_configurations
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


Used to retrieve a list of <code>domain_configurations</code> in a region or to create or delete a <code>domain_configurations</code> resource, use <code>domain_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage a Domain Configuration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.domain_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_configuration_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code=", region" /></td>
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
domain_configuration_name
FROM aws.iot.domain_configurations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>domain_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.domain_configurations (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.domain_configurations (
 DomainConfigurationName,
 AuthorizerConfig,
 DomainName,
 ServerCertificateArns,
 ServiceType,
 ValidationCertificateArn,
 DomainConfigurationStatus,
 ServerCertificateConfig,
 TlsConfig,
 Tags,
 region
)
SELECT 
 '{{ DomainConfigurationName }}',
 '{{ AuthorizerConfig }}',
 '{{ DomainName }}',
 '{{ ServerCertificateArns }}',
 '{{ ServiceType }}',
 '{{ ValidationCertificateArn }}',
 '{{ DomainConfigurationStatus }}',
 '{{ ServerCertificateConfig }}',
 '{{ TlsConfig }}',
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
  - name: domain_configuration
    props:
      - name: DomainConfigurationName
        value: '{{ DomainConfigurationName }}'
      - name: AuthorizerConfig
        value:
          AllowAuthorizerOverride: '{{ AllowAuthorizerOverride }}'
          DefaultAuthorizerName: '{{ DefaultAuthorizerName }}'
      - name: DomainName
        value: '{{ DomainName }}'
      - name: ServerCertificateArns
        value:
          - '{{ ServerCertificateArns[0] }}'
      - name: ServiceType
        value: '{{ ServiceType }}'
      - name: ValidationCertificateArn
        value: '{{ ValidationCertificateArn }}'
      - name: DomainConfigurationStatus
        value: '{{ DomainConfigurationStatus }}'
      - name: ServerCertificateConfig
        value:
          EnableOCSPCheck: '{{ EnableOCSPCheck }}'
      - name: TlsConfig
        value:
          SecurityPolicy: '{{ SecurityPolicy }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.iot.domain_configurations
WHERE data__Identifier = '<DomainConfigurationName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>domain_configurations</code> resource, the following permissions are required:

### Create
```json
iot:CreateDomainConfiguration,
iot:UpdateDomainConfiguration,
iot:DescribeDomainConfiguration,
iot:TagResource,
iot:ListTagsForResource,
acm:GetCertificate
```

### Delete
```json
iot:DescribeDomainConfiguration,
iot:DeleteDomainConfiguration,
iot:UpdateDomainConfiguration
```

### List
```json
iot:ListDomainConfigurations
```

