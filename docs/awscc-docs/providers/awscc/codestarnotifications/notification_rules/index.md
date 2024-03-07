---
title: notification_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_rules
  - codestarnotifications
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>notification_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>notification_rules</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.codestarnotifications.notification_rules</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>notification_rules</code> resource, the following permissions are required:

### Create
```json
codestar-notifications:createNotificationRule
```

### List
```json
codestar-notifications:listNotificationRules
```


## Example
```sql
SELECT
region,
arn
FROM awscc.codestarnotifications.notification_rules
WHERE region = 'us-east-1'
```
