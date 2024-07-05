---
title: health_checks_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - health_checks_list_only
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

Lists <code>health_checks</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/health_checks/"><code>health_checks</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_checks_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53::HealthCheck.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53.health_checks_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="health_check_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="health_check_config" /></td><td><code>object</code></td><td>A complex type that contains information about the health check.</td></tr>
<tr><td><CopyableCode code="health_check_tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
Lists all <code>health_checks</code> in a region.
```sql
SELECT
region,
health_check_id
FROM aws.route53.health_checks_list_only
;
```


## Permissions

For permissions required to operate on the <code>health_checks_list_only</code> resource, see <a href="/providers/aws/route53/health_checks/#permissions"><code>health_checks</code></a>


