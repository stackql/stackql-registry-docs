---
title: packaging_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - packaging_configurations_list_only
  - mediapackage
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

Lists <code>packaging_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/packaging_configurations/"><code>packaging_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packaging_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::PackagingConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.packaging_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the PackagingConfiguration.</td></tr>
<tr><td><CopyableCode code="packaging_group_id" /></td><td><code>string</code></td><td>The ID of a PackagingGroup.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the PackagingConfiguration.</td></tr>
<tr><td><CopyableCode code="cmaf_package" /></td><td><code>object</code></td><td>A CMAF packaging configuration.</td></tr>
<tr><td><CopyableCode code="dash_package" /></td><td><code>object</code></td><td>A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.</td></tr>
<tr><td><CopyableCode code="hls_package" /></td><td><code>object</code></td><td>An HTTP Live Streaming (HLS) packaging configuration.</td></tr>
<tr><td><CopyableCode code="mss_package" /></td><td><code>object</code></td><td>A Microsoft Smooth Streaming (MSS) PackagingConfiguration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
Lists all <code>packaging_configurations</code> in a region.
```sql
SELECT
region,
id
FROM aws.mediapackage.packaging_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>packaging_configurations_list_only</code> resource, see <a href="/providers/aws/mediapackage/packaging_configurations/#permissions"><code>packaging_configurations</code></a>


