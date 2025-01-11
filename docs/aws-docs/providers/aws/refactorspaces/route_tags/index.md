---
title: route_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - route_tags
  - refactorspaces
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

Expands all tag keys and values for <code>routes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RefactorSpaces::Route Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.refactorspaces.route_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="path_resource_to_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="route_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="route_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_route" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="uri_path_route" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>routes</code> in a region.
```sql
SELECT
region,
path_resource_to_id,
arn,
application_identifier,
environment_identifier,
route_identifier,
route_type,
service_identifier,
default_route,
uri_path_route,
tag_key,
tag_value
FROM aws.refactorspaces.route_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>route_tags</code> resource, see <a href="/providers/aws/refactorspaces/routes/#permissions"><code>routes</code></a>

