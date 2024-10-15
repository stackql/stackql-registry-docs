---
title: cloud_manifest_files
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_manifest_files
  - azure_stack
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>cloud_manifest_files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_manifest_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack.cloud_manifest_files" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_manifest_files', value: 'view', },
        { label: 'cloud_manifest_files', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="deployment_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The entity tag used for optimistic concurrency when modifying the resource. |
| <CopyableCode code="signature" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
| <CopyableCode code="verificationVersion" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="etag" /> | `string` | The entity tag used for optimistic concurrency when modifying the resource. |
| <CopyableCode code="properties" /> | `object` | Cloud specific manifest JSON properties. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="verificationVersion" /> | Returns a cloud specific manifest JSON file. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Returns a cloud specific manifest JSON file with latest version. |

## `SELECT` examples

Returns a cloud specific manifest JSON file with latest version.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_manifest_files', value: 'view', },
        { label: 'cloud_manifest_files', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
deployment_data,
etag,
signature,
type,
verificationVersion
FROM azure_stack.azure_stack.vw_cloud_manifest_files
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure_stack.azure_stack.cloud_manifest_files
;
```
</TabItem></Tabs>

