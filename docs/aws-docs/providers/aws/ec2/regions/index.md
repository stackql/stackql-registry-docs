---
title: regions
hide_title: false
hide_table_of_contents: false
keywords:
  - regions
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.regions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `optInStatus` | `string` | The Region opt-in status. The possible values are &lt;code&gt;opt-in-not-required&lt;/code&gt;, &lt;code&gt;opted-in&lt;/code&gt;, and &lt;code&gt;not-opted-in&lt;/code&gt;. |
| `regionEndpoint` | `string` | The Region service endpoint. |
| `regionName` | `string` | The name of the Region. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `regions_Describe` | `SELECT` |  |
