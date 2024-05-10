---
title: tag_association
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_association
  - lakeformation
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


Gets or updates an individual <code>tag_association</code> resource, use <code>tag_associations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema representing a Lake Formation Tag Association. While tag associations are not explicit Lake Formation resources, this CloudFormation resource can be used to associate tags with Lake Formation entities.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lakeformation.tag_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resource" /></td><td><code>object</code></td><td>Resource to tag with the Lake Formation Tags</td></tr>
<tr><td><CopyableCode code="lf_tags" /></td><td><code>array</code></td><td>List of Lake Formation Tags to associate with the Lake Formation Resource</td></tr>
<tr><td><CopyableCode code="resource_identifier" /></td><td><code>string</code></td><td>Unique string identifying the resource. Used as primary identifier, which ideally should be a string</td></tr>
<tr><td><CopyableCode code="tags_identifier" /></td><td><code>string</code></td><td>Unique string identifying the resource's tags. Used as primary identifier, which ideally should be a string</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
resource,
lf_tags,
resource_identifier,
tags_identifier
FROM aws.lakeformation.tag_association
WHERE region = 'us-east-1' AND data__Identifier = '<ResourceIdentifier>|<TagsIdentifier>';
```


## Permissions

To operate on the <code>tag_association</code> resource, the following permissions are required:

### Read
```json
lakeformation:GetResourceLFTags,
glue:GetDatabase,
glue:GetTable
```

