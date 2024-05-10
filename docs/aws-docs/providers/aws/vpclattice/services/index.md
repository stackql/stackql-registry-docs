---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - vpclattice
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


Used to retrieve a list of <code>services</code> in a region or to create or delete a <code>services</code> resource, use <code>service</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.services" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
arn
FROM aws.vpclattice.services
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
 "AuthType": "{{ AuthType }}",
 "DnsEntry": {
  "DomainName": "{{ DomainName }}",
  "HostedZoneId": "{{ HostedZoneId }}"
 },
 "Name": "{{ Name }}",
 "CertificateArn": "{{ CertificateArn }}",
 "CustomDomainName": "{{ CustomDomainName }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.vpclattice.services (
 AuthType,
 DnsEntry,
 Name,
 CertificateArn,
 CustomDomainName,
 Tags,
 region
)
SELECT 
{{ AuthType }},
 {{ DnsEntry }},
 {{ Name }},
 {{ CertificateArn }},
 {{ CustomDomainName }},
 {{ Tags }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AuthType": "{{ AuthType }}",
 "DnsEntry": {
  "DomainName": "{{ DomainName }}",
  "HostedZoneId": "{{ HostedZoneId }}"
 },
 "Name": "{{ Name }}",
 "CertificateArn": "{{ CertificateArn }}",
 "CustomDomainName": "{{ CustomDomainName }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.vpclattice.services (
 AuthType,
 DnsEntry,
 Name,
 CertificateArn,
 CustomDomainName,
 Tags,
 region
)
SELECT 
 {{ AuthType }},
 {{ DnsEntry }},
 {{ Name }},
 {{ CertificateArn }},
 {{ CustomDomainName }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.vpclattice.services
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>services</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:CreateService,
vpc-lattice:GetService,
vpc-lattice:ListTagsForResource,
vpc-lattice:TagResource,
acm:DescribeCertificate,
acm:ListCertificates,
iam:CreateServiceLinkedRole
```

### Delete
```json
vpc-lattice:DeleteService,
vpc-lattice:GetService
```

### List
```json
vpc-lattice:ListServices
```

