---
title: ingest_configuration_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - ingest_configuration_tags
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

Expands all tag keys and values for <code>ingest_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ingest_configuration_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::IngestConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.ingest_configuration_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>IngestConfiguration ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>IngestConfiguration</td></tr>
<tr><td><CopyableCode code="stage_arn" /></td><td><code>string</code></td><td>Stage ARN. A value other than an empty string indicates that stage is linked to IngestConfiguration. Default: "" (recording is disabled).</td></tr>
<tr><td><CopyableCode code="participant_id" /></td><td><code>string</code></td><td>Participant Id is automatically generated on creation and assigned.</td></tr>
<tr><td><CopyableCode code="ingest_protocol" /></td><td><code>string</code></td><td>Ingest Protocol.</td></tr>
<tr><td><CopyableCode code="insecure_ingest" /></td><td><code>boolean</code></td><td>Whether ingest configuration allows insecure ingest.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>State of IngestConfiguration which determines whether IngestConfiguration is in use or not.</td></tr>
<tr><td><CopyableCode code="stream_key" /></td><td><code>string</code></td><td>Stream-key value.</td></tr>
<tr><td><CopyableCode code="user_id" /></td><td><code>string</code></td><td>User defined indentifier for participant associated with IngestConfiguration.</td></tr>
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
Expands tags for all <code>ingest_configurations</code> in a region.
```sql
SELECT
region,
arn,
name,
stage_arn,
participant_id,
ingest_protocol,
insecure_ingest,
state,
stream_key,
user_id,
tag_key,
tag_value
FROM aws.ivs.ingest_configuration_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>ingest_configuration_tags</code> resource, see <a href="/providers/aws/ivs/ingest_configurations/#permissions"><code>ingest_configurations</code></a>

