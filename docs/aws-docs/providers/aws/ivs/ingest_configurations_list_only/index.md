---
title: ingest_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - ingest_configurations_list_only
  - ivs
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

Lists <code>ingest_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/ingest_configurations/"><code>ingest_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ingest_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::IngestConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.ingest_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>IngestConfiguration ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
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
Lists all <code>ingest_configurations</code> in a region.
```sql
SELECT
region,
arn
FROM aws.ivs.ingest_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>ingest_configurations_list_only</code> resource, see <a href="/providers/aws/ivs/ingest_configurations/#permissions"><code>ingest_configurations</code></a>

