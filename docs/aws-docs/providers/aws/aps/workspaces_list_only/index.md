---
title: workspaces_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_list_only
  - aps
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

Lists <code>workspaces</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/workspaces/"><code>workspaces</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::APS::Workspace</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.aps.workspaces_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>Required to identify a specific APS Workspace.</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>AMP Workspace alias.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Workspace arn.</td></tr>
<tr><td><CopyableCode code="alert_manager_definition" /></td><td><code>string</code></td><td>The AMP Workspace alert manager definition data</td></tr>
<tr><td><CopyableCode code="prometheus_endpoint" /></td><td><code>string</code></td><td>AMP Workspace prometheus endpoint</td></tr>
<tr><td><CopyableCode code="logging_configuration" /></td><td><code>object</code></td><td>Logging configuration</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>KMS Key ARN used to encrypt and decrypt AMP workspace data.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
Lists all <code>workspaces</code> in a region.
```sql
SELECT
region,
arn
FROM aws.aps.workspaces_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>workspaces_list_only</code> resource, see <a href="/providers/aws/aps/workspaces/#permissions"><code>workspaces</code></a>


