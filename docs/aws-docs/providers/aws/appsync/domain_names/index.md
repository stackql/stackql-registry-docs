---
title: domain_names
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_names
  - appsync
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


Used to retrieve a list of <code>domain_names</code> in a region or to create or delete a <code>domain_names</code> resource, use <code>domain_name</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppSync::DomainName</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appsync.domain_names" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
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
domain_name
FROM aws.appsync.domain_names
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- domain_name.iql (required properties only)
INSERT INTO aws.appsync.domain_names (
 DomainName,
 CertificateArn,
 region
)
SELECT 
'{{ DomainName }}',
 '{{ CertificateArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- domain_name.iql (all properties)
INSERT INTO aws.appsync.domain_names (
 DomainName,
 Description,
 CertificateArn,
 region
)
SELECT 
 '{{ DomainName }}',
 '{{ Description }}',
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
      - name: DomainName
        value: '{{ DomainName }}'
      - name: Description
        value: '{{ Description }}'
      - name: CertificateArn
        value: '{{ CertificateArn }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.appsync.domain_names
WHERE data__Identifier = '<DomainName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>domain_names</code> resource, the following permissions are required:

### Create
```json
appsync:CreateDomainName,
appsync:GetDomainName,
acm:DescribeCertificate,
cloudfront:UpdateDistribution
```

### Delete
```json
appsync:GetDomainName,
appsync:DeleteDomainName
```

### List
```json
appsync:ListDomainNames
```

