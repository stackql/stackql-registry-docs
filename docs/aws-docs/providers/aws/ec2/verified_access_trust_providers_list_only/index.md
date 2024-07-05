---
title: verified_access_trust_providers_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_access_trust_providers_list_only
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

Lists <code>verified_access_trust_providers</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/verified_access_trust_providers/"><code>verified_access_trust_providers</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_trust_providers_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::VerifiedAccessTrustProvider type describes a verified access trust provider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.verified_access_trust_providers_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="trust_provider_type" /></td><td><code>string</code></td><td>Type of trust provider. Possible values: user|device</td></tr>
<tr><td><CopyableCode code="device_trust_provider_type" /></td><td><code>string</code></td><td>The type of device-based trust provider. Possible values: jamf|crowdstrike</td></tr>
<tr><td><CopyableCode code="user_trust_provider_type" /></td><td><code>string</code></td><td>The type of device-based trust provider. Possible values: oidc|iam-identity-center</td></tr>
<tr><td><CopyableCode code="oidc_options" /></td><td><code>object</code></td><td>The OpenID Connect details for an oidc -type, user-identity based trust provider.</td></tr>
<tr><td><CopyableCode code="device_options" /></td><td><code>object</code></td><td>The options for device identity based trust providers.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>verified_access_trust_providers</code> in a region.
```sql
SELECT
region,
verified_access_trust_provider_id
FROM aws.ec2.verified_access_trust_providers_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>verified_access_trust_providers_list_only</code> resource, see <a href="/providers/aws/ec2/verified_access_trust_providers/#permissions"><code>verified_access_trust_providers</code></a>


