---
title: data_repository_associations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - data_repository_associations_list_only
  - fsx
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

Lists <code>data_repository_associations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/data_repository_associations/"><code>data_repository_associations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_repository_associations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an Amazon FSx for Lustre data repository association (DRA). A data repository association is a link between a directory on the file system and an Amazon S3 bucket or prefix. You can have a maximum of 8 data repository associations on a file system. Data repository associations are supported on all FSx for Lustre 2.12 and newer file systems, excluding <code>scratch_1</code> deployment type. <br />Each data repository association must have a unique Amazon FSx file system directory and a unique S3 bucket or prefix associated with it. You can configure a data repository association for automatic import only, for automatic export only, or for both. To learn more about linking a data repository to your file system, see &#91;Linking your file system to an S3 bucket&#93;(https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-dra-linked-data-repo.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fsx.data_repository_associations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="association_id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>data_repository_associations</code> in a region.
```sql
SELECT
region,
association_id
FROM aws.fsx.data_repository_associations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>data_repository_associations_list_only</code> resource, see <a href="/providers/aws/fsx/data_repository_associations/#permissions"><code>data_repository_associations</code></a>

