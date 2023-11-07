---
title: cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster
  - emr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster</td></tr>
<tr><td><b>Id</b></td><td><code>aws.emr.cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Steps</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>StepConcurrencyLevel</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>EbsRootVolumeSize</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>OSReleaseLabel</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServiceRole</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LogUri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BootstrapActions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>MasterPublicDNS</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Configurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ReleaseLabel</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ManagedScalingPolicy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>LogEncryptionKmsKeyId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AdditionalInfo</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>AutoTerminationPolicy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>KerberosAttributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Applications</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AutoScalingRole</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CustomAmiId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Instances</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ScaleDownBehavior</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>JobFlowRole</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>VisibleToAllUsers</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>SecurityConfiguration</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.emr.cluster<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
