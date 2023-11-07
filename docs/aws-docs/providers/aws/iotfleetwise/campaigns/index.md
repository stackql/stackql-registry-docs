---
title: campaigns
hide_title: false
hide_table_of_contents: false
keywords:
  - campaigns
  - iotfleetwise
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>campaigns</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>campaigns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iotfleetwise.campaigns</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Status</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Action</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CreationTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Compression</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Priority</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>SignalsToCollect</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>StartTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ExpiryTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LastModificationTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SpoolingMode</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>SignalCatalogArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PostTriggerCollectionDuration</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>DataExtraDimensions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>DiagnosticsMode</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>TargetArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CollectionScheme</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iotfleetwise.campaigns
WHERE region = 'us-east-1'
</pre>
