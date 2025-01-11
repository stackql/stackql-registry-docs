---
title: cluster_subnet_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_subnet_groups_list_only
  - redshift
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

Lists <code>cluster_subnet_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/cluster_subnet_groups/"><code>cluster_subnet_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_subnet_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Amazon Redshift subnet group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.cluster_subnet_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_subnet_group_name" /></td><td><code>string</code></td><td>This name must be unique for all subnet groups that are created by your AWS account. If costumer do not provide it, cloudformation will generate it. Must not be "Default".</td></tr>
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
Lists all <code>cluster_subnet_groups</code> in a region.
```sql
SELECT
region,
cluster_subnet_group_name
FROM aws.redshift.cluster_subnet_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>cluster_subnet_groups_list_only</code> resource, see <a href="/providers/aws/redshift/cluster_subnet_groups/#permissions"><code>cluster_subnet_groups</code></a>

