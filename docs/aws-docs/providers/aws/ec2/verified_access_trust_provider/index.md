---
title: verified_access_trust_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_access_trust_provider
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

Gets or operates on an individual <code>verified_access_trust_provider</code> resource, use <code>verified_access_trust_providers</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_trust_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::VerifiedAccessTrustProvider type describes a verified access trust provider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.verified_access_trust_provider" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="trust_provider_type" /></td><td><code>string</code></td><td>Type of trust provider. Possible values: user|device</td></tr>
<tr><td><CopyableCode code="device_trust_provider_type" /></td><td><code>string</code></td><td>The type of device-based trust provider. Possible values: jamf|crowdstrike</td></tr>
<tr><td><CopyableCode code="user_trust_provider_type" /></td><td><code>string</code></td><td>The type of device-based trust provider. Possible values: oidc|iam-identity-center</td></tr>
<tr><td><CopyableCode code="oidc_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="device_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_reference_name" /></td><td><code>string</code></td><td>The identifier to be used when working with policy rules.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The creation time.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>The last updated time.</td></tr>
<tr><td><CopyableCode code="verified_access_trust_provider_id" /></td><td><code>string</code></td><td>The ID of the Amazon Web Services Verified Access trust provider.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the Amazon Web Services Verified Access trust provider.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="sse_specification" /></td><td><code>object</code></td><td>The configuration options for customer provided KMS encryption.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
trust_provider_type,
device_trust_provider_type,
user_trust_provider_type,
oidc_options,
device_options,
policy_reference_name,
creation_time,
last_updated_time,
verified_access_trust_provider_id,
description,
tags,
sse_specification
FROM aws.ec2.verified_access_trust_provider
WHERE data__Identifier = '<VerifiedAccessTrustProviderId>';
```

## Permissions

To operate on the <code>verified_access_trust_provider</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeVerifiedAccessTrustProviders,
ec2:DescribeTags,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Update
```json
ec2:ModifyVerifiedAccessTrustProvider,
ec2:DescribeVerifiedAccessTrustProviders,
ec2:DescribeTags,
ec2:DeleteTags,
ec2:CreateTags,
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

