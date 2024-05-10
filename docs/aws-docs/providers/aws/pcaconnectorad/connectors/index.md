---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
  - pcaconnectorad
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


Used to retrieve a list of <code>connectors</code> in a region or to create or delete a <code>connectors</code> resource, use <code>connector</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::PCAConnectorAD::Connector Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcaconnectorad.connectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="connector_arn" /></td><td><code>string</code></td><td></td></tr>
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
connector_arn
FROM aws.pcaconnectorad.connectors
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "CertificateAuthorityArn": "{{ CertificateAuthorityArn }}",
 "DirectoryId": "{{ DirectoryId }}",
 "VpcInformation": {
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ]
 }
}
>>>
--required properties only
INSERT INTO aws.pcaconnectorad.connectors (
 CertificateAuthorityArn,
 DirectoryId,
 VpcInformation,
 region
)
SELECT 
{{ .CertificateAuthorityArn }},
 {{ .DirectoryId }},
 {{ .VpcInformation }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CertificateAuthorityArn": "{{ CertificateAuthorityArn }}",
 "DirectoryId": "{{ DirectoryId }}",
 "Tags": {},
 "VpcInformation": {
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ]
 }
}
>>>
--all properties
INSERT INTO aws.pcaconnectorad.connectors (
 CertificateAuthorityArn,
 DirectoryId,
 Tags,
 VpcInformation,
 region
)
SELECT 
 {{ .CertificateAuthorityArn }},
 {{ .DirectoryId }},
 {{ .Tags }},
 {{ .VpcInformation }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.pcaconnectorad.connectors
WHERE data__Identifier = '<ConnectorArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>connectors</code> resource, the following permissions are required:

### Create
```json
acm-pca:DescribeCertificateAuthority,
acm-pca:GetCertificateAuthorityCertificate,
acm-pca:GetCertificate,
acm-pca:IssueCertificate,
ds:DescribeDirectories,
ec2:CreateTags,
ec2:CreateVpcEndpoint,
ec2:DescribeVpcEndpoints,
pca-connector-ad:CreateConnector,
pca-connector-ad:GetConnector
```

### Delete
```json
pca-connector-ad:GetConnector,
pca-connector-ad:DeleteConnector,
ec2:DeleteVpcEndpoints,
ec2:DescribeVpcEndpoints
```

### List
```json
pca-connector-ad:ListConnectors
```

