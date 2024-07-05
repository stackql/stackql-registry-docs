---
title: frameworks_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - frameworks_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>frameworks</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/frameworks/"><code>frameworks</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>frameworks_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains detailed information about a framework. Frameworks contain controls, which evaluate and report on your backup events and resources. Frameworks generate daily compliance results.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.frameworks_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="framework_name" /></td><td><code>string</code></td><td>The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</td></tr>
<tr><td><CopyableCode code="framework_description" /></td><td><code>string</code></td><td>An optional description of the framework with a maximum 1,024 characters.</td></tr>
<tr><td><CopyableCode code="framework_arn" /></td><td><code>string</code></td><td>An Amazon Resource Name (ARN) that uniquely identifies Framework as a resource</td></tr>
<tr><td><CopyableCode code="deployment_status" /></td><td><code>string</code></td><td>The deployment status of a framework. The statuses are: `CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | COMPLETED | FAILED`</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The date and time that a framework is created, in ISO 8601 representation. The value of CreationTime is accurate to milliseconds. For example, 2020-07-10T15:00:00.000-08:00 represents the 10th of July 2020 at 3:00 PM 8 hours behind UTC.</td></tr>
<tr><td><CopyableCode code="framework_controls" /></td><td><code>array</code></td><td>Contains detailed information about all of the controls of a framework. Each framework must contain at least one control.</td></tr>
<tr><td><CopyableCode code="framework_status" /></td><td><code>string</code></td><td>A framework consists of one or more controls. Each control governs a resource, such as backup plans, backup selections, backup vaults, or recovery points. You can also turn AWS Config recording on or off for each resource. The statuses are:<br />`ACTIVE` when recording is turned on for all resources governed by the framework.<br />`PARTIALLY_ACTIVE` when recording is turned off for at least one resource governed by the framework.<br />`INACTIVE` when recording is turned off for all resources governed by the framework.<br />`UNAVAILABLE` when AWS Backup is unable to validate recording status at this time.</td></tr>
<tr><td><CopyableCode code="framework_tags" /></td><td><code>array</code></td><td>Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>frameworks</code> in a region.
```sql
SELECT
region,
framework_arn
FROM aws.backup.frameworks_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>frameworks_list_only</code> resource, see <a href="/providers/aws/backup/frameworks/#permissions"><code>frameworks</code></a>


