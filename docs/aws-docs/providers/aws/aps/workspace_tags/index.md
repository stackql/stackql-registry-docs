---
title: workspace_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_tags
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

Expands all tag keys and values for <code>workspaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::APS::Workspace</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.aps.workspace_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>Required to identify a specific APS Workspace.</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>AMP Workspace alias.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Workspace arn.</td></tr>
<tr><td><CopyableCode code="alert_manager_definition" /></td><td><code>string</code></td><td>The AMP Workspace alert manager definition data</td></tr>
<tr><td><CopyableCode code="prometheus_endpoint" /></td><td><code>string</code></td><td>AMP Workspace prometheus endpoint</td></tr>
<tr><td><CopyableCode code="logging_configuration" /></td><td><code>object</code></td><td>Logging configuration</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>KMS Key ARN used to encrypt and decrypt AMP workspace data.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>workspaces</code> in a region.
```sql
SELECT
region,
workspace_id,
alias,
arn,
alert_manager_definition,
prometheus_endpoint,
logging_configuration,
kms_key_arn,
tag_key,
tag_value
FROM aws.aps.workspace_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>workspace_tags</code> resource, see <a href="/providers/aws/aps/workspaces/#permissions"><code>workspaces</code></a>

