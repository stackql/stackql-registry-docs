---
title: hubs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - hubs_list_only
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

Lists <code>hubs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/hubs/"><code>hubs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hubs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::Hub resource represents the implementation of the AWS Security Hub service in your account. One hub resource is created for each Region in which you enable Security Hub.<br /></td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.hubs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>An ARN is automatically created for the customer.</td></tr>
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
Lists all <code>hubs</code> in a region.
```sql
SELECT
region,
arn
FROM aws.securityhub.hubs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>hubs_list_only</code> resource, see <a href="/providers/aws/securityhub/hubs/#permissions"><code>hubs</code></a>

