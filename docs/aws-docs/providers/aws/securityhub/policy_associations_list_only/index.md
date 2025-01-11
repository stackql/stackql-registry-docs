---
title: policy_associations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_associations_list_only
  - securityhub
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

Lists <code>policy_associations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/policy_associations/"><code>policy_associations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_associations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::PolicyAssociation resource represents the AWS Security Hub Central Configuration Policy associations in your Target. Only the AWS Security Hub delegated administrator can create the resouce from the home region.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.policy_associations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="association_identifier" /></td><td><code>string</code></td><td>A unique identifier to indicates if the target has an association</td></tr>
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
Lists all <code>policy_associations</code> in a region.
```sql
SELECT
region,
association_identifier
FROM aws.securityhub.policy_associations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>policy_associations_list_only</code> resource, see <a href="/providers/aws/securityhub/policy_associations/#permissions"><code>policy_associations</code></a>

