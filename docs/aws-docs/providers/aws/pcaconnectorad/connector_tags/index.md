---
title: connector_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_tags
  - pcaconnectorad
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

Expands all tag keys and values for <code>connectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::PCAConnectorAD::Connector Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcaconnectorad.connector_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="certificate_authority_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="connector_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="directory_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_information" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>connectors</code> in a region.
```sql
SELECT
region,
certificate_authority_arn,
connector_arn,
directory_id,
vpc_information,
tag_key,
tag_value
FROM aws.pcaconnectorad.connector_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>connector_tags</code> resource, see <a href="/providers/aws/pcaconnectorad/connectors/#permissions"><code>connectors</code></a>


