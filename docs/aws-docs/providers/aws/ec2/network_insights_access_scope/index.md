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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>network_insights_access_scope</code> resource, use <code>network_insights_access_scopes</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_access_scope</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EC2::NetworkInsightsAccessScope</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_insights_access_scope" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="network_insights_access_scope_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_insights_access_scope_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="match_paths" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="exclude_paths" /></td><td><code>array</code></td><td></td></tr>
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
network_insights_access_scope_id,
network_insights_access_scope_arn,
created_date,
updated_date,
tags,
match_paths,
exclude_paths
FROM aws.ec2.network_insights_access_scope
WHERE region = 'us-east-1' AND data__Identifier = '<NetworkInsightsAccessScopeId>';
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

