---
title: campaign
hide_title: false
hide_table_of_contents: false
keywords:
  - campaign
  - pinpoint
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>campaign</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>campaign</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>campaign</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pinpoint.campaign</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SegmentId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Priority</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>TemplateConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>IsPaused</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>AdditionalTreatments</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SegmentVersion</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>TreatmentDescription</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MessageConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Limits</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CampaignId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>HoldoutPercent</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Schedule</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CustomDeliveryConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApplicationId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CampaignHook</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>TreatmentName</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.pinpoint.campaign
WHERE region = 'us-east-1' AND data__Identifier = '&lt;CampaignId&gt;'
</pre>
