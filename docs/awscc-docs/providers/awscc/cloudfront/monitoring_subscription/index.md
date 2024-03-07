---
title: monitoring_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - monitoring_subscription
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
Gets an individual <code>monitoring_subscription</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitoring_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>monitoring_subscription</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudfront.monitoring_subscription</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>distribution_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>monitoring_subscription</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
distribution_id,
monitoring_subscription
FROM awscc.cloudfront.monitoring_subscription
WHERE data__Identifier = '{DistributionId}';
```

## Permissions

To operate on the <code>monitoring_subscription</code> resource, the following permissions are required:

### Delete
```json
cloudfront:DeleteMonitoringSubscription
```

### Read
```json
cloudfront:GetMonitoringSubscription
```

