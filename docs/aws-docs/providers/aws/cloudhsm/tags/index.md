---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - cloudhsm
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudhsm.tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `NextToken` | `string` | An opaque string that indicates that the response contains only a subset of tags. Use this value in a subsequent &lt;code&gt;ListTags&lt;/code&gt; request to get more tags. |
| `TagList` | `array` | A list of tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_tags` | `SELECT` | `X-Amz-Target, data__ResourceId, region` | &lt;p&gt;Gets a list of tags for the specified AWS CloudHSM cluster.&lt;/p&gt; &lt;p&gt;This is a paginated operation, which means that each response might contain only a subset of all the tags. When the response contains only a subset of tags, it includes a &lt;code&gt;NextToken&lt;/code&gt; value. Use this value in a subsequent &lt;code&gt;ListTags&lt;/code&gt; request to get more tags. When you receive a response with no &lt;code&gt;NextToken&lt;/code&gt; (or an empty or null value), that means there are no more tags to get.&lt;/p&gt; |
| `tag_resource` | `EXEC` | `X-Amz-Target, data__ResourceId, data__TagList, region` | Adds or overwrites one or more tags for the specified AWS CloudHSM cluster. |
| `untag_resource` | `EXEC` | `X-Amz-Target, data__ResourceId, data__TagKeyList, region` | Removes the specified tag or tags from the specified AWS CloudHSM cluster. |
