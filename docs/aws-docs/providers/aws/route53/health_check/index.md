---
title: health_check
hide_title: false
hide_table_of_contents: false
keywords:
  - health_check
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


Gets or updates an individual <code>health_check</code> resource, use <code>health_checks</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_check</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53::HealthCheck.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53.health_check" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="health_check_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
health_check_id,
health_check_config,
health_check_tags
FROM aws.route53.health_check
WHERE data__Identifier = '<HealthCheckId>';
```


## Permissions

To operate on the <code>health_check</code> resource, the following permissions are required:

### Read
```json
route53:GetHealthCheck,
route53:ListTagsForResource
```

### Update
```json
route53:UpdateHealthCheck,
route53:ChangeTagsForResource,
route53:ListTagsForResource,
cloudwatch:DescribeAlarms
```

