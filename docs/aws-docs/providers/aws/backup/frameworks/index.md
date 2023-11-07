---
title: frameworks
hide_title: false
hide_table_of_contents: false
keywords:
  - frameworks
  - backup
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>frameworks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>frameworks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>frameworks</td></tr>
<tr><td><b>Id</b></td><td><code>aws.backup.frameworks</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>FrameworkName</code></td><td><code>string</code></td><td>The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</td></tr>
<tr><td><code>FrameworkDescription</code></td><td><code>string</code></td><td>An optional description of the framework with a maximum 1,024 characters.</td></tr>
<tr><td><code>FrameworkArn</code></td><td><code>string</code></td><td>An Amazon Resource Name (ARN) that uniquely identifies Framework as a resource</td></tr>
<tr><td><code>DeploymentStatus</code></td><td><code>string</code></td><td>The deployment status of a framework. The statuses are: `CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | COMPLETED | FAILED`</td></tr>
<tr><td><code>CreationTime</code></td><td><code>string</code></td><td>The date and time that a framework is created, in ISO 8601 representation. The value of CreationTime is accurate to milliseconds. For example, 2020-07-10T15:00:00.000-08:00 represents the 10th of July 2020 at 3:00 PM 8 hours behind UTC.</td></tr>
<tr><td><code>FrameworkControls</code></td><td><code>array</code></td><td>Contains detailed information about all of the controls of a framework. Each framework must contain at least one control.</td></tr>
<tr><td><code>FrameworkStatus</code></td><td><code>string</code></td><td>A framework consists of one or more controls. Each control governs a resource, such as backup plans, backup selections, backup vaults, or recovery points. You can also turn AWS Config recording on or off for each resource. The statuses are:&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;`ACTIVE` when recording is turned on for all resources governed by the framework.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;`PARTIALLY_ACTIVE` when recording is turned off for at least one resource governed by the framework.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;`INACTIVE` when recording is turned off for all resources governed by the framework.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;`UNAVAILABLE` when AWS Backup is unable to validate recording status at this time.</td></tr>
<tr><td><code>FrameworkTags</code></td><td><code>array</code></td><td>Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.backup.frameworks<br/>WHERE region = 'us-east-1'
</pre>
