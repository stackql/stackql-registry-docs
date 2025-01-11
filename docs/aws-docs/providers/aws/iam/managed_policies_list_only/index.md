---
title: managed_policies_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_policies_list_only
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

Lists <code>managed_policies</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/managed_policies/"><code>managed_policies</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_policies_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new managed policy for your AWS-account.<br />This operation creates a policy version with a version identifier of <code>v1</code> and sets v1 as the policy's default version. For more information about policy versions, see &#91;Versioning for managed policies&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html) in the *IAM User Guide*.<br />As a best practice, you can validate your IAM policies. To learn more, see &#91;Validating IAM policies&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html) in the *IAM User Guide*.<br />For more information about managed policies in general, see &#91;Managed policies and inline policies&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.managed_policies_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="policy_arn" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>managed_policies</code> in a region.
```sql
SELECT
region,
policy_arn
FROM aws.iam.managed_policies_list_only
;
```


## Permissions

For permissions required to operate on the <code>managed_policies_list_only</code> resource, see <a href="/providers/aws/iam/managed_policies/#permissions"><code>managed_policies</code></a>

