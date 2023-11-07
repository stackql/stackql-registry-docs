---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
  - networkmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>sites</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>sites</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.sites</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SiteArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the site.</td></tr>
<tr><td><code>SiteId</code></td><td><code>string</code></td><td>The ID of the site.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the site.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags for the site.</td></tr>
<tr><td><code>GlobalNetworkId</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>Location</code></td><td><code>undefined</code></td><td>The location of the site.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.networkmanager.sites<br/>WHERE region = 'us-east-1'
</pre>
