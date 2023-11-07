---
title: matchmaking_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - matchmaking_configurations
  - gamelift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>matchmaking_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>matchmaking_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>matchmaking_configurations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.gamelift.matchmaking_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>GameProperties</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>GameSessionData</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AcceptanceTimeoutSeconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>NotificationTarget</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CustomEventData</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AdditionalPlayerCount</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>BackfillMode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RequestTimeoutSeconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>AcceptanceRequired</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>FlexMatchMode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RuleSetName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>GameSessionQueueArns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.gamelift.matchmaking_configurations<br/>WHERE region = 'us-east-1'
</pre>
