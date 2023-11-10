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
Gets an individual <code>tag_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>tag_association</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lakeformation.tag_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource</code></td><td><code>object</code></td><td>Resource to tag with the Lake Formation Tags</td></tr>
<tr><td><code>l_ftags</code></td><td><code>array</code></td><td>List of Lake Formation Tags to associate with the Lake Formation Resource</td></tr>
<tr><td><code>resource_identifier</code></td><td><code>string</code></td><td>Unique string identifying the resource. Used as primary identifier, which ideally should be a string</td></tr>
<tr><td><code>tags_identifier</code></td><td><code>string</code></td><td>Unique string identifying the resource's tags. Used as primary identifier, which ideally should be a string</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
resource,
l_ftags,
resource_identifier,
tags_identifier
FROM aws.lakeformation.tag_association
WHERE region = 'us-east-1'
AND data__Identifier = '<ResourceIdentifier>'
AND data__Identifier = '<TagsIdentifier>'
```
