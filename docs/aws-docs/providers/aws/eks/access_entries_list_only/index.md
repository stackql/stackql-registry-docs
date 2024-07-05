---
title: access_entries_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - access_entries_list_only
  - eks
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

Lists <code>access_entries</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/access_entries/"><code>access_entries</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_entries_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS AccessEntry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.access_entries_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The cluster that the access entry is created for.</td></tr>
<tr><td><CopyableCode code="principal_arn" /></td><td><code>string</code></td><td>The principal ARN that the access entry is created for.</td></tr>
<tr><td><CopyableCode code="username" /></td><td><code>string</code></td><td>The Kubernetes user that the access entry is associated with.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="access_entry_arn" /></td><td><code>string</code></td><td>The ARN of the access entry.</td></tr>
<tr><td><CopyableCode code="kubernetes_groups" /></td><td><code>array</code></td><td>The Kubernetes groups that the access entry is associated with.</td></tr>
<tr><td><CopyableCode code="access_policies" /></td><td><code>array</code></td><td>An array of access policies that are associated with the access entry.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The node type to associate with the access entry.</td></tr>
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
Lists all <code>access_entries</code> in a region.
```sql
SELECT
region,
principal_arn,
cluster_name
FROM aws.eks.access_entries_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>access_entries_list_only</code> resource, see <a href="/providers/aws/eks/access_entries/#permissions"><code>access_entries</code></a>


