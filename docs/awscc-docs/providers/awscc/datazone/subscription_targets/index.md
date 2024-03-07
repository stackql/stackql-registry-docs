---
title: subscription_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_targets
  - datazone
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>subscription_targets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>subscription_targets</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datazone.subscription_targets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which subscription target is created.</td></tr>
<tr><td><code>environment_id</code></td><td><code>string</code></td><td>The ID of the environment in which subscription target is created.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the subscription target.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>subscription_targets</code> resource, the following permissions are required:

### Create
```json
datazone:CreateSubscriptionTarget,
datazone:GetSubscriptionTarget,
iam:PassRole
```

### List
```json
datazone:ListSubscriptionTargets
```


## Example
```sql
SELECT
region,
domain_id,
environment_id,
id
FROM awscc.datazone.subscription_targets
WHERE region = 'us-east-1'
```
