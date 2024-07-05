---
title: ipam_scopes_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_scopes_list_only
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

Lists <code>ipam_scopes</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/ipam_scopes/"><code>ipam_scopes</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_scopes_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMScope Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipam_scopes_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ipam_scope_id" /></td><td><code>string</code></td><td>Id of the IPAM scope.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM scope.</td></tr>
<tr><td><CopyableCode code="ipam_id" /></td><td><code>string</code></td><td>The Id of the IPAM this scope is a part of.</td></tr>
<tr><td><CopyableCode code="ipam_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM this scope is a part of.</td></tr>
<tr><td><CopyableCode code="ipam_scope_type" /></td><td><code>string</code></td><td>Determines whether this scope contains publicly routable space or space for a private network</td></tr>
<tr><td><CopyableCode code="is_default" /></td><td><code>boolean</code></td><td>Is this one of the default scopes created with the IPAM.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pool_count" /></td><td><code>integer</code></td><td>The number of pools that currently exist in this scope.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
Lists all <code>ipam_scopes</code> in a region.
```sql
SELECT
region,
ipam_scope_id
FROM aws.ec2.ipam_scopes_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>ipam_scopes_list_only</code> resource, see <a href="/providers/aws/ec2/ipam_scopes/#permissions"><code>ipam_scopes</code></a>


