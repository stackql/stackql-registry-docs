---
title: clusters_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_list_only
  - route53recoverycontrol
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

Lists <code>clusters</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/clusters/"><code>clusters</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Route53 Recovery Control Cluster resource schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoverycontrol.clusters_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of a Cluster. You can use any non-white space character in the name</td></tr>
<tr><td><CopyableCode code="cluster_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cluster.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Deployment status of a resource. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</td></tr>
<tr><td><CopyableCode code="cluster_endpoints" /></td><td><code>array</code></td><td>Endpoints for the cluster.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
Lists all <code>clusters</code> in a region.
```sql
SELECT
region,
cluster_arn
FROM aws.route53recoverycontrol.clusters_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>clusters_list_only</code> resource, see <a href="/providers/aws/route53recoverycontrol/clusters/#permissions"><code>clusters</code></a>


