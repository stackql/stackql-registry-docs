---
title: network_insights_access_scope
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_access_scope
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>network_insights_access_scope</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_access_scope</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>network_insights_access_scope</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.network_insights_access_scope</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>network_insights_access_scope_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_insights_access_scope_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>updated_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>match_paths</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>exclude_paths</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
network_insights_access_scope_id,
network_insights_access_scope_arn,
created_date,
updated_date,
tags,
match_paths,
exclude_paths
FROM awscc.ec2.network_insights_access_scope
WHERE data__Identifier = '<NetworkInsightsAccessScopeId>';
```

## Permissions

To operate on the <code>network_insights_access_scope</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeNetworkInsightsAccessScopes,
ec2:GetNetworkInsightsAccessScopeContent
```

### Update
```json
ec2:DescribeNetworkInsightsAccessScopes,
ec2:GetNetworkInsightsAccessScopeContent,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteNetworkInsightsAccessScope,
ec2:DeleteTags
```

