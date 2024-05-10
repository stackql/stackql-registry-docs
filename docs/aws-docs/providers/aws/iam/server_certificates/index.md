---
title: server_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - server_certificates
  - iam
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


Used to retrieve a list of <code>server_certificates</code> in a region or to create or delete a <code>server_certificates</code> resource, use <code>server_certificate</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IAM::ServerCertificate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.server_certificates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="server_certificate_name" /></td><td><code>string</code></td><td></td></tr>
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
server_certificate_name
FROM aws.iam.server_certificates
;
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
 "CertificateBody": "{{ CertificateBody }}",
 "CertificateChain": "{{ CertificateChain }}",
 "ServerCertificateName": "{{ ServerCertificateName }}",
 "Path": "{{ Path }}",
 "PrivateKey": "{{ PrivateKey }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.iam.server_certificates (
 CertificateBody,
 CertificateChain,
 ServerCertificateName,
 Path,
 PrivateKey,
 Tags,
 region
)
SELECT 
{{ CertificateBody }},
 {{ CertificateChain }},
 {{ ServerCertificateName }},
 {{ Path }},
 {{ PrivateKey }},
 {{ Tags }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CertificateBody": "{{ CertificateBody }}",
 "CertificateChain": "{{ CertificateChain }}",
 "ServerCertificateName": "{{ ServerCertificateName }}",
 "Path": "{{ Path }}",
 "PrivateKey": "{{ PrivateKey }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.iam.server_certificates (
 CertificateBody,
 CertificateChain,
 ServerCertificateName,
 Path,
 PrivateKey,
 Tags,
 region
)
SELECT 
 {{ CertificateBody }},
 {{ CertificateChain }},
 {{ ServerCertificateName }},
 {{ Path }},
 {{ PrivateKey }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iam.server_certificates
WHERE data__Identifier = '<ServerCertificateName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>server_certificates</code> resource, the following permissions are required:

### Create
```json
iam:UploadServerCertificate,
iam:TagServerCertificate,
iam:GetServerCertificate
```

### Delete
```json
iam:DeleteServerCertificate
```

### List
```json
iam:ListServerCertificates,
iam:GetServerCertificate
```

