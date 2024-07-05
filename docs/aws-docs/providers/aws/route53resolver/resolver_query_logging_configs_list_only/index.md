---
title: resolver_query_logging_configs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_query_logging_configs_list_only
  - route53resolver
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

Lists <code>resolver_query_logging_configs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/resolver_query_logging_configs/"><code>resolver_query_logging_configs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_query_logging_configs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::ResolverQueryLoggingConfig.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.resolver_query_logging_configs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>AccountId</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>ResolverQueryLogConfigStatus, possible values are CREATING, CREATED, DELETED AND FAILED.</td></tr>
<tr><td><CopyableCode code="share_status" /></td><td><code>string</code></td><td>ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.</td></tr>
<tr><td><CopyableCode code="association_count" /></td><td><code>integer</code></td><td>Count</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>ResolverQueryLogConfigName</td></tr>
<tr><td><CopyableCode code="creator_request_id" /></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><CopyableCode code="destination_arn" /></td><td><code>string</code></td><td>destination arn</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
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
Lists all <code>resolver_query_logging_configs</code> in a region.
```sql
SELECT
region,
id
FROM aws.route53resolver.resolver_query_logging_configs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resolver_query_logging_configs_list_only</code> resource, see <a href="/providers/aws/route53resolver/resolver_query_logging_configs/#permissions"><code>resolver_query_logging_configs</code></a>


