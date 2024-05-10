---
title: group
hide_title: false
hide_table_of_contents: false
keywords:
  - group
  - resourcegroups
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


Gets or updates an individual <code>group</code> resource, use <code>groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for ResourceGroups::Group</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.resourcegroups.group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the resource group</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the resource group</td></tr>
<tr><td><CopyableCode code="resource_query" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Resource Group ARN.</td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resources" /></td><td><code>array</code></td><td></td></tr>
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
name,
description,
resource_query,
tags,
arn,
configuration,
resources
FROM aws.resourcegroups.group
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## Permissions

To operate on the <code>group</code> resource, the following permissions are required:

### Read
```json
resource-groups:GetGroup,
resource-groups:GetGroupQuery,
resource-groups:GetTags,
resource-groups:GetGroupConfiguration,
resource-groups:ListGroupResources
```

### Update
```json
resource-groups:UpdateGroup,
resource-groups:GetTags,
resource-groups:GetGroupQuery,
resource-groups:UpdateGroupQuery,
resource-groups:Tag,
resource-groups:Untag,
resource-groups:PutGroupConfiguration,
resource-groups:GetGroupConfiguration,
resource-groups:ListGroupResources,
resource-groups:GroupResources,
resource-groups:UnGroupResources
```

