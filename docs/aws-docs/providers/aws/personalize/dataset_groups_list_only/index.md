---
title: dataset_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset_groups_list_only
  - personalize
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

Lists <code>dataset_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/dataset_groups/"><code>dataset_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::Personalize::DatasetGroup.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.personalize.dataset_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="dataset_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the dataset group.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the new dataset group.</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name(ARN) of a AWS Key Management Service (KMS) key used to encrypt the datasets.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the AWS Identity and Access Management (IAM) role that has permissions to access the AWS Key Management Service (KMS) key. Supplying an IAM role is only valid when also specifying a KMS key.</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The domain of a Domain dataset group.</td></tr>
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
Lists all <code>dataset_groups</code> in a region.
```sql
SELECT
region,
dataset_group_arn
FROM aws.personalize.dataset_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>dataset_groups_list_only</code> resource, see <a href="/providers/aws/personalize/dataset_groups/#permissions"><code>dataset_groups</code></a>


