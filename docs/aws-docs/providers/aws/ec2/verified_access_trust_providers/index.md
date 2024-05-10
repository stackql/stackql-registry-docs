---
title: verified_access_trust_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_access_trust_providers
  - ec2
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


Used to retrieve a list of <code>verified_access_trust_providers</code> in a region or to create or delete a <code>verified_access_trust_providers</code> resource, use <code>verified_access_trust_provider</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_trust_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::VerifiedAccessTrustProvider type describes a verified access trust provider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.verified_access_trust_providers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="verified_access_trust_provider_id" /></td><td><code>string</code></td><td>The ID of the Amazon Web Services Verified Access trust provider.</td></tr>
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
verified_access_trust_provider_id
FROM aws.ec2.verified_access_trust_providers
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
 "TrustProviderType": "{{ TrustProviderType }}",
 "PolicyReferenceName": "{{ PolicyReferenceName }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.verified_access_trust_providers (
 TrustProviderType,
 PolicyReferenceName,
 region
)
SELECT 
{{ TrustProviderType }},
 {{ PolicyReferenceName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "TrustProviderType": "{{ TrustProviderType }}",
 "DeviceTrustProviderType": "{{ DeviceTrustProviderType }}",
 "UserTrustProviderType": "{{ UserTrustProviderType }}",
 "OidcOptions": {
  "Issuer": "{{ Issuer }}",
  "AuthorizationEndpoint": "{{ AuthorizationEndpoint }}",
  "TokenEndpoint": "{{ TokenEndpoint }}",
  "UserInfoEndpoint": "{{ UserInfoEndpoint }}",
  "ClientId": "{{ ClientId }}",
  "ClientSecret": "{{ ClientSecret }}",
  "Scope": "{{ Scope }}"
 },
 "DeviceOptions": {
  "TenantId": "{{ TenantId }}",
  "PublicSigningKeyUrl": "{{ PublicSigningKeyUrl }}"
 },
 "PolicyReferenceName": "{{ PolicyReferenceName }}",
 "Description": "{{ Description }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "SseSpecification": {
  "KmsKeyArn": "{{ KmsKeyArn }}",
  "CustomerManagedKeyEnabled": "{{ CustomerManagedKeyEnabled }}"
 }
}
>>>
--all properties
INSERT INTO aws.ec2.verified_access_trust_providers (
 TrustProviderType,
 DeviceTrustProviderType,
 UserTrustProviderType,
 OidcOptions,
 DeviceOptions,
 PolicyReferenceName,
 Description,
 Tags,
 SseSpecification,
 region
)
SELECT 
 {{ TrustProviderType }},
 {{ DeviceTrustProviderType }},
 {{ UserTrustProviderType }},
 {{ OidcOptions }},
 {{ DeviceOptions }},
 {{ PolicyReferenceName }},
 {{ Description }},
 {{ Tags }},
 {{ SseSpecification }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.verified_access_trust_providers
WHERE data__Identifier = '<VerifiedAccessTrustProviderId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>verified_access_trust_providers</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVerifiedAccessTrustProvider,
ec2:DescribeVerifiedAccessTrustProviders,
ec2:CreateTags,
ec2:DescribeTags,
sso:GetSharedSsoConfiguration,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
ec2:DeleteVerifiedAccessTrustProvider,
ec2:DeleteTags,
ec2:DescribeVerifiedAccessTrustProviders,
ec2:DescribeTags,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### List
```json
ec2:DescribeVerifiedAccessTrustProviders,
ec2:DescribeTags,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

