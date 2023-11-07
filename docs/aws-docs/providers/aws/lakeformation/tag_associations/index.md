---
title: tag_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_associations
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
Retrieves a list of <code>tag_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>tag_associations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lakeformation.tag_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Resource</code></td><td><code>undefined</code></td><td>Resource to tag with the Lake Formation Tags</td></tr>
<tr><td><code>LFTags</code></td><td><code>undefined</code></td><td>List of Lake Formation Tags to associate with the Lake Formation Resource</td></tr>
<tr><td><code>ResourceIdentifier</code></td><td><code>string</code></td><td>Unique string identifying the resource. Used as primary identifier, which ideally should be a string</td></tr>
<tr><td><code>TagsIdentifier</code></td><td><code>string</code></td><td>Unique string identifying the resource's tags. Used as primary identifier, which ideally should be a string</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.lakeformation.tag_associations<br/>WHERE region = 'us-east-1'
</pre>
