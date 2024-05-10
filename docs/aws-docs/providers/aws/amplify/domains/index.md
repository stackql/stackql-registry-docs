---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - amplify
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


Used to retrieve a list of <code>domains</code> in a region or to create or delete a <code>domains</code> resource, use <code>domain</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Amplify::Domain resource allows you to connect a custom domain to your app.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplify.domains" /></td></tr>
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
FROM aws.amplify.domains
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
 "AppId": "{{ AppId }}",
 "DomainName": "{{ DomainName }}",
 "SubDomainSettings": [
  {
   "Prefix": "{{ Prefix }}",
   "BranchName": "{{ BranchName }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.amplify.domains (
 AppId,
 DomainName,
 SubDomainSettings,
 region
)
SELECT 
{{ AppId }},
 {{ DomainName }},
 {{ SubDomainSettings }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AppId": "{{ AppId }}",
 "AutoSubDomainCreationPatterns": [
  "{{ AutoSubDomainCreationPatterns[0] }}"
 ],
 "AutoSubDomainIAMRole": "{{ AutoSubDomainIAMRole }}",
 "CertificateSettings": {
  "CertificateType": "{{ CertificateType }}",
  "CustomCertificateArn": "{{ CustomCertificateArn }}"
 },
 "DomainName": "{{ DomainName }}",
 "EnableAutoSubDomain": "{{ EnableAutoSubDomain }}",
 "SubDomainSettings": [
  {
   "Prefix": "{{ Prefix }}",
   "BranchName": "{{ BranchName }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.amplify.domains (
 AppId,
 AutoSubDomainCreationPatterns,
 AutoSubDomainIAMRole,
 CertificateSettings,
 DomainName,
 EnableAutoSubDomain,
 SubDomainSettings,
 region
)
SELECT 
 {{ AppId }},
 {{ AutoSubDomainCreationPatterns }},
 {{ AutoSubDomainIAMRole }},
 {{ CertificateSettings }},
 {{ DomainName }},
 {{ EnableAutoSubDomain }},
 {{ SubDomainSettings }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.amplify.domains
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>domains</code> resource, the following permissions are required:

### Create
```json
amplify:CreateDomainAssociation,
route53:ListHostedZones,
route53:ChangeResourceRecordSets,
iam:PassRole,
amplify:TagResource
```

### Delete
```json
amplify:DeleteDomainAssociation,
iam:PassRole,
amplify:DeleteDomainAssociation
```

### List
```json
amplify:ListDomainAssociations,
iam:PassRole,
amplify:ListTagsForResource
```

