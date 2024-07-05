---
title: distributions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - distributions_list_only
  - cloudfront
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

Lists <code>distributions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/distributions/"><code>distributions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distributions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A distribution tells CloudFront where you want content to be delivered from, and the details about how to track and manage content delivery.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.distributions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="distribution_config" /></td><td><code>object</code></td><td>The distribution's configuration.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A complex type that contains zero or more <code>Tag</code> elements.</td></tr>
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
Lists all <code>distributions</code> in a region.
```sql
SELECT
region,
id
FROM aws.cloudfront.distributions_list_only
;
```


## Permissions

For permissions required to operate on the <code>distributions_list_only</code> resource, see <a href="/providers/aws/cloudfront/distributions/#permissions"><code>distributions</code></a>


