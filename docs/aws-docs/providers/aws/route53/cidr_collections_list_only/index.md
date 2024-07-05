---
title: cidr_collections_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - cidr_collections_list_only
  - route53
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

Lists <code>cidr_collections</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/cidr_collections/"><code>cidr_collections</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cidr_collections_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53::CidrCollection.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53.cidr_collections_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>UUID of the CIDR collection.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A unique name for the CIDR collection.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon resource name (ARN) to uniquely identify the AWS resource.</td></tr>
<tr><td><CopyableCode code="locations" /></td><td><code>array</code></td><td>A complex type that contains information about the list of CIDR locations.</td></tr>
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
Lists all <code>cidr_collections</code> in a region.
```sql
SELECT
region,
id
FROM aws.route53.cidr_collections_list_only
;
```


## Permissions

For permissions required to operate on the <code>cidr_collections_list_only</code> resource, see <a href="/providers/aws/route53/cidr_collections/#permissions"><code>cidr_collections</code></a>


