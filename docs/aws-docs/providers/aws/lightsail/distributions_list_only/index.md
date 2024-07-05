---
title: distributions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - distributions_list_only
  - lightsail
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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Distribution</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.distributions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="distribution_name" /></td><td><code>string</code></td><td>The name for the distribution.</td></tr>
<tr><td><CopyableCode code="distribution_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="bundle_id" /></td><td><code>string</code></td><td>The bundle ID to use for the distribution.</td></tr>
<tr><td><CopyableCode code="ip_address_type" /></td><td><code>string</code></td><td>The IP address type for the distribution.</td></tr>
<tr><td><CopyableCode code="cache_behaviors" /></td><td><code>array</code></td><td>An array of objects that describe the per-path cache behavior for the distribution.</td></tr>
<tr><td><CopyableCode code="cache_behavior_settings" /></td><td><code>object</code></td><td>An object that describes the cache behavior settings for the distribution.</td></tr>
<tr><td><CopyableCode code="default_cache_behavior" /></td><td><code>object</code></td><td>An object that describes the default cache behavior for the distribution.</td></tr>
<tr><td><CopyableCode code="origin" /></td><td><code>object</code></td><td>An object that describes the origin resource for the distribution, such as a Lightsail instance or load balancer.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the distribution.</td></tr>
<tr><td><CopyableCode code="able_to_update_bundle" /></td><td><code>boolean</code></td><td>Indicates whether the bundle that is currently applied to your distribution, specified using the distributionName parameter, can be changed to another bundle.</td></tr>
<tr><td><CopyableCode code="is_enabled" /></td><td><code>boolean</code></td><td>Indicates whether the distribution is enabled.</td></tr>
<tr><td><CopyableCode code="certificate_name" /></td><td><code>string</code></td><td>The certificate attached to the Distribution.</td></tr>
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
Lists all <code>distributions</code> in a region.
```sql
SELECT
region,
distribution_name
FROM aws.lightsail.distributions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>distributions_list_only</code> resource, see <a href="/providers/aws/lightsail/distributions/#permissions"><code>distributions</code></a>


