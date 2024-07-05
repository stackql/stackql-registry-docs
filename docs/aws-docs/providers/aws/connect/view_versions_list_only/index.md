---
title: view_versions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - view_versions_list_only
  - connect
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

Lists <code>view_versions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/view_versions/"><code>view_versions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>view_versions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::ViewVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.view_versions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="view_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the view for which a version is being created.</td></tr>
<tr><td><CopyableCode code="view_version_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the created view version.</td></tr>
<tr><td><CopyableCode code="version_description" /></td><td><code>string</code></td><td>The description for the view version.</td></tr>
<tr><td><CopyableCode code="view_content_sha256" /></td><td><code>string</code></td><td>The view content hash to be checked.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>integer</code></td><td>The version of the view.</td></tr>
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
Lists all <code>view_versions</code> in a region.
```sql
SELECT
region,
view_version_arn
FROM aws.connect.view_versions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>view_versions_list_only</code> resource, see <a href="/providers/aws/connect/view_versions/#permissions"><code>view_versions</code></a>


