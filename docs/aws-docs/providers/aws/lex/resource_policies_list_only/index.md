---
title: resource_policies_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policies_list_only
  - lex
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

Lists <code>resource_policies</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/resource_policies/"><code>resource_policies</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_policies_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource policy with specified policy statements that attaches to a Lex bot or bot alias.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lex.resource_policies_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.</td></tr>
<tr><td><CopyableCode code="revision_id" /></td><td><code>string</code></td><td>The current revision of the resource policy. Use the revision ID to make sure that you are updating the most current version of a resource policy when you add a policy statement to a resource, delete a resource, or update a resource.</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>A resource policy to add to the resource. The policy is a JSON structure following the IAM syntax that contains one or more statements that define the policy.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The Physical ID of the resource policy.</td></tr>
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
Lists all <code>resource_policies</code> in a region.
```sql
SELECT
region,
id
FROM aws.lex.resource_policies_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resource_policies_list_only</code> resource, see <a href="/providers/aws/lex/resource_policies/#permissions"><code>resource_policies</code></a>


